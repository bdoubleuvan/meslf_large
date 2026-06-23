import numpy as np
import os
import re
import sys
sys.path.append(os.path.join(os.path.abspath('.')))

from meslf.networks.pandapower_network import *
from meslf.networks.gaslib_network import *
from meslf.networks.heterogeneous_network import *

# %% Essential functions

def save_table(filename=None, directory=None, header=None, body=None):
    with open(os.path.join(directory, "{}.txt".format(filename)), 'w') as text_file:
        print(header+body, file=text_file)


def create_network(network_name_e=None, network_name_g=None, scale_var='per_unit',
                   P_max=10**100, p2g_units=1, gfg_units=1, bounded=False,
                   manufactured=False, slack_position_g=0,
                   number_of_clones_g=1, number_of_merges_g=0,
                   number_of_clones_e=1, number_of_merges_e=0,
                   number_of_clones_c=1):    
    # initialise gas network          
    link_settings = {'friction' : 'friction_weymouth', # 'friction_pole'
                     'link_type' : 'pipe_high', # 'pipe_low'
                     'link_equation_formulation' : 'dp_of_q'} # 'q_of_dp'

    gaslib_network = GasLibNetwork(network_name=network_name_g)
    network_g, node_data_g, link_data_g, \
    save_node, save_merge_q_node_even, save_merge_q_node_odd = gaslib_network.create_network(flow='average',
                                                                                             pressure='max',
                                                                                             gas_type='hydrogen',
                                                                                             link_settings=link_settings,
                                                                                             resistor=False,
                                                                                             scale_var=scale_var,
                                                                                             slack_position=slack_position_g,
                                                                                             number_of_clones=number_of_clones_g,
                                                                                             number_of_merges=number_of_merges_g)
    
    node_data_g = None
    link_data_g = None
    
    # initialise electrical network
    pandapower_network = PandapowerNetwork(network_name=network_name_e)
    network_e, data_e = pandapower_network.create_network(ignore_nodes=[],
                                                          formulation='complex_power',
                                                          scale_var=scale_var,
                                                          change_first_slack=False,
                                                          number_of_clones=number_of_clones_e,
                                                          number_of_merges=number_of_merges_e)
    
    data_e = None
    
    # get solution of stand-alone single-carrier networks
    if manufactured:
        path = os.path.join(os.path.abspath('.'), 
                            'results_direct_solver', 
                            'results_p2g_gfg_slack_1_adjust_power',
                            'results_p2g_{}_gfg_{}_slack_1_adjust_power'.format(p2g_units, gfg_units),
                            'solution',
                            '{}_{}.txt'.format(network_name_e, network_name_g))
        x_manufactured = np.loadtxt(path, dtype=np.float64)
        
        node_unknown_p = []
        link_unknown_q = []
        dummy_link_unknown_q = []
        for node in network_g.nodes:
            if 'p' not in node.bc_type:
                node_unknown_p.append(node)
        
        for link in network_g.links:
            if 'q' not in link.bc_type:
                if link.link_type == 'dummy':
                    if (link.start_node in link.nodes) and (link.end_node in link.nodes):
                        dummy_link_unknown_q.append(link)
                else:
                    link_unknown_q.append(link)
        
        unknown_delta_nodes = []
        unknown_V_nodes = []       
        for node in network_e.nodes:
            if 'V' not in node.bc_type:
                unknown_V_nodes.append(node)
            if 'delta' not in node.bc_type:
                unknown_delta_nodes.append(node)
    
    # collect source and sinks from single-carrier networks
    node_index = [node for node in network_g.nodes if 'p' not in node.bc_type]
    node_index = dict([(node, i) for i, node in enumerate(node_index)])
    gfg_units_index = []
    
    source_node_g = {}
    sink_node_g = {}
    source_node_e = {}
    sink_node_e = {}
    
    name_source_node_g = set()
    name_sink_node_g = set()
    name_source_node_e = set()
    name_sink_node_e = set()
                
    # Check if there are enough copies to copy coupling units
    if number_of_clones_c > min(number_of_clones_e, number_of_clones_g):
        print("number_of_clones_c changed from {} to {}".format(number_of_clones_c, min(number_of_clones_e, number_of_clones_g)))
        number_of_clones_c = min(number_of_clones_e, number_of_clones_g)
    
    # Electrical nodes for coupling
    start = 0
    for node in network_e.nodes[start:]:
        if (node.name in name_source_node_e) or (node.name in name_sink_node_e):
            break
        
        if ('P' in node.bc_type) and ('Q' in node.bc_type) and (len(node.half_links) > 0):
            no_shunt = True
            for link in node.half_links:
                if 'shunt' in link.name:
                    no_shunt = False
                                
            if no_shunt:
                if (node.half_links[0].P < 0) and (len(source_node_e.keys()) < gfg_units):
                    source_node_e[node] = None
                    name_source_node_e.add(node.name)
                elif (node.half_links[0].P > 0) and (len(sink_node_e.keys()) < p2g_units):
                    sink_node_e[node] = None
                    name_sink_node_e.add(node.name)
        start += 1
                            
    # check if there are eneough source or sink nodes from single-carrier network to couple with
    if (p2g_units > 0) and (len(sink_node_e.keys()) < p2g_units):
        print("Not enough electrical sink nodes for {} p2g units".format(p2g_units))
        return None, None, None, None, None, None, None
    
    if (gfg_units > 0) and (len(source_node_e.keys()) < gfg_units):
        print("Not enough electrical source nodes for {} gfg units".format(gfg_units))
        return None, None, None, None, None, None, None
    
    for node in network_e.nodes[start:]:
        if ('P' in node.bc_type) and ('Q' in node.bc_type) and (len(node.half_links) > 0):
            no_shunt = True
            for link in node.half_links:
                if 'shunt' in link.name:
                    no_shunt = False
            
            if no_shunt:
                if (node.half_links[0].P < 0) and (len(source_node_e.keys()) < number_of_clones_c*gfg_units) and (node.name in name_source_node_e):
                    source_node_e[node] = None
                elif (node.half_links[0].P > 0) and (len(sink_node_e.keys()) < number_of_clones_c*p2g_units) and (node.name in name_sink_node_e):
                    sink_node_e[node] = None
                    
        if (len(source_node_e) >= number_of_clones_c*gfg_units) and (len(sink_node_e) >= number_of_clones_c*p2g_units):
            break

    # Gas nodes for coupling
    start = 0                         
    for node in network_g.nodes[start:]:
        if (node.name.split()[0] in name_source_node_g) or (node.name.split()[0] in name_sink_node_g):
            break
        
        if ('q' in node.bc_type) and (len(node.half_links) > 0):
            if (node.half_links[0].q < 0) and (len(source_node_g.keys()) < p2g_units):
                source_node_g[node] = None
                name_source_node_g.add(node.name.split()[0])
            elif (node.half_links[0].q > 0) and (len(sink_node_g.keys()) < gfg_units):
                sink_node_g[node] = None
                name_sink_node_g.add(node.name.split()[0])
        start += 1
                                        
    # check if there are eneough source or sink nodes from single-carrier network to couple with
    if (p2g_units > 0) and (len(source_node_g.keys()) < p2g_units):
        print("Not enough gas source nodes for {} p2g units".format(p2g_units))
        return None, None, None, None, None, None, None
    
    if (gfg_units > 0) and (len(sink_node_g.keys()) < gfg_units):
        print("Not enough gas sink nodes for {} gfg units".format(gfg_units))
        return None, None, None, None, None, None, None

    for node in network_g.nodes[start:]:
        if ('q' in node.bc_type) and (len(node.half_links) > 0):
            if (node.half_links[0].q < 0) and (len(source_node_g.keys()) < number_of_clones_c*p2g_units) and (node.name.split()[0] in name_source_node_g):
                source_node_g[node] = None
            elif (node.half_links[0].q > 0) and (len(sink_node_g.keys()) < number_of_clones_c*gfg_units) and (node.name.split()[0] in name_sink_node_g):
                sink_node_g[node] = None
                
        if (len(source_node_g.keys()) >= number_of_clones_c*p2g_units) and (len(sink_node_g.keys()) >= number_of_clones_c*gfg_units):
            break
                    
    # define coupling unit data for P2G and GFG
    eta = 0.8
    GHV = 1.418*10**8
    unit_params = {'eta': eta,
                   'GHV': GHV,
                   'P_max' : P_max}
    
    slack_data = np.genfromtxt(os.path.join(os.path.abspath('.'), "pandapower", "slack_value.txt"), dtype=['<U20', float, float])
    slack_active_power = {}
    for data in slack_data:
        slack_active_power[data[0]] = data[1] 
    slack_data = None
        
    if slack_active_power[network_name_e] >=0:
        unit_type = 'p2g'
    else:
        unit_type = 'gas_fired_generator'
            
    if unit_type == 'p2g':
        unit_params['q_max'] = eta * P_max / GHV
    elif unit_type == 'gas_fired_generator':
        unit_params['q_max'] = P_max / (eta * GHV)
        
    # initialise network
    network_c = HeterogeneousNetwork("Coupled network with {} P2G and {} GFG units".format(p2g_units, gfg_units))
    
    # combine slack with coupling unit
    # scale_var_params = {'Ebase' : network_e.nodes[0].scale_var_params['Sbase'],
    #                     'GHVbase' : network_e.nodes[0].scale_var_params['Sbase'] / network_g.nodes[0].scale_var_params['qbase']}
    
    # c = HeterogeneousNode('{}_slack'.format(unit_type), bc_type=[], unit_type=unit_type, unit_params=unit_params,
    #                       scale_var=scale_var, scale_var_params=scale_var_params, bounded=bounded)
    # network_c.add_node(c)
    
    # if unit_type == 'p2g':
    #     coupling_link_g = GasLink(name='{}_{}'.format(c.name, network_g.nodes[0].name),
    #                               start_node=c, end_node=network_g.nodes[0], 
    #                               link_type='dummy', q_max=unit_params['q_max'],
    #                               scale_var=scale_var, scale_var_params=network_g.nodes[0].scale_var_params)
        
    #     coupling_link_e = ElectricalLink(name='{}_{}'.format(network_e.nodes[0].name, c.name), 
    #                                      start_node=network_e.nodes[0], end_node=c, 
    #                                      bc_type=['Q_start'], Q_start=0, link_type='dummy', 
    #                                      P_max=P_max,
    #                                      scale_var=scale_var, scale_var_params=network_e.nodes[0].scale_var_params)
    # else:
    #     coupling_link_g = GasLink(name='{}_{}'.format(network_g.nodes[0].name, c.name),
    #                               start_node=network_g.nodes[0], end_node=c, 
    #                               link_type='dummy', q_max=unit_params['q_max'],
    #                               scale_var=scale_var, scale_var_params=network_g.nodes[0].scale_var_params)
        
    #     coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, network_e.nodes[0].name), 
    #                                      start_node=c, end_node=network_e.nodes[0], 
    #                                      bc_type=['Q_start'], Q_start=0, link_type='dummy', 
    #                                      P_max=P_max,
    #                                      scale_var=scale_var, scale_var_params=network_e.nodes[0].scale_var_params)
    
    # network_g.add_link(coupling_link_g) 
    # network_e.add_link(coupling_link_e)
        
    # couple P2G units
    unit_type = 'p2g'
    unit_params['q_max'] = eta * P_max / GHV
    for i, (node_e, node_g) in enumerate(zip(sink_node_e.keys(), source_node_g.keys())):
        c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
                              bc_type=[], unit_type=unit_type, unit_params=unit_params,
                              scale_var=scale_var, scale_var_params=None, bounded=bounded)
        network_c.add_node(c)

        coupling_link_g = GasLink(name='{}_{}'.format(c.name, node_g.name),
                                  start_node=c, end_node=node_g, 
                                  bc_type=[], link_type='dummy',
                                  q_max=unit_params['q_max'],
                                  scale_var=scale_var, scale_var_params=node_g.scale_var_params)
        network_g.add_link(coupling_link_g)
            
        # node_g.bc_type.append('p')
        # if manufactured:
        #     index = len(link_unknown_q) + \
        #             len(dummy_link_unknown_q) + \
        #             node_unknown_p.index(node_g)
        #     node_g.p = x_manufactured[index] * node_g.scale_var_params['pbase']
        #     print("{} p = {}".format(node_g.name, node_g.p))
        # else:
        #     node_g.p = node_g.scale_var_params['pbase']
                                   
        coupling_link_e = ElectricalLink(name='{}_{}'.format(node_e.name, c.name), 
                                         start_node=node_e, end_node=c, 
                                         bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                         P_max=P_max,
                                         scale_var=scale_var, scale_var_params=node_e.scale_var_params)
        network_e.add_link(coupling_link_e)
        
        node_e.bc_type.append('V')
        if manufactured:
            index = len(link_unknown_q) + \
                    len(dummy_link_unknown_q) + \
                    len(node_unknown_p) + \
                    len(unknown_delta_nodes) + \
                    unknown_V_nodes.index(node_e)
            node_e.V = x_manufactured[index] * node_e.scale_var_params['Vbase']
            print("{} V = {}".format(node_e.name, node_e.V))
        else:
            node_e.V = node_e.scale_var_params['Vbase']
        
        # node_e.half_links[0].P += (GHV * node_g.half_links[0].q) / eta
        # node_g.half_links[0].q = 0
                                
        scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                            'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
        c.scale_var_params = scale_var_params
    
    # couple GFG units
    unit_type = 'gas_fired_generator'
    unit_params['q_max'] = P_max / (eta * GHV)
    for i, (node_e, node_g) in enumerate(zip(source_node_e.keys(), sink_node_g.keys())):
        # if '{}_{}'.format(unit_type, i) == 'gas_fired_generator_2':
        #     print('{}_{}'.format(unit_type, i))
        #     eta_ = 1 / eta
        # else:
        #     eta_ = eta
        c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
                              bc_type=[], unit_type=unit_type, unit_params=unit_params,
                              scale_var=scale_var, scale_var_params=None, bounded=bounded)
        network_c.add_node(c)
        coupling_link_g = GasLink(name='{}_{}'.format(node_g.name, c.name),
                                  start_node=node_g, end_node=c, 
                                  bc_type=[], link_type='dummy',
                                  q_max=unit_params['q_max'],
                                  scale_var=scale_var, scale_var_params=node_g.scale_var_params)
        network_g.add_link(coupling_link_g)
        
        node_g.bc_type.append('p')
        if manufactured:
            index = len(link_unknown_q) + \
                    len(dummy_link_unknown_q) + \
                    node_unknown_p.index(node_g)
            node_g.p = x_manufactured[index] * node_g.scale_var_params['pbase']
            print("{} p = {}".format(node_g.name, node_g.p))
        else:
            node_g.p = node_g.scale_var_params['pbase']
            
        gfg_units_index.append(node_index[node_g])
        
        coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node_e.name), 
                                         start_node=c, end_node=node_e, 
                                         bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                         P_max=P_max,
                                         scale_var=scale_var, scale_var_params=node_e.scale_var_params)
        network_e.add_link(coupling_link_e)
        
        # node_e.half_links[0].P += eta * GHV * node_g.half_links[0].q
        # node_g.half_links[0].q = 0
        
        # node_e.bc_type.append('V')
        # if manufactured:
        #     index = len(link_unknown_q) + \
        #             len(dummy_link_unknown_q) + \
        #             len(node_unknown_p) + \
        #             len(unknown_delta_nodes) + \
        #             unknown_V_nodes.index(node_e)
        #     node_e.V = x_manufactured[index] * node_e.scale_var_params['Vbase']
        #     print("{} V = {}".format(node_e.name, node_e.V))
        # else:
        #     node_e.V = node_e.scale_var_params['Vbase']
                                
        scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                            'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
        c.scale_var_params = scale_var_params
                      
    network_c.add_network(network_g)
    network_c.add_network(network_e)
        
    network_c.initialize()
                    
    return network_e, network_g, network_c, save_node, save_merge_q_node_even, save_merge_q_node_odd, gfg_units_index
    
        
def create_x_init(network_e=None, network_g=None,
                  number_of_clones_g=None, gfg_units_index=None,
                  save_node=None, save_merge_q_node_even=None, save_merge_q_node_odd=None):
    q_init = 0.1 * np.ones(len(network_g.link_unknown_q))
          
    if number_of_clones_g == 1:
        p_init = np.linspace(0.95, 0.9, len(network_g.nodes)-1)[~np.isin(range(len(network_g.nodes)-1), gfg_units_index)]
    else:
        p_original = np.linspace(0.95, 0.9, len(save_node.keys()))
        p_init_even = p_original[~np.isin(range(len(p_original)), list(save_merge_q_node_odd.values()))]
        p_init_odd = p_original[~np.isin(range(len(p_original)), list(save_merge_q_node_even.values()))]
        p_init = np.linspace(0.95, 0.9, len(save_node.keys()))
        for i in range(1, number_of_clones_g):
            if (i % 2) == 0:
                p_init = np.concatenate([p_init, p_init_even])
            else:
                p_init = np.concatenate([p_init, p_init_odd])
        p_init = p_init[~np.isin(range(p_init.shape[0]), gfg_units_index)]
            
    delta_init = np.zeros(len(network_e.unknown_delta_nodes)) # flat start 0
    V_init = np.ones(len(network_e.unknown_V_nodes)) # flat start 1
    
    P_c_init = np.zeros(len(list(network_e.get_links(link_types=['dummy'], exclude_bc_types=[['P_start'], ['P_start', 'Q_start'], ['P_start', 'P_end', 'Q_start']]))))
    q_c_init = np.zeros(len(list(network_g.get_links(link_types=['dummy'], exclude_bc_types=[['q']]))))
    # for i, link in enumerate(network_g.get_links(link_types=['dummy'], exclude_bc_types=[['q']])):
    #     if isinstance(link.start_node, HeterogeneousNode):
    #         q_c_init[i] = link.start_node.unit_params['eta'] * link.start_node.scale_var_params['Ebase'] * P_c_init[i] / link.start_node.unit_params['GHV']
    #         q_c_init[i] /= link.scale_var_params['qbase']
    #     elif isinstance(link.end_node, HeterogeneousNode):
    #         q_c_init[i] = link.end_node.scale_var_params['Ebase'] * P_c_init[i] / (link.end_node.unit_params['eta'] * link.end_node.unit_params['GHV'])
    #         q_c_init[i] /= link.scale_var_params['qbase']
    
    x_init = np.concatenate([q_init, p_init, 
                             delta_init, V_init, 
                             q_c_init, P_c_init])
    
    # x_g = np.loadtxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results", "solution", "{}.txt".format(network_name_g)))
    # x_e = np.loadtxt(os.path.join(os.path.abspath('.'), "code", "pandapower", "results", "solution", "{}.txt".format(network_name_e)))
    # x_init[:x_g.shape[0]] = x_g
    # x_init[x_g.shape[0]:x_g.shape[0]+x_e.shape[0]] = x_e
        
    return x_init

def save_variables(network, variables, elements_type='node', filename=None):
    if elements_type == 'node':
        names = [node.name for node in network.nodes]
    elif elements_type == 'link':
        names = [link.name for link in network.links]
    elif elements_type == 'half_link':
        names = [hl.name for node in network.nodes for hl in node.half_links]
    
    variables_save = [(name, value) for name, value in zip(names, variables)]
    variables_save = np.array(variables_save, dtype=[('keys', '<U33'), ('data', '<f8')])
    
    np.savetxt(os.path.join(directory, filename), variables_save, fmt='%s %.16f')
    
    return None

# %% Network names

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

network_names_e = network_names_e[-1:]
network_names_g = network_names_g[-1:] # If range of test network changes, then header also changes

# %% Gas slack data for testing best slack position
# slack_data_g = np.loadtxt('./gaslib/results_slack/1/GasLib-4197/overview.txt')
slack_positions_g = [11] # slack_data_g[slack_data_g[:, 1] > 0, 0][:5]

# %% Solver settings

solver = 'nr'
solver_parameters = {'m' : 3, # Anderson acceleration
                     'max_iterations' : 50,
                     'optimal_multiplier' : False,
                     'residual_q' : False,
                     'tol' : 1e-6}

lin_solver = 'gmres'
lin_solver_parameters = {'block_size' : None,
                         'diag_pivot_thresh' : 1,
                         'drop_tol' : 1e-4,
                         'drop_rule' : ['basic', 'area'],
                         'fill_factor': None,
                         'fill_factor_11' : 5,
                         'fill_factor_22' : 4,
                         'get_condition_number' : False,
                         'get_initial' : False,
                         'gmres_restart' : 25,
                         'max_iterations' : 50,
                         'options' : {'Equil' : True},
                         'permc_spec': 'COLAMD',
                         'preconditioner': 'ilu',
                         'preconditioners_for_blocks': [],
                         'preconditioners_for_two_level': [],
                         'rcm' : False,
                         'reorderfornonzerodiagonal' : False, # also affects ordering for petsc
                         'residuals_directory' : None,
                         'shift_value': 0.1,
                         'tol' : 1e-6,
                         'petsc_fill-in' : 0,
                         'petsc_gamglevels': None, # None is default
                         'petsc_gamgsmooths' : None, # None is default
                         'petsc_gamgtype' : 'agg', # 'agg' # 'classical'
                         'petsc_gmres_restart' : 50,
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

post_processing = False

# %% Test options

slack_position_e = 0 # currently only used for naming folders, has no influence on other functions

# number_of_clones_e_list = [1, 2, 4, 8, 16, 32, 32, 32][-1:]
# number_of_merges_e_list = [0, 1, 2, 4, 8, 16, 32, 64][-1:]

# number_of_clones_g_list = [1, 2, 4, 8, 16, 32, 32, 32][-1:]
# number_of_merges_g_list = [0, 1, 2, 4, 4, 4, 4, 4][-1:]

number_of_clones_e_list = [1, 2, 4, 8, 16, 32, 64][4:-2]
number_of_merges_e_list = [0, 64, 64, 64, 64, 64, 64][4:-2]

number_of_clones_g_list = [1, 2, 4, 8, 16, 32, 64][4:-2]
number_of_merges_g_list = [0, 4, 4, 4, 4, 4, 4][4:-2]

number_of_clones_c_list = [1, 2, 4, 8, 16, 32, 32][2:-4]

p2g_units_max = 3
gfg_units_max = 4

manufactured = False

bounded = False
P_max = 10**10

lin_solver_parameters['preconditioner'] = 'ilu' # 'jacobi' # 'gauss'
lin_solver_parameters['fill_factor'] = 5

if lin_solver_parameters['preconditioner'] == 'ilu':
    preconditioner_tag = "{}({})".format(lin_solver_parameters['preconditioner'], lin_solver_parameters['fill_factor'])
else:
    preconditioner_tag = lin_solver_parameters['preconditioner']
    
save_residuals_krylov = True

results_directory = "results"

# %% Run simulations

summary_names = ['Unknowns',
                 'Iterations',
                 'Error',
                 'F time',
                 'J time',
                 'Linear time',
                 'Nonlinear time',
                 'Total time',
                 'Number of negative coupling units',
                 'All coupling units nonnegative',
                 'Number of negative pressures',
                 'All pressures nonnegative']

for number_of_clones_e, number_of_merges_e, number_of_clones_g, number_of_merges_g in zip(number_of_clones_e_list, number_of_merges_e_list, number_of_clones_g_list, number_of_merges_g_list):
    for number_of_clones_c in number_of_clones_c_list:
        if (number_of_clones_c <= number_of_clones_e) or (number_of_clones_c <= number_of_clones_g):
            for network_name_e in network_names_e:            
                for network_name_g in network_names_g:
                    for p2g_units in range(0, p2g_units_max+1):
                        for gfg_units in range(0, gfg_units_max+1):
                            if (p2g_units, gfg_units) in set([(0, 0), (3, 4)]):
                                for slack_position_g in slack_positions_g:                    
                                    if lin_solver in {'direct', 'lu'}:
                                        directory = os.path.join(os.path.abspath('.'), 
                                                                results_directory,
                                                                '{}_{}'.format(network_name_e, network_name_g),
                                                                'slack_position_e_{}_g_{}'.format(slack_position_e, slack_position_g),
                                                                'clones_e_{}_clones_g_{}_clones_c_{}_merges_e_{}_merges_g_{}'.format(number_of_clones_e, 
                                                                                                                                     number_of_clones_g,
                                                                                                                                     number_of_clones_c, 
                                                                                                                                     number_of_merges_e, 
                                                                                                                                     number_of_merges_g),
                                                                'p2g_{}_gfg_{}'.format(p2g_units, gfg_units),
                                                                lin_solver)
                                    else:
                                        directory = os.path.join(os.path.abspath('.'), 
                                                                results_directory,
                                                                '{}_{}'.format(network_name_e, network_name_g),
                                                                'slack_position_e_{}_g_{}'.format(slack_position_e, slack_position_g),
                                                                'clones_e_{}_clones_g_{}_clones_c_{}_merges_e_{}_merges_g_{}'.format(number_of_clones_e, 
                                                                                                                                     number_of_clones_g,
                                                                                                                                     number_of_clones_c, 
                                                                                                                                     number_of_merges_e, 
                                                                                                                                     number_of_merges_g),
                                                                'p2g_{}_gfg_{}'.format(p2g_units, gfg_units),
                                                                lin_solver,
                                                                preconditioner_tag)

                                    os.makedirs(directory, exist_ok=True)
                                    if save_residuals_krylov and (lin_solver != 'lu'):
                                        lin_solver_parameters['residuals_directory'] = os.path.join(directory, 'residuals_krylov')
                                        os.makedirs(name=lin_solver_parameters['residuals_directory'], exist_ok=True)

                                    print(50*"-" + "\n" + network_name_e + " + " + network_name_g + " (p2g={}, gfg={})".format(p2g_units, gfg_units) + "\n" + 50*"-")

                                    # initialise network
                                    network_e, network_g, network, \
                                    save_node, save_merge_q_node_even, save_merge_q_node_odd, \
                                    gfg_units_index = create_network(network_name_e=network_name_e, network_name_g=network_name_g, \
                                                                     number_of_clones_e=number_of_clones_e, number_of_clones_g=number_of_clones_g, \
                                                                     number_of_clones_c=number_of_clones_c, \
                                                                     number_of_merges_e=number_of_merges_e, number_of_merges_g=number_of_merges_g, \
                                                                     slack_position_g=slack_position_g, \
                                                                     P_max=P_max, p2g_units=p2g_units, gfg_units=gfg_units, bounded=bounded, \
                                                                     manufactured=manufactured)

                                    # if there are not enough source and sink nodes to couple stop simulation
                                    if network is None:
                                        print("Not enough sinks or sources for coupling units. Stopping simulating this specific case.")
                                        break

                                    # initial guess
                                    x_init = create_x_init(network_e=network_e, network_g=network_g,
                                                           number_of_clones_g=number_of_clones_g, gfg_units_index=gfg_units_index,
                                                           save_node=save_node, save_merge_q_node_even=save_merge_q_node_even, save_merge_q_node_odd=save_merge_q_node_odd)

                                    print()
                                    print("Number of unknowns = {} \n".format(x_init.shape[0]))

                                    # solve network
                                    x_sol, iterations, errors, \
                                    p_g, q, q_inj, \
                                    delta, V, S_inj, P_link, Q_link, \
                                    m, p_h, Ts, Tr, m_hl, phi_hl, Ts_hl, Tr_hl, \
                                    q_c, P_c, Q_c, m_c, dphi_c, Ts_c, Tr_c = network.solve_network(x_init=x_init,
                                                                                                   solver=solver,
                                                                                                   solver_parameters=solver_parameters,
                                                                                                   lin_solver=lin_solver,
                                                                                                   lin_solver_parameters=lin_solver_parameters,
                                                                                                   post_processing=post_processing,
                                                                                                   bounded=bounded)
                                    
                                    # create output
                                    try:
                                        F_time = np.average(network.solver.F_times)
                                    except:
                                        F_time = 0

                                    try:
                                        J_time = np.average(network.solver.J_times)
                                    except:
                                        J_time = 0

                                    try:
                                        l_time = np.average(network.solver.linear_solve_times)
                                    except:
                                        l_time = 0

                                    try:
                                        nl_time = np.average(network.solver.nonlinear_solve_times)
                                    except:
                                        nl_time = 0

                                    # print output
                                    print()
                                    if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
                                        print("Average F time in seconds = {:.3e}".format(F_time))
                                        print("Average J time in seconds = {:.3e}".format(J_time))
                                        print("Average linear solve time in seconds = {:.3e}".format(l_time))
                                    print("Average non-linear solve time in seconds = {:.3e}".format(nl_time))
                                    print("Total time in seconds = {:.3e}".format(network.solver.total_time))

                                    print("Iterations = {:d}".format(iterations))
                                    print("Final error = {:.3e}".format(errors[-1]))

                                    # check negative input or output from coupling
                                    number_of_negative_coupling_units = np.sum(P_c < 0)
                                    all_coupling_units_nonnegative = number_of_negative_coupling_units == 0

                                    print()
                                    print("Number of negative coupling units = {:d}".format(number_of_negative_coupling_units))
                                    print("All coupling units nonnegative = {}".format(all_coupling_units_nonnegative))
                                    
                                    # check negative pressure at gas network
                                    number_of_negative_pressures = np.sum(p_g < 0)
                                    all_pressures_nonnegative = number_of_negative_pressures == 0

                                    print()
                                    print("Number of negative pressures = {:d}".format(number_of_negative_pressures))
                                    print("All pressures nonnegative = {}".format(all_pressures_nonnegative))
                                    
                                    # summary
                                    summary_values = [x_sol.shape[0],
                                                      iterations,
                                                      errors[-1],
                                                      F_time,
                                                      J_time,
                                                      l_time,
                                                      nl_time,
                                                      network.solver.total_time,
                                                      number_of_negative_coupling_units,
                                                      all_coupling_units_nonnegative,
                                                      number_of_negative_pressures,
                                                      all_pressures_nonnegative]
                                    summary = [(name, value) for name, value in zip(summary_names, summary_values)]
                                    summary = np.array(summary, dtype=[('keys', '<U33'), ('data', '<f8')])

                                    # save output
                                    np.savetxt(os.path.join(directory, 'summary.txt'), summary, fmt='%s %.16f')
                                    np.savetxt(os.path.join(directory, 'residuals.txt'), errors, fmt='%.16f')
                                    np.savetxt(os.path.join(directory, 'solution.txt'), x_sol, fmt='%.16f')
                                                                                            
                                    # save_variables(network_g, p_g, elements_type='node', filename='p.txt')
                                    # save_variables(network_g, q, elements_type='link', filename='q.txt')
                                    # save_variables(network_g, q_inj, elements_type='half_link', filename='q_inj.txt')
                                    
                                    # save_variables(network_e, delta, elements_type='node', filename='delta.txt')
                                    # save_variables(network_e, V, elements_type='node', filename='V.txt')
                                    # save_variables(network_e, V, elements_type='node', filename='V.txt')
                                    # save_variables(network_e, P_link[:len(network_e.links)], elements_type='link', filename='P_start.txt')
                                    # save_variables(network_e, P_link[len(network_e.links):], elements_type='link', filename='P_end.txt')
                                    # save_variables(network_e, Q_link[:len(network_e.links)], elements_type='link', filename='Q_start.txt')
                                    # save_variables(network_e, Q_link[len(network_e.links):], elements_type='link', filename='Q_end.txt')                                
                                    # save_variables(network_e, S_inj.real, elements_type='half_link', filename='P_inj.txt')
                                    # save_variables(network_e, S_inj.imag, elements_type='half_link', filename='Q_inj.txt')
                                    
                                    # save_variables(network, P_c, elements_type='node', filename='P_c.txt')
                                    # save_variables(network, q_c, elements_type='node', filename='q_c.txt')
                                    
                                    if lin_solver_parameters['get_condition_number']:
                                        np.savetxt(os.path.join(directory, 'sv.txt'), np.array(network.sv).T, fmt='%.16f')
                                        
                                    if lin_solver_parameters['get_initial']:
                                        f_ratio = (network.lu_init.L.nnz + network.lu_init.U.nnz) / network.J_init.nnz
                                        data_lu = [network.J_init.nnz, network.lu_init.L.nnz, network.lu_init.U.nnz, f_ratio, network.lu_init.nnz]
                                        np.savetxt(os.path.join(directory, 'summary_lu.txt'), data_lu, fmt='%.16f')