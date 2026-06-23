import numpy as np
import pandapower

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
                -'case4gs',
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
                A pandapower network object
        """
        
        result = {}
        exec("data = pandapower.networks.{}()".format(self.network_name), globals(), result)
        return result['data']


    def find_node(self, name, network, node_names):
        return network.nodes[node_names.index(name)]


    def compute_admittance(self, c_nf_per_km, f, g_us_per_km, length_km, parallel, r_ohm_per_km, x_ohm_per_km, Sbase, Vbase):
        r = r_ohm_per_km*length_km/parallel
        x = x_ohm_per_km*length_km/parallel
        
        Zbase = Vbase**2 / Sbase
        
        b = -x / (r**2 + x**2) * Zbase
        g = r / (r**2 + x**2) * Zbase
        
        b_sh = 2*np.pi*f*c_nf_per_km*10**-9*length_km*parallel * Zbase
        g_sh = g_us_per_km*10**-6*length_km*parallel * Zbase

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
                
        ratio = (vn_hv_kv / vn_lv_kv) * (vn_kv_to / vn_kv_from) 

        sn_ratio = sn_mva_net / sn_mva
        vn_ratio = (vn_kv_to / vn_lv_kv)**2
            
        vk_percent *= 0.01
        vkr_percent *= 0.01
        i0_percent *= 0.01

        r = vkr_percent
        x = vk_percent
        x = np.sign(vk_percent) * np.sqrt(x**2 - r**2)
        
        b = -x / (r**2 + x**2) * vn_ratio / sn_ratio
        g = r / (r**2 + x**2) * vn_ratio / sn_ratio
        
        g_sh = pfe_kw / (sn_mva * 1000) 
        b_sh = i0_percent**2 - g_sh**2
        if b_sh < 0:
            b_sh = 0
        b_sh = -np.sign(i0_percent) * np.sqrt(b_sh) * vn_ratio / sn_ratio
        g_sh *= vn_ratio / sn_ratio
                    
        if tap_changer_type == 'Ideal':        
            if not np.isnan(tap_step_degree):
                shift_degree_tp = tap_step_degree*(tap_pos - tap_neutral)
            elif not np.isnan(tap_step_percent):
                shift_degree_tp = 2*np.arcsin(0.5*tap_step_percent*10**-2)*(tap_pos - tap_neutral)
            else:
                shift_degree_tp = 0
            
            phase_shift = (shift_degree + shift_degree_tp)*np.pi/180
        else:
            phase_shift = 0

        return g, b, g_sh, b_sh, ratio, phase_shift


    def create_network(self, ignore_nodes=[], formulation='complex_power', scale_var=None):
        MW = 10**6
        KV = 10**3
        
        data = self.get_data()

        f = data.f_hz # default frequency

        network = ElectricalNetwork(name=self.network_name, formulation=formulation)
        
        node_names = []
        Sbase = {}
        
        scale_var_params = None

        data.gen.loc[data.gen['sn_mva'].isnull(), 'sn_mva'] = data.sn_mva
        data.load.loc[data.load['sn_mva'].isnull(), 'sn_mva'] = data.sn_mva
        data.sgen.loc[data.sgen['sn_mva'].isnull(), 'sn_mva'] = data.sn_mva

        # Slack node (V=V, delta=delta)
        # Slack nodes should be defined first, so that the first terminal link is a slack
        for index, row in data.ext_grid.iterrows():
            if row['in_service']:
                node_name = data.bus.loc[row['bus'], 'name']
                                        
                if node_name not in ignore_nodes:
                    node_names.append(node_name)
                    Sbase[node_name] = data.sn_mva
                  
                    node = ElectricalNode(name=node_name,
                                          bc_type=['V', 'delta'],
                                          V=row['vm_pu'],
                                          delta=row['va_degree']*np.pi/180,
                                          scale_var=scale_var,
                                          scale_var_params=scale_var_params)
                    network.add_node(node)
                    
                    half_link = ElectricalHalfLink(name = '{}_slack'.format(node_name), start_node=node)
                    network.add_half_link(half_link)  
                else:
                    print("Slack node is not included in network. This can lead to an ill-posed system.")

        # PV node (P=-P, V=V)
        for index, row in data.gen.iterrows():
            if row['in_service']:
                node_name = data.bus.loc[row['bus'], 'name']
                
                if node_name not in node_names + ignore_nodes:
                    node_names.append(node_name)
                    Sbase[node_name] = row['sn_mva']
                    
                    node = ElectricalNode(name=node_name,
                                          V=row['vm_pu'],
                                          bc_type=['P', 'V'],
                                          scale_var=scale_var,
                                          scale_var_params=scale_var_params)
                    network.add_node(node)
                    
                    half_link = ElectricalHalfLink(name='{}_pv'.format(node_name), 
                                                   start_node=node,
                                                   P=-row['p_mw']/Sbase[node_name])
                    network.add_half_link(half_link) 

        # PQ node (static generator, P=-P, Q=-Q)
        for index, row in data.sgen.iterrows():
            if row['in_service']:
                node_name = data.bus.loc[row['bus'], 'name']
                
                if node_name not in node_names + ignore_nodes:
                    node_names.append(node_name)
                    Sbase[node_name] = row['sn_mva']
                    
                    node = ElectricalNode(name=node_name,
                                          bc_type=['P', 'Q'],
                                          scale_var=scale_var,
                                          scale_var_params=scale_var_params)
                    network.add_node(node)   
                    
                    half_link = ElectricalHalfLink(name='{}_sgen'.format(node_name), 
                                                   start_node=node,
                                                   P=-row['p_mw']/Sbase[node_name],
                                                   Q=-row['q_mvar']/Sbase[node_name])
                    network.add_half_link(half_link)  
                elif node_name in node_names:
                    half_link = ElectricalHalfLink(name='{}_sgen'.format(node_name), 
                                                   start_node=self.find_node(node_name, network, node_names),
                                                   P=-row['p_mw']/Sbase[node_name],
                                                   Q=-row['q_mvar']/Sbase[node_name])
                    network.add_half_link(half_link)

        # Load (PQ node)
        for index, row in data.load.iterrows():
            if row['in_service']:
                node_name = data.bus.loc[row['bus'], 'name']
                
                if node_name not in node_names + ignore_nodes:
                    node_names.append(node_name)
                    Sbase[node_name] = row['sn_mva']
                    
                    node = ElectricalNode(name=node_name,
                                          bc_type=['P', 'Q'],
                                          scale_var=scale_var,
                                          scale_var_params=scale_var_params)
                    network.add_node(node)   
                    
                    half_link = ElectricalHalfLink(name='{}_pq'.format(node_name), 
                                                   start_node=node,
                                                   P=row['p_mw']/Sbase[node_name],
                                                   Q=row['q_mvar']/Sbase[node_name])
                    network.add_half_link(half_link)  
                elif node_name in node_names:         
                    half_link = ElectricalHalfLink(name='{}_pq'.format(node_name), 
                                                   start_node=self.find_node(node_name, network, node_names),
                                                   P=row['p_mw']/Sbase[node_name],
                                                   Q=row['q_mvar']/Sbase[node_name])
                    network.add_half_link(half_link)
                    
        # Shunt (PQ Node, P=P, Q=-Q)
        for index, row in data.shunt.iterrows():
            if row['in_service']:
                node_name = data.bus.loc[row['bus'], 'name']
                
                if node_name not in node_names + ignore_nodes:
                    node_names.append(node_name)
                    Sbase[node_name] = data.sn_mva
                    
                    node = ElectricalNode(name=node_name,
                                          bc_type=['P', 'Q'],
                                          scale_var=scale_var,
                                          scale_var_params=scale_var_params)
                    network.add_node(node)
                    
                    P = row['p_mw']*row['step'] / Sbase[node_name]
                    Q = -row['q_mvar']*row['step'] / Sbase[node_name]
                                        
                    half_link = ElectricalHalfLink(name='{}_shunt'.format(node_name), 
                                                   start_node=node,
                                                   P=P,
                                                   Q=Q,
                                                   link_type='nodal_shunt',
                                                   link_params={'b_sh' : Q,
                                                                'g_sh' : P})
                    network.add_half_link(half_link)
                elif node_name in node_names:
                    P = row['p_mw']*row['step'] / Sbase[node_name]
                    Q = -row['q_mvar']*row['step'] / Sbase[node_name]
                                    
                    half_link = ElectricalHalfLink(name='{}_shunt'.format(node_name), 
                                                   start_node=self.find_node(node_name, network, node_names),
                                                   P=P,
                                                   Q=Q,
                                                   link_type='nodal_shunt',
                                                   link_params={'b_sh' : Q,
                                                                'g_sh' : P})
                    network.add_half_link(half_link)
                            
        # Junction (PQ Node, P=0, Q=0)
        for index, row in data.bus.iterrows():
            if row['in_service']:
                node_name = row['name']
                
                if node_name not in node_names + ignore_nodes:
                    node_names.append(node_name)
                    Sbase[node_name] = data.sn_mva
                    
                    node = ElectricalNode(name=node_name,
                                          bc_type=['P', 'Q'],
                                          scale_var=scale_var,
                                          scale_var_params=scale_var_params)
                    network.add_node(node)
                    
        # Line
        for index, row in data.line.iterrows():
            if row['in_service']:
                from_bus = data.bus.loc[row['from_bus'], 'name']
                to_bus = data.bus.loc[row['to_bus'], 'name']
                            
                if (row['from_bus'] not in ignore_nodes) and (row['to_bus'] not in ignore_nodes):
                    g, b, g_sh, b_sh = self.compute_admittance(c_nf_per_km=row['c_nf_per_km'],
                                                               f=f,
                                                               g_us_per_km=row['g_us_per_km'],
                                                               length_km=row['length_km'],
                                                               parallel=row['parallel'],
                                                               r_ohm_per_km=row['r_ohm_per_km'],
                                                               x_ohm_per_km=row['x_ohm_per_km'],
                                                               Sbase=Sbase[from_bus],
                                                               Vbase=data.bus.loc[row['from_bus']].vn_kv)
                                   
                    network.add_link(ElectricalLink(name="{}-{}".format(from_bus, to_bus),
                                                    start_node=self.find_node(from_bus, network, node_names),
                                                    end_node=self.find_node(to_bus, network, node_names),
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
                from_bus = data.bus.loc[row['hv_bus'], 'name']
                to_bus = data.bus.loc[row['lv_bus'], 'name']
                
                if (row['hv_bus'] not in ignore_nodes) and (row['lv_bus'] not in ignore_nodes):
                    g, b, g_sh, b_sh, ratio, phase_shift = self.compute_trafo(vn_hv_kv=row['vn_hv_kv'],
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
                                 
                    network.add_link(ElectricalLink(name="{}-{}".format(from_bus, to_bus),
                                                    start_node=self.find_node(from_bus, network, node_names),
                                                    end_node=self.find_node(to_bus, network, node_names),
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
                    
        return network, data