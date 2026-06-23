"""
Heterogeneous network base class, including Network, and Node.
"""
import numpy as np
import re

from meslf.load_flow.system_of_equations import NonLinearSystemHeterogeneous
from meslf.load_flow.non_linear_solvers import NR, AA, FP
from meslf.networks.network import Network, Node, Link, HalfLink
from meslf.networks.gas_network import GasNetwork, GasNode, GasLink, GasHalfLink
from meslf.networks.electrical_network import ElectricalNetwork, ElectricalNode, ElectricalLink, ElectricalHalfLink
from meslf.networks.heat_network import HeatNetwork, HeatNode, HeatLink, HeatHalfLink
from meslf.node_equations import coupling

# %% Network

class HeterogeneousNetwork(Network):
    """
    Overall heterogeneous network class. Subclass of Network.
    Only heterogeneous nodes can be added separately.

    Attributes
    ----------
    name : str
        The name of the network.
    nodes : list
        List of nodes in the network.
    links : list
        List of links in the network.
    half_links : list
        List of half links in the network.
    number_of_nodes : list
        Amount of node present in the network.
    number_of_links : list
        Amount of links present in the network.
    number_of_half_links : list
        Amount of half links present in the network.
    networks : list
        List of (sub)networks in the network.
    level : list
        List of names in the network.
    F_entries : list
        List of network elements corresponding to equations in the system.
    x_entries : list
        List of network elements corresponding to variables present in system of equations.
    x_c_entries : list
        List of network elements corresponding to variables present in system of equations related to heterogeneous network elements.
    x_e_entries : list
        List of network elements corresponding to variables present in system of equations related to electrical network elements.
    x_g_entries : list
        List of network elements corresponding to variables present in system of equations related to gas network elements.
    x_h_entries : list
        List of network elements corresponding to variables present in system of equations related to heat network elements.
    unknown_q_links : list
        List of links related to unknown mass flow of coupling element.
    unknown_P_links : list
        List of links related to unknown active power of coupling element.
    unknown_Q_links : list
        List of links related to unknown active power of coupling element.    
    unknown_m_links : list
        List of links related to unknown mass flow of coupling element.
    unknown_dphi_links : list
        List of links related to unknown heat power of coupling element.
    unknown_Ts_links : list
        List of links related to unknown supply temperature of coupling element.
    unknown_Tr_links : list
        List of links related to unknown return temperature of coupling element.
    unknown_q_halflinks : list
        List of half links related to unknown mass flow of coupling element.
    unknown_P_halflinks : list
        List of half links related to unknown active power of coupling element.
    unknown_Q_halflinks : list
        List of half links related to unknown active power of coupling element.    
    unknown_m_halflinks : list
        List of half links related to unknown mass flow of coupling element.
    unknown_dphi_halflinks : list
        List of half links related to unknown heat power of coupling element.
    unknown_Ts_halflinks : list
        List of half links related to unknown supply temperature of coupling element.
    unknown_Tr_halflinks : list
        List of half links related to unknown return temperature of coupling element.
    """

    def __init__(self, name):
        """
        Creates a HeatNetwork object.

        Parameters
        ----------
        name : str
            The name of the network.
        """
        super().__init__(name)
                
        self.x_entries = []
        self.x_c_entries = []
        self.x_e_entries = []
        self.x_g_entries = []
        self.x_h_entries = []
        
        self.known_dphi_nodes = []
        self.known_dT_nodes = []
        
        self.unknown_q_links = []
        self.unknown_P_links = []
        self.unknown_Q_links = []
        self.unknown_m_links = []
        self.unknown_dphi_links = []
        self.unknown_Ts_links = []
        self.unknown_Tr_links = []
        
        self.unknown_q_halflinks = []
        self.unknown_P_halflinks = []
        self.unknown_Q_halflinks = []
        self.unknown_m_halflinks = []
        self.unknown_dphi_halflinks = []
        self.unknown_Ts_halflinks = []
        self.unknown_Tr_halflinks = []
        
        self.F_c_nodes = []
        
        self.F_entries = []
        self.F_c_entries = []
        self.F_e_entries = []
        self.F_g_entries = []
        self.F_h_entries = []
        
        self.unit_types = ['dummy', 
                           'gas_fired_generator', 
                           'p2g',
                           'gas_fired_generator_valve_point', 
                           'gas_boiler',
                           'gas_boiler_part_load', 
                           'electrical_boiler', 
                           'chp',
                           'chp_part_load', 
                           'electrolyser',
                           'eh']
               
        self.unit_types_heat = ['gas_boiler', 
                                'gas_boiler_part_load',
                                'electrical_boiler', 
                                'chp', 
                                'chp_part_load', 
                                'electrolyser', 
                                'electrolyser_ratio', 
                                'eh']
        

    def get_nodes(self, bc_types=[], unit_types=[], carriers=[]):
        """
        Iterates over all the nodes in the list of nodes, with the specified node type.

        Parameters
        ----------
        bc_types : list, optional
            List of node type of the nodes to be yielded. If empty, all the nodes are yielded. 
            Default is an empty list.
        unit_type : list, optional
            List of unit types of the heterogeneous nodes to be yielded. 
            If empty, all the nodes are yielded. Default is an empty list.
        carriers : list, optional
            List of carriers of the nodes to be yielded. 
            If empty, all the nodes are yielded. 
            Carriers are: 
            - 'c', 
            - 'e', 
            - 'g',
            - 'h'.

        Yields
        ------
        node : Node
            The next Node instance in self.nodes.
        """                
        if carriers and unit_types:
            for node in super().get_nodes(bc_types=bc_types):
                if 'g' in carriers:              
                    if isinstance(node, GasNode):
                        if node.unit_type in unit_types:
                            yield node
                if 'e' in carriers:
                    if isinstance(node, ElectricalNode):
                        yield node    
                if 'h' in carriers:
                    if isinstance(node, HeatNode):
                        yield node  
                if 'c' in carriers:
                    if isinstance(node, HeterogeneousNode):
                        yield node      
        elif carriers:
            for node in super().get_nodes(bc_types=bc_types):
                if 'g' in carriers:              
                    if isinstance(node, GasNode):
                        yield node
                if 'e' in carriers:
                    if isinstance(node, ElectricalNode):
                        yield node     
                if 'h' in carriers:
                    if isinstance(node, HeatNode):
                        yield node  
                if 'c' in carriers:
                    if isinstance(node, HeterogeneousNode):
                        yield node
        elif unit_types:
            for node in super().get_nodes(bc_types=bc_types):
                if isinstance(node, HeterogeneousNode):
                    if node.unit_type in unit_types:
                        yield node
        else:
            for node in super().get_nodes(bc_types=bc_types):
                yield node


    def get_networks(self, carriers=[]):
        """
        Iterates over all the networks in the list of networks of the specified carrier.

        Parameters
        ----------
        carriers : list, optional
            List of carriers of the subnetworks to be yielded. If empty, all the subnetworks are yielded. 
            Carriers are:
            - 'c', 
            - 'e', 
            - 'g',
            - 'h'.
        get_all : boolean, optional
            Specify if the subsubnetworks etc. should also be returned. 
            If False, only the subnetworks are returned. 
            If True, all the subnetworks of all the subnetwork etc. are returned. 
            Default is False.

        Yields
        ------
        network : Network
            The next Network instance in self.networks.
        """
        if carriers:
            for network in super().get_networks():
                if 'g' in carriers and isinstance(network, GasNetwork):
                    yield network
                elif 'e' in carriers and isinstance(network, ElectricalNetwork):
                    yield network
                elif 'h' in carriers and isinstance(network, HeatNetwork):
                    yield network
                elif 'c' in carriers and isinstance(network, HeterogeneousNetwork):
                    yield network
        else:
            for network in super().get_networks():
                yield network


    def initialize(self):
        """
        Initializes the network.
        """
        for network in self.get_networks():
            network.initialize()
            
        self.set_F_entries()
        self.set_x_entries()
            
            
    def set_x_entries(self):
        """
        Creates all the nodes, links, and half links that have an entry in variable vector x.

        Returns
        -------
        x_entries : list
           List of all the nodes, links, and half links that contribute to x.
        """
        x_index_offset = 0
        
        for network in self.get_networks():
            if not isinstance(network, HeterogeneousNetwork):
                network.x_start_index = x_index_offset
                x_index_offset += len(network.x_entries)
                network.x_end_index = x_index_offset
            
            if isinstance(network, GasNetwork):
                self.x_g_entries += network.x_entries
                
                for link in network.get_links(link_types=['dummy']):
                    if isinstance(link.start_node, HeterogeneousNode) or isinstance(link.end_node, HeterogeneousNode):
                        if 'q' not in link.bc_type:
                            self.unknown_q_links.append(link)                                     
            elif isinstance(network, ElectricalNetwork):
                self.x_e_entries += network.x_entries
                
                for link in network.get_links(link_types=['dummy']):
                    if isinstance(link.start_node, HeterogeneousNode) or isinstance(link.end_node, HeterogeneousNode):
                        if ('P_start' not in link.bc_type) and ('P_end' not in link.bc_type):
                            self.unknown_P_links.append(link)
                            
                        if ('Q_start' not in link.bc_type) and ('Q_end' not in link.bc_type):
                            self.unknown_Q_links.append(link)
            elif isinstance(network, HeatNetwork):
                self.x_h_entries += network.x_entries
                
                for link in network.get_links(link_types=['dummy']):
                    if isinstance(link.start_node, HeterogeneousNode) or isinstance(link.end_node, HeterogeneousNode):
                        if 'm' not in link.bc_type:
                            self.unknown_m_links.append(link)
                            
                        if 'dphi' not in link.bc_type:
                            self.unknown_dphi_links.append(link)
                            
                        if 'Ts' not in link.bc_type:
                            self.unknown_Ts_links.append(link)
                            
                        if 'Tr' not in link.bc_type:
                            self.unknown_Tr_links.append(link)
            elif isinstance(network, HeterogeneousNetwork):
                for node in network.get_nodes():
                    for hl in node.get_half_links():
                        if isinstance(hl, GasHalfLink):
                            if 'q' not in hl.bc_type:
                                self.unknown_q_halflinks.append(hl)
                        elif isinstance(hl, ElectricalHalfLink):
                            if 'P' not in hl.bc_type:
                                self.unknown_P_halflinks.append(hl)
                                
                            if 'Q' not in hl.bc_type:
                                self.unknown_Q_halflinks.append(hl)
                        elif isinstance(hl, HeatHalfLink):
                            if 'm' not in hl.bc_type:
                                self.unknown_m_halflinks.append(hl)
                                
                            if 'dphi' not in hl.bc_type:
                                self.unknown_dphi_halflinks.append(hl)
                                
                            if 'Ts' not in hl.bc_type:
                                self.unknown_Ts_halflinks.append(hl)
                                
                            if 'Tr' not in hl.bc_type:
                                self.unknown_Tr_halflinks.append(hl)

        self.x_c_entries = self.unknown_q_links + self.unknown_q_halflinks + \
                           self.unknown_P_links + self.unknown_P_halflinks + \
                           self.unknown_Q_links + self.unknown_Q_halflinks + \
                           self.unknown_m_links + self.unknown_m_halflinks + \
                           self.unknown_dphi_links + self.unknown_dphi_halflinks + \
                           self.unknown_Ts_links + self.unknown_Ts_halflinks + \
                           self.unknown_Tr_links + self.unknown_Tr_halflinks
                           
        self.x_start_index = x_index_offset
        x_index_offset += len(self.x_c_entries)
        self.x_end_index = x_index_offset
                           
        self.x_entries = self.x_g_entries + self.x_e_entries + self.x_h_entries + self.x_c_entries


    def set_F_entries(self):
        """
        Returns all the nodes, links, and half links that have an entry in function vector F.

        Returns
        -------
        F_entries : list
           List of all the nodes, links, and half links that contribute to F.
        """
        F_index_offset = 0
         
        for network in self.get_networks():
            if not isinstance(network, HeterogeneousNetwork):
                network.F_start_index = F_index_offset
                F_index_offset += len(network.F_entries)
                network.F_end_index = F_index_offset     
            
            if isinstance(network, GasNetwork):
                self.F_g_entries += network.F_entries
            elif isinstance(network, ElectricalNetwork):
                self.F_e_entries += network.F_entries
            elif isinstance(network, HeatNetwork):
                self.F_h_entries += network.F_entries
        
        # 1.) Heterogenous nodes with equations        
        # 2.) Heterogeneous coupling node, where heat is involved, 
        # and where there is a heat (dummy) link connected to the heterogeneous node, 
        # such that a Tr of Ts is available.
        # 3.) Heterogeneous coupling node, where heat is involved, 
        # and where delta T is specified instead of Tr or Ts.
        for node in self.get_nodes(carriers=['c']):
            if node.unit_type not in {'dummy'}:
                self.F_c_nodes.append(node)
            
            if ('Tr' in node.bc_type) or ('Ts' in node.bc_type):
                for link in node.get_links():
                    if isinstance(link, HeatLink) or isinstance(link, HeatHalfLink):
                        self.known_dphi_nodes.append(node)
                        break

            if 'dT' in node.bc_type:       
                self.known_dT_nodes.append(node)
        
        self.F_c_entries = self.F_c_nodes + self.known_dphi_nodes + self.known_dT_nodes
        
        self.F_start_index = F_index_offset
        F_index_offset += len(self.F_c_entries)
        self.F_end_index = F_index_offset
        
        self.F_entries = self.F_g_entries + self.F_e_entries + self.F_h_entries + self.F_c_entries


    def get_x_entries(self):
        """
        Nodes, links and half links that contribute to relevant unknown variables.
        
        Yield
        -----
        element : list
            The next network element instance in self.x_entries.
        """
        for element in self.x_entries:
            if element is not None:
                yield element
        
        
    def get_F_entries(self):
        """
        Nodes, links and half links that contribute to the system of equations.

        Yields
        ------
        element : network element
            The next network element instance in self.F_entries.
        """
        for element in self.F_entries:
            if element is not None:
                yield element


    def set_x_init(self):
        """
        Creates the initial gues based on the current network parameters.

        Returns
        -------
        x_init : np array
           Initial guess for variable vector x.
        """
        x_init = np.zeros(len(self.x_entries))
        
        # homogeneous part
        for network in self.get_networks():
            if not isinstance(network, HeterogeneousNetwork):
                x_init[network.x_start_index:network.x_end_index] = network.set_x_init()
        index_offset = len(self.x_g_entries)+len(self.x_e_entries)+len(self.x_h_entries)
        
        # coupling gas part
        for i, link in enumerate(self.unknown_q_links):
            x_init[i+index_offset] = link.get_q()
        ind_offset += len(self.unknown_q_links)
        
        for i, link in enumerate(self.unknown_q_halflinks):
            x_init[i+index_offset] = -link.get_q() # minus based on how q is defined / used for the dummy links
        index_offset += len(self.unknown_q_halflinks)
        
        # coupling electricity part
        for i, link in enumerate(self.unknown_P_links):
            x_init[i+index_offset] = link.get_P_start()
        index_offset += len(self.unknown_P_links)
        
        for i, link in enumerate(self.unknown_P_halflinks):
            x_init[i+index_offset] = link.get_P()
        index_offset += len(self.unknown_P_halflinks)
        
        for i, link in enumerate(self.unknown_Q_links):
            x_init[i+index_offset] = link.get_Q_start()
        index_offset += len(self.unknown_Q_links)
        
        for i, link in enumerate(self.unknown_Q_halflinks):
            x_init[i+index_offset] = link.get_Q()
        index_offset += len(self.unknown_Q_halflinks)
        
        # coupling heat part
        for i, link in enumerate(self.unknown_m_links):
            x_init[i+index_offset] = link.get_m()
        index_offset += len(self.unknown_m_links)
        
        for i, link in enumerate(self.unknown_m_halflinks):
            x_init[i+index_offset] = -link.get_m()
        index_offset += len(self.unknown_m_halflinks)
        
        for i, link in enumerate(self.unknown_dphi_links):
            x_init[i+index_offset] = -link.get_dphi_start()
        index_offset += len(self.unknown_dphi_links)
        
        for i, link in enumerate(self.unknown_dphi_halflinks):
            x_init[i+index_offset] = -link.get_dphi()
        index_offset += len(self.unknown_dphi_halflinks)
        
        for i, link in enumerate(self.unknown_Ts_links):
            x_init[i+index_offset] = link.get_Ts_start()
        index_offset += len(self.unknown_Ts_links)
        
        for i, link in enumerate(self.unknown_Ts_halflinks):
            x_init[i+index_offset] = link.get_Ts()
        index_offset += len(self.unknown_Ts_halflinks)
        
        for i, link in enumerate(self.unknown_Tr_links):
            x_init[i+index_offset] = link.get_Tr_start()
        index_offset += len(self.unknown_Tr_links)
        
        for i, link in enumerate(self.unknown_Tr_halflinks):
            x_init[i+index_offset] = link.get_Tr()
        
        return x_init
   

    def update(self, x):
        """
        Updates the network given variable vector x.

        Parameters
        ----------
        x : np array
            Variable vector x, scaled.
        """         
        # homogeneous parts
        for network in self.get_networks():
            if not isinstance(network, HeterogeneousNetwork):
                network.update(x[network.x_start_index:network.x_end_index])
        
        # heterogeneous gas part
        index_offset = len(self.x_g_entries) + len(self.x_e_entries) + len(self.x_h_entries)
        for i, link in enumerate(self.unknown_q_links):
            link.q = x[i+index_offset]
            if link.scale_var == 'per_unit':
                link.q *= link.scale_var_params['qbase']
            
        index_offset += len(self.unknown_q_links)
        for i, hl in enumerate(self.unknown_q_halflinks):
            hl.q = -x[i+index_offset] # minus based on how q is defined / used for the dummy links
            if hl.scale_var == 'per_unit':
                hl.q *= hl.scale_var_params['qbase']

        # heterogeneous electricity part
        index_offset += len(self.unknown_q_halflinks)
        for i, link in enumerate(self.unknown_P_links):
            P = x[i+index_offset]
            if link.scale_var == 'per_unit':
                P *= link.scale_var_params['Sbase']
            link.P_start = P
            link.P_end = -P
 
        index_offset += len(self.unknown_P_links)
        for i, hl in enumerate(self.unknown_P_halflinks):
            hl.P = x[i+index_offset]
            if self.scale_var == 'per_unit':
                hl.P *= self.scale_var_params['Sbase']
                
        index_offset += len(self.unknown_P_halflinks)
        for i, link in enumerate(self.unknown_Q_links):
            Q = x[i+index_offset]
            if link.scale_var == 'per_unit':
                Q *= link.scale_var_params['Sbase']
            link.Q_start = Q
            link.Q_end = -Q
            
        index_offset += len(self.unknown_Q_links)
        for i, hl in enumerate(self.unknown_Q_halflinks):
            hl.Q = x[i+index_offset]
            if hl.scale_var == 'per_unit':
                hl.Q *= hl.scale_var_params['Sbase']
                
        # heterogeneous heat part
        index_offset += len(self.unknown_Q_halflinks)
        for i, link in enumerate(self.unknown_m_links):
            link.m = x[i+index_offset]
            if link.m >= 0:
                if link.scale_var == 'per_unit':
                    link.m *= link.scale_var_params['qbase']
            else:
                print('Update(x) encountered a heat link with heterogeneous start node and negative flow. Flow is set to 1e-6.')

                x[i+index_offset] = 1e-6
                link.m = x[i+index_offset]
                
        index_offset += len(self.unknown_m_links)
        for hl in self.unknown_m_halflinks:
            m = -x[i+index_offset]
            if hl.scale_var == 'per_unit':
                m *= hl.scale_var_params['qbase']
            hl.m = m
        
        index_offset += len(self.unknown_m_halflinks)
        for i, link in enumerate(self.unknown_dphi_links):
            phi = x[i+index_offset]
            if link.scale_var == 'per_unit':
                phi *= link.scale_var_params['phibase']
            if phi < 0:
                print('Update(x) encountered a negative valued coupling heat power. But all coupling components should produce heat.')
            elif phi == 0:
                print('Update(x) encountered a zero valued coupling heat power. But all coupling components should produce heat.')
            link.dphi_start = -phi
        
        index_offset += len(self.unknown_dphi_links)
        for i, hl in enumerate(self.unknown_dphi_halflinks):
            phi = x[i+index_offset]
            if hl.scale_var == 'per_unit':
                phi *= hl.scale_var_params['phibase']
            if phi < 0:
                print('Update(x) encountered a negative valued coupling heat power. But all coupling components should produce heat.')
            elif phi == 0:
                print('Update(x) encountered a zero valued coupling heat power. But all coupling components should produce heat.')
            hl.dphi = -phi
            
        index_offset += len(self.unknown_dphi_halflinks)
        for i, link in enumerate(self.unknown_Ts_links):
            link.Ts_start = x[i+index_offset]
            if link.scale_var == 'per_unit':
                link.Ts_start *= link.scale_var_params['Tbase']
            
        index_offset += len(self.unknown_Ts_links)
        for i, hl in enumerate(self.unknown_Ts_halflinks):
            hl.Ts = x[i+index_offset]
            if hl.scale_var == 'per_unit':
                hl.Ts *= hl.scale_var_params['Tbase']

        index_offset += len(self.unknown_Ts_halflinks)
        for i, link in enumerate(self.unknown_Tr_links):
            link.Tr_start = x[i+index_offset]
            if link.scale_var == 'per_unit':
                link.Tr_start *= link.scale_var_params['Tbase']
        
        index_offset += len(self.unknown_Tr_links)
        for i, hl in enumerate(self.unknown_Tr_halflinks):
            hl.Tr = x[i+index_offset]
            if hl.scale_var == 'per_unit':
                hl.Tr *= hl.scale_var_params['Tbase']

        index_offset += len(self.unknown_Tr_halflinks)
        # update other (half) link temperatures
        # nodes where heat is or might be involved
        for i, node in enumerate(self.get_nodes(unit_types=self.unit_types_heat)):
            for hl in node.get_half_links(carriers=['h']):
                if hl.sink:  # sinks
                    # dT known (Ts is assumed known, or updated before)
                    if ('dT' in hl.bc_type) and (hl not in self.unknown_Tr_halflinks) and (hl not in self.unknown_Tr_halflinks):
                        hl.Tr = hl.Ts - hl.dT
                elif hl.source:  # sources
                    # dT known (Tr is assumed known, or updated before)
                    if ('dT' in hl.bc_type) and (hl not in self.unknown_Ts_halflinks) and (hl not in self.unknown_Ts_halflinks):
                        hl.Ts = hl.dT + hl.Tr
        
        heat_coupling_links = [link for link in self.get_links(link_types=['dummy']) if (isinstance(link, HeatLink) and (
            isinstance(link.start_node, HeterogeneousNode) or isinstance(link.end_node, HeterogeneousNode)))]
        for i, link in enumerate(heat_coupling_links):
            if isinstance(link.start_node, HeterogeneousNode):
                if 'dphi' in link.bc_type:  # coupling acts as sink
                    raise NotImplementedError('Updating heat dummy link for which the coupling acts as a sink not implemented.')
                else:  # coupling acts as source. Ts is either known, or part is unknown_Ts_links, such that it is already updated
                    if link.m >= 0:  # mass flow in correct direction for a source
                        link.Tr_end = link.end_node.Tr
                        link.Tr_start = link.return_temperature_start()
                        link.Ts_end = link.supply_temperature_end()
                        if link.scale_var == 'per_unit':
                            link.Tr_start *= link.scale_var_params['Tbase']
                            link.Ts_end *= link.scale_var_params['Tbase']
                    else:
                        raise NotImplementedError('Updating encountered heat dummy link which is a source, but acts like a sink.')
            else:
                raise NotImplementedError('Update not implemented for a heat link with heterogeneous end node.')


    def update_full(self):
        """
        Updates the full network given variable vector x.
        Unlike update(x), not only the values from x are updated, 
        but also all parameters not included in x.

        Parameters
        ----------
        x : np array
            Variable vector x, scaled.

        Returns
        -------
        p_g : np array
            Array with all unscaled nodal pressures in the gas network.
        q : np array
            Array with all unscaled gas link flows.
        q_inj : np array
            Array with all unscaled nodal injeted gas flows.
        delta : np array
            Array with all unscaled nodal voltage angles.
        V : np array
            Array with all unscaled nodal voltage amplitudes.
        S_inj : np array
            Array with all unscaled injected complex powers.
        P_link : np array
            Array with all unscaled link active powers.
        Q_link : np array
            Array with all unscaled link reactive powers.
        m : np array
            Array with all unscaled heat link flows.
        p_h : np array
            Array with all unscaled nodal pressures in the heat network.
        Ts : np array
            Array with all unscaled nodal supply temperatures.
        Tr : np array
            Array with all unscaled nodal return temperatures.
        m_hl : list
            List of arrays with all unscaled  half link flows per node.
        phi_hl : list
            List of array with all unscaled half link heat powers per node.
        Ts_hl : list
            List of array with all unscaled half link supply temperatures per node.
        Tr_hl : list
            List of array with all unscaled half link return temperatures per node.
        q_c : np array
            Array with all unscaled coupling gas link flows.
        P_c : np array
            Array with all unscaled coupling electrical link active powers.
        Q_c : np array
            Array with all unscaled coupling electrical link reactive powers.
        m_c : np array
            Array with all unscaled coupling heat link flows.
        dphi_c : np array
            Array with all unscaled coupling half link heat power.
        Ts_c : np array
            Array with all unscaled coupling half link supply temperatures.
        Tr_c : np array
            Array with all unscaled coupling half link return temperatures.
        """
        # homogeneous parts
        p_g = np.array([])
        q = np.array([])
        q_inj = np.array([])
        delta = np.array([])
        V_mag = np.array([])
        S_inj = np.array([])
        P_link = np.array([])
        Q_link = np.array([])
        m = np.array([])
        p_h = np.array([])
        Ts = np.array([])
        Tr = np.array([])
        m_hl = np.array([])
        phi_hl = np.array([])
        Ts_hl = np.array([])
        Tr_hl = np.array([])

        for network in self.get_networks():
            if isinstance(network, GasNetwork):
                p_g, q, q_inj = network.update_full()
            elif isinstance(network, ElectricalNetwork):
                delta, V_mag, S_inj, P_link, Q_link = network.update_full()
            elif isinstance(network, HeatNetwork):
                m, p_h, Ts, Tr, m_hl, phi_hl, Ts_hl, Tr_hl = network.update_full()

        # heterogeneous part
        q_c = []
        P_c = []
        Q_c = []
        m_c = []
        dphi_c = []
        Ts_c = []
        Tr_c = []

        for node in self.get_nodes(carriers=['c']):
            for link in node.get_links():
                if isinstance(link, GasLink) or isinstance(link, GasHalfLink):
                    q_c.append(link.q)
                elif isinstance(link, ElectricalLink):
                    P_c.append(link.P_start)
                    Q_c.append(link.Q_start)
                elif isinstance(link, ElectricalHalfLink):
                    P_c.append(link.P)
                    Q_c.append(link.Q)
                elif isinstance(link, HeatLink):
                    m_c.append(link.m)
                    dphi_c.append(-link.dphi_start)
                    Ts_c.append(link.Ts_start)
                    Tr_c.append(link.Tr_start)
                elif isinstance(link, HeatHalfLink):
                    m_c.append(-link.m)
                    dphi_c.append(-link.dphi)
                    Ts_c.append(link.Ts)
                    Tr_c.append(link.Tr)
                    
        q_c = np.array(q_c)
        P_c = np.array(P_c)
        Q_c = np.array(Q_c)
        m_c = np.array(m_c)
        dphi_c = np.array(dphi_c)
        Ts_c = np.array(Ts_c)
        Tr_c = np.array(Tr_c)
        
        return p_g, q, q_inj, \
               delta, V_mag, S_inj, P_link, Q_link, \
               m, p_h, Ts, Tr, m_hl, phi_hl, Ts_hl, Tr_hl, \
               q_c, P_c, Q_c, m_c, dphi_c, Ts_c, Tr_c


    def reset_network(self, x):
        """
        Resets the full network to a vector x.

        Parameters
        ----------
        x_init : np array
            Vector with initial guess for x.
        """
        for network in self.get_networks():
            if isinstance(network, GasNetwork):
                x_network = x[self.g_indices]
            elif isinstance(network, ElectricalNetwork):
                x_network = x[self.e_indices]
            elif isinstance(network, HeatNetwork):
                x_network = x[self.h_indices]
            elif isinstance(network, HeterogeneousNetwork):
                x_network = x[self.c_indices]
                
            network.reset_network(x_network)
        
        self.update_full(x)


    def solve_network(self, x_init, solver='nr', solver_parameters={}, lin_solver='lu', lin_solver_parameters={}, post_processing=False, bounded=False):
        """
        Solves the steady-state load flow problem for the network.

        Parameters
        ----------
        x_init : array like
            Scaled initial guess.
        solver : string
            Solver used. Default is standard NR. Options are 'nr', 'aa' and 'fp'.

        Returns
        -------
        x_sol : np array
            Solution vector x, scaled.
        iterations : int
            Number of iterations used.
        errors : list
            List with the error for each iteration.
        p_g : np array
            Array with all unscaled nodal pressures in the gas network.
        q : np array
            Array with all unscaled gas link flows.
        q_inj : np array
            Array with all unscaled nodal injeted gas flows.
        delta : np array
            Array with all unscaled nodal voltage angles.
        V : np array
            Array with all unscaled nodal voltage amplitudes.
        S_inj : np array
            Array with all unscaled injected complex powers.
        P_link : np array
            Array with all unscaled link active powers.
        Q_link : np array
            Array with all unscaled link reactive powers.
        m : np array
            Array with all unscaled heat link flows.
        p_h : np array
            Array with all unscaled nodal pressures in the heat network.
        Ts : np array
            Array with all unscaled nodal supply temperatures.
        Tr : np array
            Array with all unscaled nodal return temperatures.
        m_hl : list
            List of arrays with all unscaled  half link flows per node.
        phi_hl : list
            List of array with all unscaled half link heat powers per node.
        Ts_hl : list
            List of array with all unscaled half link supply temperatures per node.
        Tr_hl : list
            List of array with all unscaled half link return temperatures per node.
        q_c : np array
            Array with all unscaled coupling gas link flows.
        P_c : np array
            Array with all unscaled coupling electrical link active powers.
        Q_c : np array
            Array with all unscaled coupling electrical link reactive powers.
        m_c : np array
            Array with all unscaled coupling heat link flows.
        dphi_c : np array
            Array with all unscaled coupling half link heat power.
        Ts_c : np array
            Array with all unscaled coupling half link supply temperatures.
        Tr_c : np array
            Array with all unscaled coupling half link return temperatures.
        """                
        # solver
        if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
            self.solver = NR(tol=solver_parameters['tol'])
        elif re.fullmatch(r'aa', solver, flags=re.IGNORECASE):
            self.solver = AA(tol=solver_parameters['tol'])
        elif re.fullmatch(r'fp', solver, flags=re.IGNORECASE):
            self.solver = FP(tol=solver_parameters['tol'])

        x_sol = self.solver.solve(network=self,
                                  nlsys=NonLinearSystemHeterogeneous(self),
                                  x_init=x_init,
                                  solver_parameters=solver_parameters,
                                  lin_solver=lin_solver,
                                  lin_solver_parameters=lin_solver_parameters,
                                  post_processing=post_processing,
                                  bounded=bounded)
        
        if lin_solver_parameters['get_condition_number']:
            self.sv = self.solver.sv
            
        if lin_solver_parameters['get_initial']:
            self.J_init = self.solver.J_init
            self.lu_init = self.solver.lu_init

        # update the rest of the network
        p_g, q, q_inj, \
        delta, V, S_inj, P_link, Q_link, \
        m, p_h, Ts, Tr, m_hl, phi_hl, Ts_hl, Tr_hl, \
        q_c, P_c, Q_c, m_c, dphi_c, Ts_c, Tr_c = self.update_full()
        
        return x_sol, self.solver.iterations, self.solver.errors, \
               p_g, q, q_inj, \
               delta, V, S_inj, P_link, Q_link, \
               m, p_h, Ts, Tr, m_hl, phi_hl, Ts_hl, Tr_hl, \
               q_c, P_c, Q_c, m_c, dphi_c, Ts_c, Tr_c
                
# %% Node

class HeterogeneousNode(Node):
    """
    Heterogeneous node class.

    Attributes
    ----------
    name : str
        The name of the node.
    out_links : list
        List of outgoing links and half links connected to the node.
    in_links : list
        List of ingoing links and half links connected to the node.
    half_links : list
        List of half links connected to the node.
    number : int
        Number of the node.
    bc_type : list
        A list that specifies which variables are known.
    unit_type : str, optional
        Type of the conversion unit, which determines the node law(s).
    unit_params : dict, optional
        Dictionary with parameters needed for the node law of a specific node type. 
    """

    def __init__(self, name, scale_var=None, scale_var_params={}, bc_type=[], unit_type='dummy', unit_params={}, bounded=False):
        """
        Creates an HeatNode object.

        Parameters
        ----------
        name : str
            Name of the node.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.
        bc_type : int, optional
            A list that specifies which variables are known. Default is an empty list.
            Hence every variable is unknown.
        unit_type : str, optional
            Type of the node, which determines the node law(s). Default is 'dummy'. 
            Options are 
            - 'dummy', 
            - 'p2g'
            - 'gas_fired_generator'.
        unit_params : dict, optional
            Dictionary with parameters needed for the node law of a specific node type. Default is an empty dict.

        Raises
        ------
        ValueError
            If the unit_type is not a valid unit type.
        """
        super().__init__(name=name, scale_var=scale_var, scale_var_params=scale_var_params)
        
        self.bc_type = bc_type
        
        self.unit_type = unit_type
        self.unit_params = unit_params
        
        if unit_type == 'dummy':
            self.equation = coupling.dummy
        elif unit_type == 'gas_fired_generator':
            self.equation = coupling.gas_fired_generator
        elif unit_type == 'p2g':
            self.equation = coupling.p2g
        else:
            raise ValueError("unit_type '{}' is not a valid unit type.".format(unit_type))
        
        self.bounded = bounded
        
        self.f, self.df_dE = self.equation(unit_params=unit_params)


    def set_type(self, scale_var=None, scale_var_params=None, bc_type=None, unit_type=None, unit_params=None, bounded=None):
        """
        Set or change the node unit type, and the corresponding node equations.

        Parameters
        ----------
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.
        unit_type : str
            (New) type of the node, which determines the node law(s). 
            Must be 
            - 'dummy', 
            - 'p2g'
            - 'gas_fired_generator'.
        unit_params : dict
            Dictionary with parameters needed for the node law of a specific node type.

        Raises
        ------
        ValueError
            If the unit_type is not a valid unit type.
        """
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        if bc_type is not None:
            self.bc_type = bc_type
            
        if unit_type is not None:
            self.unit_type = unit_type
        if unit_params is not None:
            self.unit_params = unit_params
           
        if unit_type == 'dummy':
            self.equation = coupling.dummy
        elif unit_type == 'gas_fired_generator':
            self.equation = coupling.gas_fired_generator
        elif unit_type == 'p2g':
            self.equation = coupling.p2g
        else:
            raise ValueError("unit_type '{}' is not a valid unit type.".format(unit_type))
        
        if bounded is not None:
            self.bounded = bounded
        
        self.f, self.df_dE = self.equation(unit_params=unit_params)
        

    def get_half_links(self, bc_types=[], carriers=[], link_types=[]):
        """
        Iterates over all the half links connected to the node.

        Parameters
        ----------
        bc_types : list, optional
            List of bc types of the links to be yielded. 
            If empty, all the links are yielded. Default is an empty list.
        carriers : list, optional
            List of carriers of the halflinks to be yielded. 
            If empty, all the halflinks are yielded. 
            Carriers are, 
            - 'e', 
            - 'g',
            - 'h.'
        link_types : list, optional
            List of link types of the links to be yielded. 
            If empty, all the links are yielded. Default is an empty list.

        Yields
        ------
        hl : HalfLink
            The next HalfLink instance in self.half_links.
        """
        if carriers:
            for hl in super().get_half_links(link_types=link_types, bc_types=bc_types):
                if 'g' in carriers and isinstance(hl, GasHalfLink):
                    yield hl
                elif 'e' in carriers and isinstance(hl, ElectricalHalfLink):
                    yield hl
                elif 'h' in carriers and isinstance(hl, HeatHalfLink):
                    yield hl
        else:
            for hl in super().get_half_links(link_types=link_types, bc_types=bc_types):
                yield hl


    def get_p(self):
        return None


    def get_E_out(self):
        """
        Determine the energies (per carrier) on the outgoing links.

        Returns
        -------
        E_out : np array
            Outgoing energies.
        """
        gas = []
        active_power = []
        
        for link in self.get_out_links():
            if isinstance(link, GasLink):                   
                gas.append(link.q)
            elif isinstance(link, ElectricalLink):
                active_power.append(link.P_start)
                    
        return np.array(gas), np.array(active_power)


    def get_E_in(self):
        """
        Collect the carrier values of the incoming links, which are mass flow q and active power P.
        NB. Assumption is that there is no incoming heat power.

        Returns
        -------
        q, P : np array
            Incoming energies.
        """
        gas = []
        active_power = []
        
        for link in self.get_in_links():
            if isinstance(link, GasLink):
                gas.append(link.q)
            elif isinstance(link, ElectricalLink):
                active_power.append(link.P_start)
                                
        return np.array(gas), np.array(active_power)


    def node_law(self):
        """
        Node law for a heterogeneous node.
        The node law is determined by the unit type.

        Returns
        -------
        f : float
            The sum of all incoming and outgoing energies.
        """
        return self.f(self.get_E_in(), self.get_E_out(), scale_var=self.scale_var, scale_var_params=self.scale_var_params, bounded=self.bounded)


    def dnode_law_dE(self):
        """
        Derivative of the node law to all energy carriers.

        Returns
        -------
        df_dE : np array
            Derivative of the node law to all energy carriers: [df/dq df/dP].
        """
        return self.df_dE(self.get_E_in(), self.get_E_out(), scale_var=self.scale_var, scale_var_params=self.scale_var_params, bounded=self.bounded)