import numpy as np
import os
import re
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'code'))

from meslf.networks.pandapower_network import *
from meslf.networks.gaslib_network import *
from meslf.networks.heterogeneous_network import *

# %% 

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

network_names_g = [
                   'GasLib-11',
                   'GasLib-24',
                   'GasLib-40',
                   'GasLib-135',
                   'GasLib-582',
                   'GasLib-4197'
                  ]
 
for network_name_e in network_names_e[:]:
    for network_name_g in network_names_g[:]:
        print(50*"-" + "\n" + network_name_e + " + " + network_name_g + "\n" + 50*"-")
        
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
        
        scale_var_params = {'Ebase' : network_e.nodes[0].scale_var_params['Sbase'],
                            'GHVbase' : network_e.nodes[0].scale_var_params['Sbase'] / network_g.nodes[0].scale_var_params['qbase']}

        eta = 1
        GHV = 1.418*10**8
        unit_params = {'eta': eta,
                    'GHV': GHV}
        unit_type = 'p2g'
            
        network_c = HeterogeneousNetwork('Test network for 1 coupling unit')
        c0 = HeterogeneousNode('c0', bc_type=[], unit_type=unit_type, unit_params=unit_params,
                               scale_var=scale_var, scale_var_params=scale_var_params)
        network_c.add_node(c0)
        
        c0g0 = GasLink(name='c0g0', start_node=c0, end_node=network_g.nodes[0], link_type='dummy', 
                       scale_var=scale_var, scale_var_params=network_g.nodes[0].scale_var_params)
        network_g.add_link(c0g0)
        
        e0c0 = ElectricalLink(name='e0c0', start_node=network_e.nodes[0], end_node=c0, bc_type=['Q_start'], Q_start=0, link_type='dummy', 
                              scale_var=scale_var, scale_var_params=network_e.nodes[0].scale_var_params)
        network_e.add_link(e0c0)
        
        network_c.add_network(network_g)
        network_c.add_network(network_e)
            
        network_c.initialize()

        q_init = 0.1 * np.ones(len(network_g.links)-1)

        # initial pressure deviates from 5% to 10% of the reference pressure

        p_init = np.linspace(0.95, 0.9, network_g.number_of_unknown_p)

        delta_init = np.zeros(len(network_e.unknown_delta_nodes)) # flat start 0
        V_init = np.ones(len(network_e.unknown_V_nodes)) # flat start 1
        x_init = np.concatenate([q_init, p_init, delta_init, V_init, [0], [0]])
        
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
                                 'fill_factor': 1,
                                 'max_iterations': 100,
                                 'reorderfornonzerodiagonal' : False, # also affects ordering for petsc
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
        
        x_sol, iterations, errors, \
        p_g, q, q_inj, \
        delta, V, S_inj, P_link, Q_link, \
        m, p_h, Ts, Tr, m_hl, phi_hl, Ts_hl, Tr_hl, \
        q_c, P_c, Q_c, m_c, dphi_c, Ts_c, Tr_c = network_c.solve_network(x_init=x_init,
                                                                         solver=solver,
                                                                         solver_parameters=solver_parameters,
                                                                         lin_solver=lin_solver,
                                                                         lin_solver_parameters=lin_solver_parameters,
                                                                         post_processing=True)

        if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
            print("Average F time in seconds = {:.4e}".format(np.average(network_c.solver.F_times)))
            print("Average J time in seconds = {:.4e}".format(np.average(network_c.solver.J_times)))
            print("Average linear solve time in seconds = {:.4e}".format(np.average(network_c.solver.linear_solve_times)))
        print("Average non-linear solve time in seconds = {:.4e}".format(np.average(network_c.solver.nonlinear_solve_times)))
        print("Total time in seconds = {:.4e}".format(network_c.solver.total_time))
        
        print("Iterations = {:d}".format(iterations))
        print("Final error = {:.3e}".format(errors[-1]))