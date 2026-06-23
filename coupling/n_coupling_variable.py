import numpy as np
import os
import re
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'code'))

from meslf.networks.pandapower_network import *
from meslf.networks.gaslib_network import *
from meslf.networks.heterogeneous_network import *

# %% Essential functions

def save_table(filename=None, directory=None, header=None, body=None):
    with open(os.path.join(directory, "{}.txt".format(filename)), 'w') as text_file:
        print(header+body, file=text_file)


def create_network(network_name_e=None, network_name_g=None, \
                   adjust_power=False, adjust_flow=False, \
                   same_electrical_node=False, same_gas_node=False, \
                   p2g_units=1, gfg_units=1, 
                   bounded=False, P_max=10**10, connect_with_non_slack_gas_node=False):
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
                                                                        scale_var=scale_var,
                                                                        slack_node=0,
                                                                        clone_network=1)
    
    
    formulation = 'complex_power'
    scale_var = 'per_unit'
    change_first_slack = True
    
    pandapower_network = PandapowerNetwork(network_name=network_name_e)
    network_e, data_e = pandapower_network.create_network(ignore_nodes=[],
                                                          formulation=formulation,
                                                          scale_var=scale_var,
                                                          change_first_slack=change_first_slack)
    
    
    source_node_g = []
    sink_node_g = []
    source_node_e = []
    sink_node_e = []
    
    for node in network_g.nodes:
        if ('q' in node.bc_type) and (len(node.half_links) > 0):
            if node.half_links[0].q < 0:
                source_node_g.append(node)
            elif node.half_links[0].q > 0:
                sink_node_g.append(node)
                
    for node in network_e.nodes:
        if ('P' in node.bc_type) and ('P' in node.bc_type) and (len(node.half_links) > 0):
            no_shunt = True
            for link in node.half_links:
                if 'shunt' in link.name:
                    no_shunt = False
            if no_shunt:
                if node.half_links[0].P < 0:
                    source_node_e.append(node)
                elif node.half_links[0].P > 0:
                    sink_node_e.append(node)   
    
    
    network_c = HeterogeneousNetwork("Coupled network with {} P2G and {} GFG units".format(p2g_units, gfg_units))
    
    slack_data = np.genfromtxt(os.path.join(os.path.abspath('.'), "code", "pandapower", "results", "slack_value.txt"), dtype=['<U20', float, float])
    slack_active_power = {}
    for data in slack_data:
        slack_active_power[data[0]] = data[1] 
    slack_data = None
    
    if slack_active_power[network_name_e] >=0:
        unit_type = 'p2g'
    else:
        unit_type = 'gas_fired_generator'
        
    eta = 0.8
    GHV = 1.418*10**8
    unit_params = {'eta': eta,
                   'GHV': GHV}
    unit_params['P_max'] = P_max
    if unit_type == 'p2g':
        unit_params['q_max'] = (eta * unit_params['P_max']) / GHV
    else:
        unit_params['q_max'] = unit_params['P_max'] / (eta * GHV)
            
    scale_var_params = {'Ebase' : network_e.nodes[0].scale_var_params['Sbase'],
                        'GHVbase' : network_e.nodes[0].scale_var_params['Sbase'] / network_g.nodes[0].scale_var_params['qbase']}
    
    c = HeterogeneousNode('{}_slack'.format(unit_type), bc_type=[], unit_type=unit_type, unit_params=unit_params,
                          scale_var=scale_var, scale_var_params=scale_var_params, bounded=bounded)
    network_c.add_node(c)
    
    if unit_type == 'p2g':
        if connect_with_non_slack_gas_node:
            coupling_link_g = GasLink(name='{}_{}'.format(c.name, sink_node_g[-1].name),
                                      start_node=c, end_node=sink_node_g[-1], 
                                      link_type='dummy',
                                      q_max=unit_params['q_max'],
                                      scale_var=scale_var, scale_var_params=sink_node_g[-1].scale_var_params)
            
            print("p2g = ", eta * slack_active_power[network_name_e] / GHV)
            sink_node_g[-1].half_links[0].q += eta * slack_active_power[network_name_e] / GHV
        else:
            coupling_link_g = GasLink(name='{}_{}'.format(c.name, network_g.nodes[0].name),
                                      start_node=c, end_node=network_g.nodes[0], 
                                      link_type='dummy',
                                      q_max=unit_params['q_max'],
                                      scale_var=scale_var, scale_var_params=network_g.nodes[0].scale_var_params)

        coupling_link_e = ElectricalLink(name='{}_{}'.format(network_e.nodes[0].name, c.name), 
                                         start_node=network_e.nodes[0], end_node=c, 
                                         bc_type=['Q_start'], Q_start=0, link_type='dummy', 
                                         P_max=unit_params['P_max'],
                                         scale_var=scale_var, scale_var_params=network_e.nodes[0].scale_var_params)
    else:
        if connect_with_non_slack_gas_node:
            coupling_link_g = GasLink(name='{}_{}'.format(source_node_g[-1].name, c.name),
                                      start_node=source_node_g[-1], end_node=c, 
                                      link_type='dummy',
                                      q_max=unit_params['q_max'],
                                      scale_var=scale_var, scale_var_params=source_node_g[-1].scale_var_params)
            
            source_node_g[-1].half_links[0].q += slack_active_power[network_name_e] / (eta * GHV)
            print("gfg = ", slack_active_power[network_name_e] / (eta * GHV))
        else:
            coupling_link_g = GasLink(name='{}_{}'.format(network_g.nodes[0].name, c.name),
                                      start_node=network_g.nodes[0], end_node=c, 
                                      link_type='dummy',
                                      q_max=unit_params['q_max'],
                                      scale_var=scale_var, scale_var_params=network_g.nodes[0].scale_var_params)
                
        coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, network_e.nodes[0].name), 
                                         start_node=c, end_node=network_e.nodes[0], 
                                         bc_type=['Q_start'], Q_start=0, link_type='dummy', 
                                         P_max=unit_params['P_max'],
                                         scale_var=scale_var, scale_var_params=network_e.nodes[0].scale_var_params)
    
    network_g.add_link(coupling_link_g) 
    network_e.add_link(coupling_link_e)
    
       
    if p2g_units > 0:
        if same_electrical_node:
            if p2g_units > len(source_node_g):
                return None, None, None
        else:     
            if p2g_units > min(len(source_node_g), len(sink_node_e)):
                return None, None, None
    
    if gfg_units > 0:
        if same_electrical_node:
            if gfg_units > len(sink_node_g):
                return None, None, None
        else:     
            if gfg_units > min(len(sink_node_g), len(source_node_e)):
                return None, None, None
    
    
    unit_type = 'p2g'
    if same_electrical_node:
        for i, node_g in enumerate(source_node_g): # Replacing source from terminal link to coupling link
            if i < p2g_units:        
                c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
                                      bc_type=[], unit_type=unit_type, unit_params=unit_params,
                                      scale_var=scale_var, scale_var_params=None, bounded=bounded)
                network_c.add_node(c)

                coupling_link_g = GasLink(name='{}_{}'.format(c.name, node_g.name),
                                          start_node=c, end_node=node_g, 
                                          bc_type=['q'], q=-node_g.half_links[0].q, link_type='dummy',
                                          q_max=unit_params['q_max'],
                                          scale_var=scale_var, scale_var_params=node_g.scale_var_params)
                network_g.add_link(coupling_link_g)
                
                node_e = network_e.nodes[0]
                coupling_link_e = ElectricalLink(name='{}_{}'.format(node_e.name, c.name), 
                                                 start_node=node_e, end_node=c, 
                                                 bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                 P_max=unit_params['P_max'],
                                                 scale_var=scale_var, scale_var_params=node_e.scale_var_params)
                network_e.add_link(coupling_link_e)
                                
                scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                                    'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
                c.scale_var_params = scale_var_params
                
                if adjust_power:
                    P_adjust = GHV * node_g.half_links[0].q / eta
                    node_e.half_links[0].P += P_adjust # Make sure equivalent amount of energy is added.
                node_g.half_links[0].q = 0
            else:
                break
    else:
        for i, (node_e, node_g) in enumerate(zip(sink_node_e, source_node_g)):
            if i < p2g_units:
                c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
                                      bc_type=[], unit_type=unit_type, unit_params=unit_params,
                                      scale_var=scale_var, scale_var_params=None, bounded=bounded)
                network_c.add_node(c)

                coupling_link_g = GasLink(name='{}_{}'.format(c.name, node_g.name),
                                          start_node=c, end_node=node_g, 
                                          bc_type=['q'], q=-node_g.half_links[0].q, link_type='dummy',
                                          q_max=unit_params['q_max'],
                                          scale_var=scale_var, scale_var_params=node_g.scale_var_params)
                network_g.add_link(coupling_link_g)
                                
                coupling_link_e = ElectricalLink(name='{}_{}'.format(node_e.name, c.name), 
                                                 start_node=node_e, end_node=c, 
                                                 bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                 P_max=unit_params['P_max'],
                                                 scale_var=scale_var, scale_var_params=node_e.scale_var_params)
                network_e.add_link(coupling_link_e)
                                        
                scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                                    'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
                c.scale_var_params = scale_var_params
                
                if adjust_power:
                    P_adjust = GHV * node_g.half_links[0].q / eta
                    node_e.half_links[0].P += P_adjust # Make sure equivalent amount of energy is added.
                node_g.half_links[0].q = 0
            else:
                break
    
    unit_type = 'gas_fired_generator'
    if same_electrical_node:
        for i, node_g in enumerate(sink_node_g): # Replacing sink from terminal link to coupling link
            if i < gfg_units:          
                c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
                                      bc_type=[], unit_type=unit_type, unit_params=unit_params,
                                      scale_var=scale_var, scale_var_params=None, bounded=bounded)
                network_c.add_node(c)

                coupling_link_g = GasLink(name='{}_{}'.format(node_g.name, c.name),
                                          start_node=node_g, end_node=c, 
                                          bc_type=['q'], q=node_g.half_links[0].q, link_type='dummy',
                                          q_max=unit_params['q_max'],
                                          scale_var=scale_var, scale_var_params=node_g.scale_var_params)
                network_g.add_link(coupling_link_g)
                            
                node_e = network_e.nodes[0]
                coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node_e.name), 
                                                 start_node=c, end_node=node_e, 
                                                 bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                 P_max=unit_params['P_max'],
                                                 scale_var=scale_var, scale_var_params=node_e.scale_var_params)
                network_e.add_link(coupling_link_e)

                
                scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                                    'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
                c.scale_var_params = scale_var_params
                
                if adjust_power:
                    P_adjust = GHV * node_g.half_links[0].q * eta
                    node_e.half_links[0].P += P_adjust # Make sure equivalent amount of energy is added.
                node_g.half_links[0].q = 0
            else:
                break
    else:
        for i, (node_e, node_g) in enumerate(zip(source_node_e, sink_node_g)):
            if i < gfg_units:                
                c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
                                      bc_type=[], unit_type=unit_type, unit_params=unit_params,
                                      scale_var=scale_var, scale_var_params=None, bounded=bounded)
                network_c.add_node(c)

                coupling_link_g = GasLink(name='{}_{}'.format(node_g.name, c.name),
                                          start_node=node_g, end_node=c, 
                                          bc_type=['q'], q=node_g.half_links[0].q, link_type='dummy',
                                          q_max=unit_params['q_max'],
                                          scale_var=scale_var, scale_var_params=node_g.scale_var_params)
                network_g.add_link(coupling_link_g)
                
                coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node_e.name), 
                                                 start_node=c, end_node=node_e, 
                                                 bc_type=['Q_start'], Q_start=0, link_type='dummy',
                                                 P_max=unit_params['P_max'],
                                                 scale_var=scale_var, scale_var_params=node_e.scale_var_params)
                network_e.add_link(coupling_link_e)
                                        
                scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
                                    'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
                c.scale_var_params = scale_var_params
                
                if adjust_power:
                    P_adjust = GHV * node_g.half_links[0].q * eta
                    node_e.half_links[0].P += P_adjust # Make sure equivalent amount of energy is added.
                node_g.half_links[0].q = 0
            else:
                break
    
    # unit_type = 'gas_fired_generator' 
    # if same_gas_node:
    #     for i, node_e in enumerate(source_node_e): # Replacing source from terminal link to coupling link
    #         if i < gfg_units:        
    #             c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
    #                                   bc_type=[], unit_type=unit_type, unit_params=unit_params,
    #                                   scale_var=scale_var, scale_var_params=None)
    #             network_c.add_node(c)

    #             coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node_e.name), 
    #                                              start_node=c, end_node=node_e, 
    #                                              bc_type=['P_start', 'Q_start'], P_start=-node_e.half_links[0].P, Q_start=0, link_type='dummy',
    #                                              scale_var=scale_var, scale_var_params=node_e.scale_var_params)
    #             network_e.add_link(coupling_link_e)
                 
    #             q_c = node_e.half_links[0].P / (eta * GHV)
    #             node_e.half_links[0].P = 0 
                
    #             node_g = network_g.nodes[0]
    #             coupling_link_g = GasLink(name='{}_{}'.format(node_g.name, c.name),
    #                                       start_node=node_g, end_node=c, 
    #                                       bc_type=[], link_type='dummy',
    #                                       scale_var=scale_var, scale_var_params=node_g.scale_var_params)
    #             network_g.add_link(coupling_link_g)
    #             if adjust_flow:
    #                 node_g.half_links[0].q += q_c # Make sure equivalent amount of energy is added.
                
    #             scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
    #                                 'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
    #             c.scale_var_params = scale_var_params
    #         else:
    #             break
    # else:
    #     for i, (node_e, node_g) in enumerate(zip(source_node_e, sink_node_g)):
    #         if i < gfg_units:
    #             c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
    #                                   bc_type=[], unit_type=unit_type, unit_params=unit_params,
    #                                   scale_var=scale_var, scale_var_params=None)
    #             network_c.add_node(c)

    #             coupling_link_e = ElectricalLink(name='{}_{}'.format(c.name, node_e.name), 
    #                                              start_node=c, end_node=node_e, 
    #                                              bc_type=['P_start', 'P_end', 'Q_start'], 
    #                                              P_start=-node_e.half_links[0].P, P_end=node_e.half_links[0].P, 
    #                                              Q_start=0, link_type='dummy',
    #                                              scale_var=scale_var, scale_var_params=node_e.scale_var_params)
    #             network_e.add_link(coupling_link_e)
                    
    #             q_c = node_e.half_links[0].P / (eta * GHV)
    #             node_e.half_links[0].P = 0 # Make sure equivalent amount of energy is added.

    #             coupling_link_g = GasLink(name='{}_{}'.format(node_g.name, c.name),
    #                                       start_node=node_g, end_node=c, 
    #                                       bc_type=[], link_type='dummy',
    #                                       scale_var=scale_var, scale_var_params=node_g.scale_var_params)
    #             network_g.add_link(coupling_link_g)
    #             if adjust_flow:
    #                 node_g.half_links[0].q += q_c
                    
    #             scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
    #                                 'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
    #             c.scale_var_params = scale_var_params
                
    #         else:
    #             break
    
    # unit_type = 'p2g'        
    # if same_gas_node:
    #     for i, node_e in enumerate(sink_node_e): # Replacing sink from terminal link to coupling link
    #         if i < p2g_units:          
    #             c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
    #                                   bc_type=[], unit_type=unit_type, unit_params=unit_params,
    #                                   scale_var=scale_var, scale_var_params=None)
    #             network_c.add_node(c)
                
    #             coupling_link_e = ElectricalLink(name='{}_{}'.format(node_e.name, c.name), 
    #                                              start_node=node_e, end_node=c, 
    #                                              bc_type=['P_start', 'Q_start'], P=node_e.half_links[0].P, Q_start=0, link_type='dummy',
    #                                              scale_var=scale_var, scale_var_params=node_e.scale_var_params)
    #             network_e.add_link(coupling_link_e)
                
    #             q_c = node_e.half_links[0].P * eta / GHV
    #             node_e.half_links[0].P = 0 

    #             node_g = network_g.nodes[0]
    #             coupling_link_g = GasLink(name='{}_{}'.format(c.name, node_g.name),
    #                                       start_node=c, end_node=node_g, 
    #                                       bc_type=[], link_type='dummy',
    #                                       scale_var=scale_var, scale_var_params=node_g.scale_var_params)
    #             network_g.add_link(coupling_link_g)
    #             if adjust_flow:
    #                 node_g.half_links[0].q += q_c # Make sure equivalent amount of energy is added.
                
    #             scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
    #                                 'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
    #             c.scale_var_params = scale_var_params
    #         else:
    #             break
    # else:
    #     for i, (node_e, node_g) in enumerate(zip(sink_node_e, source_node_g)):
    #         if i < p2g_units:
    #             c = HeterogeneousNode(name='{}_{}'.format(unit_type, i), 
    #                                   bc_type=[], unit_type=unit_type, unit_params=unit_params,
    #                                   scale_var=scale_var, scale_var_params=None)
    #             network_c.add_node(c)
                
    #             coupling_link_e = ElectricalLink(name='{}_{}'.format(node_e.name, c.name), 
    #                                              start_node=node_e, end_node=c, 
    #                                              bc_type=['P_start', 'Q_start'], P_start=node_e.half_links[0].P, Q_start=0, link_type='dummy',
    #                                              scale_var=scale_var, scale_var_params=node_e.scale_var_params)
    #             network_e.add_link(coupling_link_e)
                
    #             q_c = node_e.half_links[0].P * eta / GHV
    #             node_e.half_links[0].P = 0 
                
    #             coupling_link_g = GasLink(name='{}_{}'.format(c.name, node_g.name),
    #                                       start_node=c, end_node=node_g, 
    #                                       bc_type=[], link_type='dummy',
    #                                       scale_var=scale_var, scale_var_params=node_g.scale_var_params)
    #             network_g.add_link(coupling_link_g)
    #             if adjust_flow:
    #                 node_g.half_links[0].q += q_c # Make sure equivalent amount of energy is added.
                              
    #             scale_var_params = {'Ebase' : node_e.scale_var_params['Sbase'],
    #                                 'GHVbase' : node_e.scale_var_params['Sbase'] / node_g.scale_var_params['qbase']}
    #             c.scale_var_params = scale_var_params
                
    #         else:
    #             break
                  
    network_c.add_network(network_g)
    network_c.add_network(network_e)
        
    network_c.initialize()
                    
    return network_e, network_g, network_c
    
        
def create_x_init(network_e=None, network_g=None, network_c=None):
    q_init = 0.1 * np.ones(len(network_g.link_unknown_q) + len(network_g.dummy_link_unknown_q))
    p_init = np.linspace(0.95, 0.9, network_g.number_of_unknown_p)

    delta_init = np.zeros(len(network_e.unknown_delta_nodes)) # flat start 0
    V_init = np.ones(len(network_e.unknown_V_nodes)) # flat start 1
    
    q_c_init = np.zeros(len(list(network_g.get_links(link_types=['dummy'], exclude_bc_types=[['q']])))-len(network_g.dummy_link_unknown_q))
    P_c_init = np.zeros(len(list(network_e.get_links(link_types=['dummy'], exclude_bc_types=[['P_start'], ['P_start', 'Q_start'], ['P_start', 'P_end', 'Q_start']]))))
    
    x_init = np.concatenate([q_init, p_init, 
                             delta_init, V_init, 
                             q_c_init, P_c_init])
        
    return x_init
        

# %% Test options

adjust_power = True # Adjust boundary condition for additional load
adjust_flow = False
same_electrical_node = False # Connect both coupling units to same electrical node
same_gas_node = False
p2g_units_max = 1
gfg_units_max = 1

bounded = False
P_max = 10**100
connect_with_non_slack_gas_node = False

save = False


# %% Run test cases

for p2g_units in range(1, p2g_units_max+1):
    for gfg_units in range(1, gfg_units_max+1):       
        if save:
            if adjust_power:
                test = 'adjust_power'
            elif same_electrical_node:
                test = 'same_electrical_node'
            else:
                test = ''

            # directory = os.path.join(os.path.abspath('.'), 
            #                          'results_gmres_block_ilu(5, 3)',
            #                          'results_p2g_gfg_slack_1_{}'.format(test),
            #                          'results_p2g_{}_gfg_{}_slack_1_{}'.format(p2g_units, gfg_units, test))
            
            # directory = os.path.join(os.path.abspath('.'), 
            #                          'results_direct_solver',
            #                          'results_p2g_gfg_non-slack_1_{}'.format(test),
            #                          'results_p2g_{}_gfg_{}_non-slack_1_{}'.format(p2g_units, gfg_units, test))
            
            directory = os.path.join(os.path.abspath('.'), 
                                    'results_direct_solver',
                                    'results_p2g_gfg_slack_{}'.format(test),
                                    'results_p2g_{}_gfg_{}_slack_{}'.format(p2g_units, gfg_units, test))
            
            os.makedirs(name=os.path.join(directory, "solution"), exist_ok=True)
            os.makedirs(name=os.path.join(directory, "residuals"), exist_ok=True)
            if lin_solver != 'lu':
                os.makedirs(name=os.path.join(directory, "residuals_krylov"), exist_ok=True)


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


        flow = 'average' # 'min' # 'max'
        pressure = 'max' # 'min' # 'average'
        gas_type = 'hydrogen' # 'natural'
                            
        link_settings = {'friction' : 'friction_weymouth', # 'friction_pole'
                         'link_type' : 'pipe_high', # 'pipe_low'
                         'link_equation_formulation' : 'dp_of_q'} # 'q_of_dp'

        resistor = False # True


        solver = 'nr'
        solver_parameters = {'m' : 3, # Anderson acceleration
                             'max_iterations' : 20,
                             'optimal_multiplier' : False,
                             'residual_q' : False,
                             'tol' : 1e-6}
        
        
        lin_solver = 'lu'
        lin_solver_parameters = {'block_size' : None,
                                 'diag_pivot_thresh' : 1,
                                 'drop_tol' : 1e-4,
                                 'drop_rule' : ['basic', 'area'],
                                 'fill_factor': 5,
                                 'fill_factor_11' : 5,
                                 'fill_factor_22' : 4,
                                 'max_iterations': 100,
                                 'reorderfornonzerodiagonal' : False, # also affects ordering for petsc
                                 'options' : {'Equil' : True},
                                 'permc_spec': 'colamd',
                                 'preconditioner': 'gauss',
                                 'preconditioners_for_blocks': [],
                                 'preconditioners_for_two_level': [],
                                 'rcm' : False,
                                 'residuals_filename' : None,
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


        if save:
            converged_message = ""
            difference_message = ""
            difference_e_message = ""
            difference_g_message = ""
            iterations_message = ""


        for network_name_e in network_names_e:
            if save:  
                converged_message += "\\textbf{{{}}} & ".format(network_name_e)
                difference_message += "\\textbf{{{}}} & ".format(network_name_e)
                difference_e_message += "\\textbf{{{}}} & ".format(network_name_e)
                difference_g_message += "\\textbf{{{}}} & ".format(network_name_e)
                iterations_message += "\\textbf{{{}}} & ".format(network_name_e)
            
            
            for network_name_g in network_names_g:
                print(50*"-" + "\n" + network_name_e + " + " + network_name_g + " (p2g={}, gfg={})".format(p2g_units, gfg_units) + "\n" + 50*"-")
                
                network_e, network_g, network = create_network(network_name_e=network_name_e,
                                                               network_name_g=network_name_g,
                                                               adjust_power=adjust_power,
                                                               adjust_flow=adjust_flow,
                                                               same_electrical_node=same_electrical_node,
                                                               same_gas_node=same_gas_node,
                                                               p2g_units=p2g_units,
                                                               gfg_units=gfg_units,
                                                               bounded=bounded,
                                                               P_max=P_max,
                                                               connect_with_non_slack_gas_node=connect_with_non_slack_gas_node)
                
                if network is None:
                    break
                
    
                if 'block' in lin_solver_parameters['preconditioner']:        
                    lin_solver_parameters['block_size'] = len(network.x_g_entries)
                
                if lin_solver != 'lu':
                    lin_solver_parameters['residuals_filename'] = os.path.join(directory, 'residuals_krylov', '{}_{}.txt'.format(network_name_e, network_name_g))
                    open(lin_solver_parameters['residuals_filename'], 'w').close()
                
                
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
                
                
                # for node in network.networks[0].nodes:
                #     if 'source_2' in node.name:
                #         print('{} p = {}'.format(node.name, node.p, network.x_entries.index(node)))
                          
                # for node in network.networks[1].nodes:
                #     if node.name == 227:
                #         print('{} V = {}'.format(node.name, node.V, network.x_entries.index(node)))
                
                
                if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
                    print("Average F time in seconds = {:.4e}".format(np.average(network.solver.F_times)))
                    print("Average J time in seconds = {:.4e}".format(np.average(network.solver.J_times)))
                    print("Average linear solve time in seconds = {:.4e}".format(np.average(network.solver.linear_solve_times)))
                print("Average non-linear solve time in seconds = {:.4e}".format(np.average(network.solver.nonlinear_solve_times)))
                print("Total time in seconds = {:.4e}".format(network.solver.total_time))
                
                print("Iterations = {:d}".format(iterations))
                print("Final error = {:.3e}".format(errors[-1]))
                
                
                if save:
                    x_g = np.loadtxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results", "solution", "{}.txt".format(network_name_g)))
                    difference_g = np.linalg.norm(x_g - x_sol[:len(network.x_g_entries)], ord=np.inf)
                    print("Max-norm difference (g) = {}".format(difference_g))
                    
                    x_e = np.loadtxt(os.path.join(os.path.abspath('.'), "code", "pandapower", "results", "solution", "{}.txt".format(network_name_e)))
                    difference_e = np.linalg.norm(x_e - x_sol[len(network.x_g_entries):len(network.x_g_entries)+len(network.x_e_entries)], ord=np.inf)
                    print("Max-norm difference (e) = {}".format(difference_e))
                    
                    converged_message += "{} & ".format(errors[-1] < solver_parameters['tol'])
                    difference_message += "{:6.3e} & ".format(max(difference_e, difference_g))
                    difference_e_message += "{:6.3e} & ".format(difference_e)
                    difference_g_message += "{:6.3e} & ".format(difference_g)
                    iterations_message += "{} & ".format(iterations)
                
                
                    np.savetxt(os.path.join(directory, "solution", "{}_{}.txt".format(network_name_e, network_name_g)), x_sol)
                    np.savetxt(os.path.join(directory, "residuals", "{}_{}.txt".format(network_name_e, network_name_g)), errors)
            
              
            if save: 
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
           
           
        if save:     
            header = ""
            for network_name_g in network_names_g:
                header += "\\textbf{{{}}} & ".format(network_name_g)
            header = header[:-2] + "\\\\ \\hline \n"
            
            save_table(filename="converged", directory=directory, header=header, body=converged_message)
            save_table(filename="difference", directory=directory, header=header, body=difference_message)
            save_table(filename="difference_e", directory=directory, header=header, body=difference_e_message)
            save_table(filename="difference_g", directory=directory, header=header, body=difference_g_message)
            save_table(filename="iterations", directory=directory, header=header, body=iterations_message)