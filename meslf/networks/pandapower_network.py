import numpy as np
import os
import pandapower
import time

from tqdm import tqdm

from meslf.networks.electrical_network import ElectricalNetwork, ElectricalNode, ElectricalLink, ElectricalHalfLink

# %%

class PandapowerNetwork():
    def __init__(self, network_name):
        self.network_name = network_name
    
    
    def get_data(self):
        """
        Get data from pandapower based on the name of the network.

        Parameters
        ----------
            network_name : str
                Name of the network. Options:
                - 'case4gs',
                - 'case5',
                - 'case6ww',
                - 'case9',
                - 'case14',
                - 'case24_ieee_rts',
                - 'GBreducednetwork',
                - 'case30',
                - 'case_ieee30',
                - 'case33bw',
                - 'case39',
                - 'case57',
                - 'case89pegase',
                - 'case118',
                - 'case145',
                - 'iceland',
                - 'case_illinois200',
                - 'case300',
                - 'case1354pegase',
                - 'case1888rte',
                - 'GBnetwork',
                - 'case2848rte',
                - 'case2869pegase',
                - 'case3120sp',
                - 'case6470rte',
                - 'case6495rte',
                - 'case6515rte',
                - 'case9241pegase'.

        Return
        ----------
            Return : pandapower.networks
                A pandapower network object.
        """
        
        result = {}
        exec("data = pandapower.networks.{}()".format(self.network_name), globals(), result)
        return result['data']


    def compute_admittance(self, c_nf_per_km, f, g_us_per_km, length_km, parallel, r_ohm_per_km, x_ohm_per_km, Sbase, Vbase):
        r = r_ohm_per_km*length_km/parallel
        x = x_ohm_per_km*length_km/parallel
        
        b = -x / (r**2 + x**2)
        g = r / (r**2 + x**2)
        
        b_sh = 2*np.pi*f*c_nf_per_km*10**-9*length_km*parallel
        g_sh = g_us_per_km*10**-6*length_km*parallel

        return g, b, g_sh, b_sh


    def compute_trafo(self, vn_hv_kv, vn_lv_kv, vn_kv_from, vn_kv_to, pfe_kw, i0_percent, vk_percent, vkr_percent, \
                      sn_mva, sn_mva_net, \
                      tap_neutral, tap_changer_type, tap_pos, tap_side, tap_step_degree, tap_step_percent, \
                      shift_degree):
        
        if (tap_changer_type == 'Ratio') and (not np.isnan(tap_step_percent)) and (not np.isnan(tap_neutral)) and (not np.isnan(tap_pos)):
            n_tap = abs(1 + (tap_pos - tap_neutral) * tap_step_percent * 0.01)
            if tap_side == 'hv':
                vn_hv_kv *= n_tap
            elif tap_side =='lv':
                vn_lv_kv *= n_tap
                
        ratio = (vn_hv_kv / vn_lv_kv)

        admittance_unit = sn_mva / vn_lv_kv**2
            
        vk_percent *= 0.01
        vkr_percent *= 0.01
        i0_percent *= 0.01

        r = vkr_percent
        x = vk_percent
        x = np.sign(vk_percent) * np.sqrt(x**2 - r**2)
        
        b = -x / (r**2 + x**2) * admittance_unit
        g = r / (r**2 + x**2) * admittance_unit
        
        g_sh = pfe_kw / (sn_mva * 1000) 
        b_sh = i0_percent**2 - g_sh**2
        if b_sh < 0:
            b_sh = 0
        b_sh = -np.sign(i0_percent) * np.sqrt(b_sh) * admittance_unit
        g_sh *= admittance_unit
                    
        if 'tap_changer_type' == 'Ideal': # False: # tap_phase_shifter:        
            if not np.isnan(tap_step_degree):
                shift_degree_tp = tap_step_degree*(tap_pos - tap_neutral)
            elif not np.isnan(tap_step_percent):
                shift_degree_tp = 2*np.arcsin(0.5*tap_step_percent*10**-2)*(tap_pos - tap_neutral)
            else:
                shift_degree_tp = 0
            
            phase_shift = (shift_degree + shift_degree_tp)*np.pi/180
        else:
            phase_shift = 0

        return g, b, g_sh, b_sh, ratio, phase_shift, vn_hv_kv, vn_lv_kv


    def create_network(self, ignore_nodes=[], formulation='complex_power', scale_var=None, 
                       change_first_slack=False, number_of_clones=1, number_of_merges=0):
        MW = 10**6
        KV = 10**3
        
        # Initialise electrical network
        network = ElectricalNetwork(name=self.network_name, formulation=formulation)
        
        # slack_data = np.genfromtxt(os.path.join(os.path.abspath('.'), "code", "pandapower", "results", "slack_value.txt"), dtype=['<U20', float, float])
        # slack_active_power = {}
        # slack_reactive_power = {}
        # for data in slack_data:
        #     slack_active_power[data[0]] = data[1] 
        #     slack_reactive_power[data[0]] = data[2] 
        # slack_data = None
        
        data = self.get_data()
        data.gen.loc[data.gen['sn_mva'].isnull(), 'sn_mva'] = data.sn_mva
        data.load.loc[data.load['sn_mva'].isnull(), 'sn_mva'] = data.sn_mva
        data.sgen.loc[data.sgen['sn_mva'].isnull(), 'sn_mva'] = data.sn_mva
        f = data.f_hz # default frequency
        
        index_shunt_buses = set(data.shunt['bus'].values)
        
        save_merge_pq_node_even = {}
        save_merge_pq_node_odd = {}
                
        for clone_number in tqdm(range(number_of_clones)):
            number_of_merge_pq_nodes = 0
            
            nodes = {}
            Sbase = {}
            
            if (clone_number % 2) == 0:
                merge_pq_node_even = {}
            else:
                merge_pq_node_odd = {}

            # Slack node (V=V, delta=delta)
            # Slack nodes should be defined first, so that the first terminal link is a slack
            for index, row in data.ext_grid.iterrows():
                if row['in_service']:
                    if row['bus'] not in ignore_nodes:
                        if nodes.get(row['bus']) is None: # Avoid overlapping voltage variables
                            if change_first_slack:
                                Sbase[row['bus']] = data.sn_mva * MW

                                scale_var_params = {'Sbase' : Sbase[row['bus']], 
                                                    'Vbase' : data.bus.loc[row['bus'], 'vn_kv']*KV,
                                                    'deltabase' : 1}

                                node = ElectricalNode(name=row['bus'],
                                                      bc_type=['P',  'V', 'delta'],
                                                      V=row['vm_pu']*scale_var_params['Vbase'],
                                                      delta=row['va_degree']*np.pi/180,
                                                      scale_var=scale_var,
                                                      scale_var_params=scale_var_params)
                                network.add_node(node)
                                
                                nodes[row['bus']] = network.nodes[-1] 

                                half_link = ElectricalHalfLink(name = '{}_PVdelta'.format(row['bus']), start_node=node, P=0)
                                network.add_half_link(half_link)

                                change_first_slack = False
                            else:
                                Sbase[row['bus']] = data.sn_mva * MW

                                scale_var_params = {'Sbase' : Sbase[row['bus']],
                                                    'Vbase' : data.bus.loc[row['bus'], 'vn_kv']*KV,
                                                    'deltabase' : 1}

                                node = ElectricalNode(name=row['bus'],
                                                      bc_type=['V', 'delta'],
                                                      V=row['vm_pu']*scale_var_params['Vbase'],
                                                      delta=row['va_degree']*np.pi/180,
                                                      scale_var=scale_var,
                                                      scale_var_params=scale_var_params)
                                network.add_node(node)
                                
                                nodes[row['bus']] = network.nodes[-1] 

                                half_link = ElectricalHalfLink(name='{}_slack'.format(row['bus']), start_node=node)
                                network.add_half_link(half_link)


            # PV node (P=-P, V=V)
            for index, row in data.gen.iterrows():
                if row['in_service']:
                    if row['bus'] not in ignore_nodes:
                        if nodes.get(row['bus']) is None: # Avoid overlapping voltage variables
                            Sbase[row['bus']] = row['sn_mva'] * MW

                            scale_var_params = {'Sbase' : Sbase[row['bus']],
                                                'Vbase' : data.bus.loc[row['bus'], 'vn_kv']*KV,
                                                'deltabase' : 1}

                            node = ElectricalNode(name=row['bus'],
                                                  V=row['vm_pu']*scale_var_params['Vbase'],
                                                  bc_type=['P', 'V'],
                                                  scale_var=scale_var,
                                                  scale_var_params=scale_var_params)
                            network.add_node(node)
                            
                            nodes[row['bus']] = network.nodes[-1]

                            half_link = ElectricalHalfLink(name='{}_pv'.format(row['bus']), 
                                                           start_node=node,
                                                           P=-row['p_mw']*MW)
                            network.add_half_link(half_link)
  

            # PQ node (static generator, P=-P, Q=-Q)
            for index, row in data.sgen.iterrows():
                if row['in_service']:
                    if row['bus'] not in ignore_nodes:
                        if nodes.get(row['bus']) is None:
                            Sbase[row['bus']] = row['sn_mva'] * MW

                            scale_var_params = {'Sbase' : Sbase[row['bus']],
                                                'Vbase' : data.bus.loc[row['bus'], 'vn_kv']*KV,
                                                'deltabase' : 1}

                            node = ElectricalNode(name=row['bus'],
                                                  bc_type=['P', 'Q'],
                                                  scale_var=scale_var,
                                                  scale_var_params=scale_var_params)
                            network.add_node(node)
                            
                            nodes[row['bus']] = network.nodes[-1]

                            half_link = ElectricalHalfLink(name='{}_sgen'.format(row['bus']), 
                                                           start_node=node,
                                                           P=-row['p_mw']*MW,
                                                           Q=-row['q_mvar']*MW)
                            network.add_half_link(half_link)
                        else:
                            half_link = ElectricalHalfLink(name='{}_sgen'.format(row['bus']), 
                                                           start_node=nodes[row['bus']],
                                                           P=-row['p_mw']*MW,
                                                           Q=-row['q_mvar']*MW)
                            network.add_half_link(half_link)
                            

            # Load (PQ node)
            for index, row in data.load.iterrows():
                if row['in_service']:
                    if row['bus'] not in ignore_nodes:
                        if nodes.get(row['bus']) is None:
                            Sbase[row['bus']] = row['sn_mva'] * MW
                            
                            scale_var_params = {'Sbase' : Sbase[row['bus']],
                                                'Vbase' : data.bus.loc[row['bus'], 'vn_kv']*KV,
                                                'deltabase' : 1}
                            
                            node = ElectricalNode(name=row['bus'],
                                                  bc_type=['P', 'Q'],
                                                  scale_var=scale_var,
                                                  scale_var_params=scale_var_params)
                            network.add_node(node)
                            
                            nodes[row['bus']] = node
                            
                            half_link = ElectricalHalfLink(name='{}_pq'.format(row['bus']), 
                                                           start_node=node,
                                                           P=row['p_mw']*MW,
                                                           Q=row['q_mvar']*MW)
                            network.add_half_link(half_link)
                            
                            # if clone_number > 0:
                            #     if (clone_number % 2) == 0:
                            #         no_merge = merge_pq_node_odd.get(row['bus']) is None
                            #     else:
                            #         no_merge = merge_pq_node_even.get(row['bus']) is None
                            # else:
                            #     no_merge = True

                            # if no_merge:
                            #     scale_var_params = {'Sbase' : Sbase[row['bus']],
                            #                         'Vbase' : data.bus.loc[row['bus'], 'vn_kv']*KV,
                            #                         'deltabase' : 1}

                            #     node = ElectricalNode(name=row['bus'],
                            #                           bc_type=['P', 'Q'],
                            #                           scale_var=scale_var,
                            #                           scale_var_params=scale_var_params)
                            #     network.add_node(node)
                                
                            #     nodes[row['bus']] = node

                            #     half_link = ElectricalHalfLink(name='{}_pq'.format(row['bus']), 
                            #                                    start_node=node,
                            #                                    P=row['p_mw']*MW,
                            #                                    Q=row['q_mvar']*MW)
                            #     network.add_half_link(half_link)
                                
                            #     if (row['bus'] not in index_shunt_buses) and (number_of_merge_pq_nodes < number_of_merges):
                            #         if (clone_number % 2) == 0:
                            #             merge_pq_node_even[row['bus']] = node
                            #         else:
                            #             merge_pq_node_odd[row['bus']] = node
                            #         number_of_merge_pq_nodes += 1
                            # else:
                            #     if (clone_number % 2) == 0:
                            #         nodes[row['bus']] = merge_pq_node_odd[row['bus']]
                            #     else:
                            #         nodes[row['bus']] = merge_pq_node_even[row['bus']]
                                    
                            #     nodes[row['bus']].half_links[0].P += row['p_mw'] * MW
                            #     nodes[row['bus']].half_links[0].Q += row['q_mvar'] * MW
                        else:         
                            half_link = ElectricalHalfLink(name='{}_pq'.format(row['bus']), 
                                                           start_node=nodes[row['bus']],
                                                           P=row['p_mw']*MW,
                                                           Q=row['q_mvar']*MW)
                            network.add_half_link(half_link)


            # Shunt (PQ Node, P=P, Q=-Q)
            for index, row in data.shunt.iterrows():
                if row['in_service']:
                    if row['bus'] not in ignore_nodes:
                        if nodes.get(row['bus']) is None:
                            Sbase[row['bus']] = data.sn_mva * MW

                            scale_var_params = {'Sbase' : Sbase[row['bus']],
                                                'Vbase' : data.bus.loc[row['bus'], 'vn_kv']*KV,
                                                'deltabase' : 1}

                            node = ElectricalNode(name=row['bus'],
                                                  bc_type=['P', 'Q'],
                                                  scale_var=scale_var,
                                                  scale_var_params=scale_var_params)
                            network.add_node(node)
                            
                            nodes[row['bus']] = network.nodes[-1]

                            P = row['p_mw']*row['step'] * MW
                            Q = -row['q_mvar']*row['step'] * MW

                            half_link = ElectricalHalfLink(name='{}_shunt'.format(row['bus']), 
                                                           start_node=node,
                                                           P=P,
                                                           Q=Q,
                                                           link_type='nodal_shunt',
                                                           link_params={'b_sh' : Q,
                                                                        'g_sh' : P})
                            network.add_half_link(half_link)
                        else:
                            P = row['p_mw']*row['step'] * MW
                            Q = -row['q_mvar']*row['step'] * MW

                            half_link = ElectricalHalfLink(name='{}_shunt'.format(row['bus']), 
                                                           start_node=nodes[row['bus']],
                                                           P=P,
                                                           Q=Q,
                                                           link_type='nodal_shunt',
                                                           link_params={'b_sh' : Q,
                                                                        'g_sh' : P})
                            network.add_half_link(half_link)


            # Junction (PQ Node, P=0, Q=0)
            for index, row in data.bus.iterrows():
                if row['in_service']:
                    if index not in ignore_nodes:
                        if nodes.get(index) is None:
                            Sbase[index] = data.sn_mva * MW

                            # scale_var_params = {'Sbase' : Sbase[index],
                            #                     'Vbase' : row['vn_kv']*KV,
                            #                     'deltabase' : 1}

                            # node = ElectricalNode(name=index,
                            #                       bc_type=['P', 'Q'],
                            #                       scale_var=scale_var,
                            #                       scale_var_params=scale_var_params)
                            
                            # network.add_node(node)
                            # nodes[index] = network.nodes[-1]
                            
                            if clone_number > 0:
                                if (clone_number % 2) == 0:
                                    no_merge = merge_pq_node_odd.get(index) is None
                                else:
                                    no_merge = merge_pq_node_even.get(index) is None
                            else:
                                no_merge = True

                            if no_merge:
                                scale_var_params = {'Sbase' : Sbase[index],
                                                    'Vbase' : row['vn_kv']*KV,
                                                    'deltabase' : 1}
                                
                                node = ElectricalNode(name=index,
                                                      bc_type=['P', 'Q'],
                                                      scale_var=scale_var,
                                                      scale_var_params=scale_var_params)
                                                            
                                network.add_node(node)
                                
                                nodes[index] = node
                                
                                if (index not in index_shunt_buses) and (number_of_merge_pq_nodes < number_of_merges):
                                    if (clone_number % 2) == 0:
                                        merge_pq_node_even[index] = node
                                    else:
                                        merge_pq_node_odd[index] = node
                                    number_of_merge_pq_nodes += 1
                                    
                                    if clone_number == 0:
                                        save_merge_pq_node_even[index] = len(network.nodes)
                                    elif clone_number == 1:
                                        save_merge_pq_node_odd[index] = len(network.nodes)
                            else:
                                if (clone_number % 2) == 0:
                                    nodes[index] = merge_pq_node_odd[index]
                                else:
                                    nodes[index] = merge_pq_node_even[index]


            # Line
            for index, row in data.line.iterrows():
                if row['in_service']:
                    if (row['from_bus'] not in ignore_nodes) and (row['to_bus'] not in ignore_nodes):
                        g, b, g_sh, b_sh = self.compute_admittance(c_nf_per_km=row['c_nf_per_km'],
                                                                   f=f,
                                                                   g_us_per_km=row['g_us_per_km'],
                                                                   length_km=row['length_km'],
                                                                   parallel=row['parallel'],
                                                                   r_ohm_per_km=row['r_ohm_per_km'],
                                                                   x_ohm_per_km=row['x_ohm_per_km'],
                                                                   Sbase=Sbase[row['from_bus']],
                                                                   Vbase=data.bus.loc[row['from_bus']].vn_kv)
                        
                        scale_var_params = {'Sbase' : Sbase[row['from_bus']],
                                            'Vbase' : data.bus.loc[row['from_bus']].vn_kv*KV}
                        
                        network.add_link(ElectricalLink(name="{}-{}".format(row['from_bus'], row['to_bus']),
                                                        start_node=nodes[row['from_bus']],
                                                        end_node=nodes[row['to_bus']],
                                                        bc_type=[],
                                                        link_type='pi_line',
                                                        link_params={'b' : b,
                                                                     'g' : g,
                                                                     'b_sh' : b_sh,
                                                                     'g_sh' : g_sh},
                                                        scale_var=scale_var,
                                                        scale_var_params=scale_var_params))



            # Transformer
            for index, row in data.trafo.iterrows():
                if row['in_service']:
                    if (row['hv_bus'] not in ignore_nodes) and (row['lv_bus'] not in ignore_nodes):
                        g, b, g_sh, b_sh, ratio, phase_shift, vn_hv_kv, vn_lv_kv = self.compute_trafo(vn_hv_kv=row['vn_hv_kv'],
                                                                                                      vn_lv_kv=row['vn_lv_kv'],
                                                                                                      vn_kv_from=data.bus.loc[row['hv_bus']].vn_kv,
                                                                                                      vn_kv_to=data.bus.loc[row['lv_bus']].vn_kv,
                                                                                                      pfe_kw=row['pfe_kw'],
                                                                                                      i0_percent=row['i0_percent'],
                                                                                                      vk_percent=row['vk_percent'],
                                                                                                      vkr_percent=row['vkr_percent'],
                                                                                                      sn_mva=row['sn_mva'],
                                                                                                      sn_mva_net=data.sn_mva,
                                                                                                      tap_neutral=row['tap_neutral'],
                                                                                                      tap_changer_type=row['tap_changer_type'],
                                                                                                      tap_pos=row['tap_pos'],
                                                                                                      tap_side=row['tap_side'],
                                                                                                      tap_step_degree=row['tap_step_degree'],
                                                                                                      tap_step_percent=row['tap_step_percent'],
                                                                                                      shift_degree=row['shift_degree'])
                        
                        scale_var_params = {'Sbase' : row['sn_mva']*MW,
                                            'Sbase_net' : data.sn_mva*MW,
                                            'Vbase_high' : vn_hv_kv*KV,
                                            'Vbase_low' : vn_lv_kv*KV,
                                            'Vbase_from' : data.bus.loc[row['hv_bus']].vn_kv*KV,
                                            'Vbase_to' : data.bus.loc[row['lv_bus']].vn_kv*KV}

                        network.add_link(ElectricalLink(name="{}-{}".format(row['hv_bus'], row['lv_bus']),
                                                        start_node=nodes[row['hv_bus']],
                                                        end_node=nodes[row['lv_bus']],
                                                        bc_type=[],
                                                        link_type='pi_line_trafo',
                                                        link_params={'b' : b,
                                                                     'g' : g,
                                                                     'b_sh' : b_sh,
                                                                     'g_sh' : g_sh,
                                                                     'ratio' : ratio,
                                                                     'phase_shift' : phase_shift},
                                                        scale_var=scale_var,
                                                        scale_var_params=scale_var_params))
               
        # print(save_merge_pq_node_even)
        # print(save_merge_pq_node_odd)
                            
        return network, data