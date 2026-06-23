import numpy as np
import os
import re
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'code'))

from meslf.networks.pandapower_network import *
from meslf.networks.gaslib_network import *
from meslf.networks.heterogeneous_network import *

# %%

def create_network(network_name_e=None, network_name_g=None, p2g=True, adjust_power=False, same_electrical_node=False):
    flow = 'average' # 'min' # 'max'
    pressure = 'max' # 'min' # 'average'
    gas_type = 'hydrogen' # 'natural'
                        
    link_settings = {'friction' : 'friction_weymouth', # 'friction_pole'
                     'link_type' : 'pipe_high', # 'pipe_low'
                     'link_equation_formulation' : 'dp_of_q'} # 'q_of_dp'

    resistor = False # True
    scale_var = 'per_unit' # None

    gaslib_network = GasLibNetwork(network_name=network_name_g)
    network_g, node_data_g, link_data_g = gaslib_network.create_network(flow=flow,
                                                                        pressure=pressure,
                                                                        gas_type=gas_type,
                                                                        link_settings=link_settings,
                                                                        resistor=resistor,
                                                                        scale_var=scale_var)
    
    
    formulation = 'complex_power'
    scale_var = 'per_unit'
    change_first_slack = True
    
    pandapower_network = PandapowerNetwork(network_name=network_name_e)
    network_e, data_e = pandapower_network.create_network(ignore_nodes=[],
                                                          formulation=formulation,
                                                          scale_var=scale_var,
                                                          change_first_slack=change_first_slack)
    

    eta = 0.8
    GHV = 1.418*10**8
    unit_params = {'eta': eta,
                   'GHV': GHV}
    unit_type = 'p2g'
    
    scale_var_params = {'Ebase' : network_e.nodes[0].scale_var_params['Sbase'],
                        'GHVbase' : network_e.nodes[0].scale_var_params['Sbase'] / network_g.nodes[0].scale_var_params['qbase']}
        
    network_c = HeterogeneousNetwork('Test network for 2 coupling units')
    c0 = HeterogeneousNode(name='c0', 
                           bc_type=[], unit_type=unit_type, unit_params=unit_params,
                           scale_var=scale_var, scale_var_params=scale_var_params)
    network_c.add_node(c0)
    coupling_link_g = GasLink(name='{}_{}'.format(c0.name, network_g.nodes[0].name),
                              start_node=c0, end_node=network_g.nodes[0], 
                              link_type='dummy',
                              scale_var=scale_var, scale_var_params=network_g.nodes[0].scale_var_params)
    network_g.add_link(coupling_link_g) 
    coupling_link_e = ElectricalLink(name='{}_{}'.format(network_e.nodes[0].name, c0.name), 
                                     start_node=network_e.nodes[0], end_node=c0, 
                                     bc_type=['Q_start'], Q_start=0, link_type='dummy', 
                                     scale_var=scale_var, scale_var_params=network_e.nodes[0].scale_var_params)
    network_e.add_link(coupling_link_e)
    
    
    eta = 0.8
    GHV = 1.418*10**8
    unit_params = {'eta': eta,
                   'GHV': GHV}
    
    if p2g:
        unit_type = 'p2g'

        c = HeterogeneousNode(name='c1', 
                              bc_type=[], unit_type=unit_type, unit_params=unit_params,
                              scale_var=scale_var, scale_var_params=None)
        network_c.add_node(c)
        
        no_suitable_node_g = True  
        for node in network_g.nodes: # Replacing source from terminal link to coupling link
            if ('q' in node.bc_type) and (node.half_links[0].q < 0):
                node_g = node
                P_c = -GHV*node.half_links[0].q / eta
                coupling_link_g = GasLink(name='{}_{}'.format(c.name, node.name),
                                          start_node=c, end_node=node, 
                                          bc_type=['q'], q=-node.half_links[0].q, link_type='dummy',
                                          scale_var=scale_var, scale_var_params=node.scale_var_params)
                network_g.add_link(coupling_link_g)
                node.half_links[0].q = 0
                no_suitable_node_g = False
                break
        
        if no_suitable_node_g:
            print("No source node for gas network found. Using sink instead.")
            for node in network_g.nodes: # Increase sink value from terminal link, because coupling link gives energy
                if ('q' in node.bc_type) and (node.half_links[0].q > 0):
                    node_g = node
                    P_c = GHV*node.half_links[0].q / eta
                    coupling_link_g = GasLink(name='{}_{}'.format(c.name, node.name), 
                                              start_node=c, end_node=node, 
                                              bc_type=['q'], q=node.half_links[0].q, link_type='dummy',
                                              scale_var=scale_var, scale_var_params=node.scale_var_params)
                    network_g.add_link(coupling_link_g)
                    node.half_links[0].q += node.half_links[0].q
                    break
        
        if same_electrical_node: # Connect coupling unit to same electrical node as first coupling unit
            node_e = network_e.nodes[0]
            coupling_link_e = ElectricalLink(name='{}_{}'.format(node_e.name, c.name), 
                                             start_node=node_e, end_node=c, 
                                             bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                             scale_var=scale_var, scale_var_params=node_e.scale_var_params)
            network_e.add_link(coupling_link_e)
            if adjust_power:
                node_e.half_links[0].P -= P_c # Make sure equivalent amount of energy is added.
        else:
            no_suitable_node_e = True
            for node in network_e.nodes:
                if ('P' in node.bc_type) and (node.half_links[0].P > 0): # Adjust sink
                    node_e = node
                    coupling_link_e = ElectricalLink(name='{}_{}'.format(node.name, c.name), 
                                                     start_node=node, end_node=c, 
                                                     bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                     scale_var=scale_var, scale_var_params=node.scale_var_params)
                    network_e.add_link(coupling_link_e)
                    if adjust_power:
                        node.half_links[0].P -= P_c # Make sure equivalent amount of energy is added.
                    no_suitable_node_e = False
                    break
            
            if no_suitable_node_e:
                print("No sink node for electrical network found. Using source instead.")
                for node in network_e.nodes:
                    if ('P' in node.bc_type) and (node.half_links[0].P < 0): # Adjust source
                        node_e = node
                        coupling_link_e = ElectricalLink(name='{}_{}'.format(node.name, c.name), 
                                                         start_node=node, end_node=c, 
                                                         bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                         scale_var=scale_var, scale_var_params=node.scale_var_params)
                        network_e.add_link(coupling_link_e)
                        if adjust_power:
                            node.half_links[0].P -= P_c # Make sure equivalent amount of energy is added.
                        break
        
        scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                            'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
        c.scale_var_params = scale_var_params
    else:
        unit_type = 'gas_fired_generator'
        
        c = HeterogeneousNode(name='c1', 
                              bc_type=[], unit_type=unit_type, unit_params=unit_params,
                              scale_var=scale_var, scale_var_params=None)
        network_c.add_node(c)
        
        no_suitable_node_g = True  
        for node in network_g.nodes:
            if ('q' in node.bc_type) and (node.half_links[0].q > 0): # Replacing sink with coupling link
                node_g = node
                P_c = GHV*node.half_links[0].q * eta
                coupling_link_g = GasLink(name='{}_{}'.format(node.name, c.name), 
                                          start_node=node, end_node=c,
                                          bc_type=['q'], q=node.half_links[0].q, link_type='dummy',
                                          scale_var=scale_var, scale_var_params=node.scale_var_params)
                network_g.add_link(coupling_link_g)
                node.half_links[0].q = 0
                no_suitable_node_g = False
                break
        
        if no_suitable_node_g:
            print("No sink node for gas network found. Using source instead.")
            for node in network_g.nodes:
                if ('q' in node.bc_type) and (node.half_links[0].q < 0): # Replacing source with coupling link
                    node_g = node
                    P_c = -GHV*node.half_links[0].q * eta
                    coupling_link_g = GasLink(name='{}_{}'.format(node.name, c.name),
                                              start_node=node, end_node=c,
                                              bc_type=['q'], q=-node.half_links[0].q, link_type='dummy',
                                              scale_var=scale_var, scale_var_params=node.scale_var_params)
                    network_g.add_link(coupling_link_g)
                    node.half_links[0].q += node.half_links[0].q
                    break
        
        if same_electrical_node: # Connect coupling unit to same electrical node as first coupling unit
            node_e = network_e.nodes[0]
            coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node_e.name), 
                                             start_node=c, end_node=node_e, 
                                             bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                             scale_var=scale_var, scale_var_params=node_e.scale_var_params)
            network_e.add_link(coupling_link_e)
            if adjust_power:
                node_e.half_links[0].P += P_c
        else:
            no_suitable_node_e = True
            for node in network_e.nodes:
                if ('P' in node.bc_type) and (node.half_links[0].P < 0): # Adjust source
                    node_e = node
                    coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node.name), 
                                                     start_node=c, end_node=node,
                                                     bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                     scale_var=scale_var, scale_var_params=node.scale_var_params)
                    network_e.add_link(coupling_link_e)
                    if adjust_power:
                        node.half_links[0].P += P_c
                    no_suitable_node_e = False
                    break
            
            if no_suitable_node_e:
                print("No source node for electrical network found. Using sink instead.")
                for node in network_e.nodes:
                    if ('P' in node.bc_type) and (node.half_links[0].P > 0): # Adjust sink
                        node_e = node
                        coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node.name), 
                                                         start_node=c, end_node=node,
                                                         bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                         scale_var=scale_var, scale_var_params=node.scale_var_params)
                        network_e.add_link(coupling_link_e)
                        if adjust_power:
                            node.half_links[0].P += P_c
                        break
        
        scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                            'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
        c.scale_var_params = scale_var_params
        
    network_c.add_network(network_g)
    network_c.add_network(network_e)
        
    network_c.initialize()
    
    return network_e, network_g, network_c
    
        
def create_x_init(network_e=None, network_g=None, network_c=None):
    q_init = 0.1 * np.ones(len(network_g.links)-2)
    p_init = np.linspace(0.95, 0.9, network_g.number_of_unknown_p)

    delta_init = np.zeros(len(network_e.unknown_delta_nodes)) # flat start 0
    V_init = np.ones(len(network_e.unknown_V_nodes)) # flat start 1
    
    q_c_init = [0]
    P_c_init = [0, 0]
    
    x_init = np.concatenate([q_init, p_init, 
                             delta_init, V_init, 
                             q_c_init, P_c_init])
    
    return x_init
        
# %% Main

p2g = False # Unit type of second coupling unit
adjust_power = False # Adjust boundary condition for additional load
same_electrical_node = False # Connect both coupling units to same electrical node

if p2g:
    unit_type = 'p2g'
else:
    unit_type = 'gfg'
    
if adjust_power:
    test = '_adjust_power'
elif same_electrical_node:
    test = '_same_electrical_node'
else:
    test = ''
directory = "results_2_coupling_{}{}".format(unit_type, test)

os.makedirs(name=os.path.join(os.path.abspath('.'), "code", "coupling", directory, "solution"), exist_ok=True)
os.makedirs(name=os.path.join(os.path.abspath('.'), "code", "coupling", directory, "residuals"), exist_ok=True)

network_names_g = [
                   'GasLib-11',
                   'GasLib-24',
                   'GasLib-40',
                   'GasLib-135',
                   'GasLib-582',
                   'GasLib-4197'
                  ]

network_names_e = [
                   'case4gs',
                   'case5',
                   'case6ww',
                   'case9',
                   'case14',
                   'case24_ieee_rts',
                   'GBreducednetwork',
                   'case30',
                   'case_ieee30',
                   'case33bw',
                   'case39',
                   'case57',
                   'case89pegase',
                   'case118',
                   'case145',
                   'iceland',
                   'case_illinois200',
                   'case300',
                   'case1354pegase',
                   'case1888rte',
                   'GBnetwork',
                   'case2848rte',
                   'case2869pegase',
                   'case3120sp',
                   'case6470rte',
                   'case6495rte',
                   'case6515rte',
                   'case9241pegase'
                   ]

network_names_e = network_names_e[:]
network_names_g = network_names_g[:] # If range of test network changes, then header also changes

flow = 'average' # 'min' # 'max'
pressure = 'max' # 'min' # 'average'
gas_type = 'hydrogen' # 'natural'
                    
link_settings = {'friction' : 'friction_weymouth', # 'friction_pole'
                 'link_type' : 'pipe_high', # 'pipe_low'
                 'link_equation_formulation' : 'dp_of_q'} # 'q_of_dp'

resistor = False # True
scale_var = 'per_unit' # None

solver = 'nr'
solver_parameters = {'m' : 3, # Anderson acceleration
                     'max_iterations' : 20,
                     'optimal_multiplier' : False,
                     'residual_q' : False,
                     'tol' : 1e-6}

lin_solver = 'lu'
lin_solver_parameters = {'diag_pivot_thresh' : 0.1,
                         'drop_tol' : 1e-4,
                         'drop_rule' : ['basic', 'area'],
                         'fill_factor': 5,
                         'max_iterations': 100,
                         'reorderfornonzerodiagonal' : True, # also affects ordering for petsc
                         'options' : {'Equil' : True},
                         'permc_spec': 'colamd',
                         'preconditioner': 'ilu',
                         'preconditioners_for_blocks': [],
                         'preconditioners_for_two_level': [],
                         'rcm' : False,
                         'shift_value': 0.1,
                         'tol' : 1e-6,
                         'gmres_restart' : 100,
                         'petsc_fill-in' : 0,
                         'petsc_gamglevels': None, # None is default
                         'petsc_gamgsmooths' : None, # None is default
                         'petsc_gamgtype' : 'agg', # 'agg' # 'classical'
                         'petsc_gmres_restart' : 100,
                         'petsc_lin_solver' : 'gmres',
                         'petsc_max_iterations': 100,
                         'petsc_nzdiag' : 1e-6,
                         'petsc_ord_type' : 'qmd', # 'natural' # 'nd' # 'qmd' # 'rcm' # 'rowlength' # 'spectral' # 'wbm' # '1wd'
                         'petsc_preconditioner' : 'ilu', # 'gamg' # 'ilu' # 'jacobi' # 'kaczmarz' # 'lu' # 'sor'
                         'petsc_reorderfornonzerodiagonal' : False,
                         'petsc_reuse' : False,
                         'petsc_shift_amount' : None, # use None to turn off
                         'petsc_shift_type' : 'inblocks', # 'positive_definite' # None # 'nonzero'
                         'petsc_zero_diagonal' : False # define the zeros on diagonal explicitly
                        }

converged_message = ""
difference_message = ""
difference_e_message = ""
difference_g_message = ""
iterations_message = ""

for network_name_e in network_names_e:    
    converged_message += "\\textbf{{{}}} & ".format(network_name_e)
    difference_message += "\\textbf{{{}}} & ".format(network_name_e)
    difference_e_message += "\\textbf{{{}}} & ".format(network_name_e)
    difference_g_message += "\\textbf{{{}}} & ".format(network_name_e)
    iterations_message += "\\textbf{{{}}} & ".format(network_name_e)
    
    for network_name_g in network_names_g:
        print(50*"-" + "\n" + network_name_e + " + " + network_name_g + "\n" + 50*"-")
        
        network_e, network_g, network = create_network(network_name_e=network_name_e,
                                                       network_name_g=network_name_g,
                                                       p2g=p2g,
                                                       adjust_power=adjust_power,
                                                       same_electrical_node=same_electrical_node)
        x_init = create_x_init(network_e=network_e,
                               network_g=network_g)
                                        
        x_sol, iterations, errors, \
        p_g, q, q_inj, \
        delta, V, S_inj, P_link, Q_link, \
        m, p_h, Ts, Tr, m_hl, phi_hl, Ts_hl, Tr_hl, \
        q_c, P_c, Q_c, m_c, dphi_c, Ts_c, Tr_c = network.solve_network(x_init=x_init,
                                                                       solver=solver,
                                                                       solver_parameters=solver_parameters,
                                                                       lin_solver=lin_solver,
                                                                       lin_solver_parameters=lin_solver_parameters,
                                                                       post_processing=True)
    
        x_g = np.loadtxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results", "solution", "{}.txt".format(network_name_g)))
        difference_g = np.linalg.norm(x_g - x_sol[:len(network.x_g_entries)], ord=np.inf)
        print("Max-norm difference (g) = {}".format(difference_g))
        
        x_e = np.loadtxt(os.path.join(os.path.abspath('.'), "code", "pandapower", "results", "solution", "{}.txt".format(network_name_e)))
        difference_e = np.linalg.norm(x_e - x_sol[len(network.x_g_entries):len(network.x_g_entries)+len(network.x_e_entries)], ord=np.inf)
        print("Max-norm difference (e) = {}".format(difference_e))
       
        if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
            print("Average F time in seconds = {:.4e}".format(np.average(network.solver.F_times)))
            print("Average J time in seconds = {:.4e}".format(np.average(network.solver.J_times)))
            print("Average linear solve time in seconds = {:.4e}".format(np.average(network.solver.linear_solve_times)))
        print("Average non-linear solve time in seconds = {:.4e}".format(np.average(network.solver.nonlinear_solve_times)))
        print("Total time in seconds = {:.4e}".format(network.solver.total_time))
        
        print("Iterations = {:d}".format(iterations))
        print("Final error = {:.3e}".format(errors[-1]))
        
        converged_message += "{} & ".format(errors[-1] < solver_parameters['tol'])
        difference_message += "{:6.3e} & ".format(max(difference_e, difference_g))
        difference_e_message += "{:6.3e} & ".format(difference_e)
        difference_g_message += "{:6.3e} & ".format(difference_g)
        iterations_message += "{} & ".format(iterations)
        
        np.savetxt(os.path.join(os.path.abspath('.'), "code", "coupling", directory, "solution", "{}_{}.txt".format(network_name_e, network_name_g)), x_sol)
        np.savetxt(os.path.join(os.path.abspath('.'), "code", "coupling", directory, "residuals", "{}_{}.txt".format(network_name_e, network_name_g)), errors)
        
    converged_message = converged_message[:-2]    
    converged_message += "\\\\ \n"
    difference_message = difference_message[:-2]    
    difference_message += "\\\\ \n"
    difference_e_message = difference_e_message[:-2]    
    difference_e_message += "\\\\ \n"
    difference_g_message = difference_g_message[:-2]
    difference_g_message += "\\\\ \n"
    iterations_message = iterations_message[:-2]
    iterations_message += "\\\\ \n"
          
header = ""
for network_name_g in network_names_g:
    header += "\\textbf{{{}}} & ".format(network_name_g)
header = header[:-2] + "\\\\ \\hline \n"

def save_table(filename=None, directory=None, header=None, body=None):
    with open(os.path.join(os.path.abspath('.'), "code", "coupling", directory, "{}.txt".format(filename)), 'w') as text_file:
        print(header+body, file=text_file)
    
save_table(filename="converged", directory=directory, header=header, body=converged_message)
save_table(filename="difference", directory=directory, header=header, body=difference_message)
save_table(filename="difference_e", directory=directory, header=header, body=difference_e_message)
save_table(filename="difference_g", directory=directory, header=header, body=difference_g_message)
save_table(filename="iterations", directory=directory, header=header, body=iterations_message)