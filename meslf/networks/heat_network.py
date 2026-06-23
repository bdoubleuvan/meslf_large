"""
Heat network base class, including Network, Node, and Link.
"""
from meslf.networks.network import Network, Node, Link, HalfLink
from meslf.link_equations import hydraulic, thermal
import meslf.half_link_equations.thermal as halflink_thermal
from meslf.load_flow.system_of_equations import NonLinearSystemHeat
from meslf.load_flow.non_linear_solvers import NR, AA, FP

import numpy as np
import re
import scipy.sparse as sps

# %% Network

class HeatNetwork(Network):
    """
    Overall heat network class. Subclass of Network.
    """
    
    def __init__(self, name, formulation):
        """
        Creates a HeatNetwork object.

        Parameters
        ----------
        name : str
            The name of the network.
        """
        super().__init__(name)
        
        self.A = None
        self.Ad = None
        
        self.formulation = formulation


    def add_node(self, node, position=None):
        """
        Adds a node to the network. A node is only added if it is a HeatNode.

        Parameters
        ----------
        node : HeatNode
            Node object to be added to the network.
        position : integer, optional
            Position (index) in the list of nodes of the network where the node should be inserted. 
            Default is insert at end of list (append).
        """
        if isinstance(node, HeatNode):
            super().add_node(node, position=position)


    def add_link(self, link, position=None):
        """
        Adds link to the network.
        A link can only added if it is a HeatLink.
        If the start node or the end node are not yet added to the network, they
        will be added to the list of nodes.

        Parameters
        ----------
        link : HeatLink
            Link object to be added to the network.

        Raises
        ------
        TypeError
            If link is not an instance of HeatLink.
        """
        if not isinstance(link, HeatLink):
            raise TypeError("Only a HeatLink object can be added.")
        else:
            super().add_link(link, position=position)


    def add_half_link(self, half_link, position=None):
        """
        Adds half_link to the network.
        A half link can only added if it a HeatHalfLink.

        If the start node is not yet added to the network, 
        it will be added to the list of nodes.

        Parameters
        ----------
        half_link : HeatHalfLink
            Half link object to be added to the network.

        Raises
        ------
        TypeError
            If half_link is not an instance of HeatHalfLink.
        """
        if not isinstance(half_link, HeatHalfLink):
            raise TypeError("Only a HeatHalfLink object can be added.")
        else:
            super().add_half_link(half_link, position=position)


    def get_half_links(self, link_types=[], bc_types=[]):
        """
        Iterates over all the half links in the list of links, 
        with the specified link type or a specified boundary condition.

        Parameters
        ----------
        link_types : list, optional
            List of link types of the halflinks to be yielded. 
            If empty, all the halflinks are yielded. Default is an empty list.
        bc_types : list, optional
            List of boundary condition types of the halflinks to be yielded. 
            If empty, all the halflinks are yielded. Default is an empty list.

        Yields
        ------
        hl : Link
            The next Link instance in self.links.
        """
        for hl in super().get_half_links():
            if link_types and bc_types:
                if hl.link_type in link_types and hl.bc_type in bc_types:
                    yield hl
            elif link_types:
                if hl.link_type in link_types:
                    yield hl
            elif bc_types:
                if hl.bc_type in bc_types:
                    yield hl
            else:
                yield hl


    def add_network(self, network):
        """
        Adds network to the network.
        A network can only be added if it a HeatNetwork.

        Parameters
        ----------
        network : HeatNetwork
            The network to be added.

        Raises
        ------
        TypeError
            If network is not a HeatNetwork instance.
        """
        if not isinstance(network, HeatNetwork):
            raise TypeError("Only a HeatNetwork object can be added.")
        else:
            super().add_network(network)


    def make_incidence_matrix(self):
        """
        Creates the branch-nodal incidence matrix A.
        Assigns a number to all nodes and links.
        """
        row = []
        col = []
        data = []
                
        for link in self.get_links():
            # outgoing edge
            if link.start_node in self.get_nodes():  # check if start_node is in the network, i.e. if it is a HeatNode
                row.append(link.start_node.number)
                col.append(link.number)
                data.append(-1)
            # incoming edge
            if link.end_node in self.get_nodes():  # check if end_node is in the network, i.e. if it is a HeatNode
                row.append(link.end_node.number)
                col.append(link.number)
                data.append(1)
        
        self.A = sps.csr_matrix((data, (row, col)), shape=(len(list(self.get_nodes())), len(list(self.get_links()))))


    def actual_incidence_matrix(self):
        """
        Branch-nodal incidence matrix A of the heat network based on the actual direction of flow.

        Returns
        -------
        A : scipy sparse csr_matrix
            Branch-nodal incidence matrix based on actual direction of flow.
        A_neg : scipy sparse csr_matrix
            Aac with positive entries set to 0.
        A_pos : scipy sparse csr_matrix
            Aac with negative entries set to 0.
        """
        m_direction = np.zeros(len(self.links))
        
        for i, link in enumerate(self.get_links()):
            m_direction[i] = np.sign(link.m)
        
        A = self.A.dot(sps.diags(m_direction))
        
        A_neg = A.copy()
        A_neg[A > 0] = 0
        
        A_pos = A.copy()
        A_pos[A < 0] = 0
        
        return A, A_neg, A_pos


    def make_adjacency_matrix(self):
        """
        Create the adjacency matrix Ad. 
        It assumes and uses the same numbering as assigned by make_incidence_matrix(self). 
        This means that the incidence matrix must be made before the adjacency matrix can be made.
        """
        row = []
        col = []
        data = []
        
        for i, node in enumerate(self.get_nodes()):
            for link in node.get_out_links():  # only a non-zero element for out links
                if isinstance(link, HeatLink):  # HalfLinks should not be taken into account
                    row.append(link.start_node.number)
                    col.append(link.end_node.number)
                    data.append(1)
                    
        self.Ad = sps.csr_matrix((data, (row, col)), shape=(len(list(self.get_nodes())), len(list(self.get_nodes()))))


    def initialize(self):
        """
        Inializes the network.
        The branch-nodal incidence matrix, and the adjacency matrix for the heat network are made. 
        Also, all the half links are added to the network, 
        and the bc type of the half link is checked against the node type. 
        The bc type is changed if needed.
        """
        self.make_incidence_matrix()
        self.make_adjacency_matrix()
        
        for node in self.get_nodes():
            for hl in node.get_half_links():
                self.add_half_link(hl)


    def get_x_entries(self):
        """
        Return all the nodes, links, and half links that have an entry in variable vector x.
        It also return all the links with unknown flow, 
        and all the nodes with unknown pressure, 
        all the nodes with unknown supply temperature, 
        and all the nodes with unknown return temperature.

        Returns
        -------
        x_entries : list
           List of all the nodes, links, and half links that contribute to x.
        unknown_m_links : list
            List of all the links that have unknown link flow.
        unknown_m_halflinks : list
            List of all the half links that have unknown half link flow, 
            and are connected to a non slack node. Only used if formulation is 'half_link_flow'.
        unknown_p_nodes : list
            List of all the nodes that have unknown pressure.
        unknown_Ts_nodes : list
            List of all the nodes that have unknown supply temperature.
        unknown_Tr_nodes : list
            List of all the nodes that have unknown return temperature.
        unknown_Ts_halflinks : list
            List of all the half links that have unknown supply temperature.    
        unknown_Tr_halflinks : list
            List of all the half links that have unknown return temperature. 
        """
        unknown_m_links = [link for link in self.get_links() if (isinstance(link.start_node, HeatNode) and isinstance(link.end_node, HeatNode))]  # non-coupling links
        unknown_p_nodes = list(self.get_nodes([1, 2, 4, 6, 12, 14, 15, 16]))
        unknown_Ts_nodes = list(self.get_nodes([1, 2, 3, 5, 8, 9, 11, 12, 13, 15, 16]))
        unknown_Tr_nodes = list(self.get_nodes([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14]))
        
        if self.formulation == 'half_link_flow':
            # half links are not taken into variable vector for all node types, even if m, Ts, or Tr is unknown
            unknown_m_halflinks = [hl for node in self.get_nodes(node_types=[1, 3, 4, 12, 13, 14, 15, 16]) for hl in node.get_half_links()]
            unknown_Ts_halflinks = [hl for node in self.get_nodes(node_types=[1, 3, 4, 12, 13, 14, 15, 16])for hl in node.get_half_links(bc_types=[0, 4, 8, 10, 12, 16, 20, 22])]
            unknown_Tr_halflinks = [hl for node in self.get_nodes(node_types=[1, 3, 4, 12, 13, 14, 15, 16])for hl in node.get_half_links(bc_types=[1, 5, 9, 11, 13, 17, 21, 23])]
        else:
            unknown_m_halflinks = []
            unknown_Ts_halflinks = []
            unknown_Tr_halflinks = []
        
        x_entries = unknown_m_links + unknown_m_halflinks + unknown_p_nodes + \
                    unknown_Ts_nodes + unknown_Tr_nodes + unknown_Ts_halflinks + unknown_Tr_halflinks
        
        return x_entries, unknown_m_links, unknown_m_halflinks, unknown_p_nodes, unknown_Ts_nodes, unknown_Tr_nodes, unknown_Ts_halflinks, unknown_Tr_halflinks


    def get_F_entries(self):
        """
        Return all the nodes, links, and half links that have an entry in function vector F. 
        It also returns the nodes that have an entry in conservation of, 
        all the links that have an entry in the link equations, 
        all the nodes that have an entry in the supply temperature mixing rule,
        and all the nodes that have an entry in the return temperature mixing rule.

        Returns
        -------
        F_entries : list
           List of all the nodes, links, and half links that contribute to F.
        F_m_nodes : list
            List of all the nodes that contribute to conservation of mass.
        F_deltap_links : list
            List of all the links that contribute to link equations.
        F_Ts_nodes : list
            List of all the nodes that contribute to supply temperature mixing rule.
        F_Tr_nodes : list
            List of all the nodes that contribute to return temperature mixing rule.
        F_phi_nodes : list
            List of all the half links that contribute to a heat power equation. Only used if formulation is 'half_link_flow'.
        F_dT_nodes : list
            List of all the half links that contribute to a temperature difference equation. Only used if formulation is 'half_link_flow'.
        """
        F_m_nodes = list(self.get_nodes([1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16]))
        
        # non-coupling links and non-dummy links
        F_deltap_links = [link for link in self.get_links() if ((not link.link_type == 'dummy') and isinstance(link.start_node, HeatNode) and isinstance(link.end_node, HeatNode))]
        
        F_Ts_nodes = list(self.get_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]))
        F_Tr_nodes = list(self.get_nodes([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14, 15, 16]))
        
        if self.formulation == 'half_link_flow':
            F_phi_halflinks = [hl for hl in self.get_half_links(link_types='heat_exchanger', bc_types=[2, 3, 4, 5, 8, 9, 14, 15, 16, 17, 20, 21]) if hl.start_node.node_type in [1, 3, 4, 12, 13, 14, 15, 16]]
            F_dT_halflinks = [hl for hl in self.get_half_links(link_types='heat_exchanger', bc_types=[4, 5, 10, 11, 16, 17, 22, 23]) if hl.start_node.node_type in [12, 13, 14, 15, 16]]
        else:
            F_phi_halflinks = []
            F_dT_halflinks = []

        F_entries = F_m_nodes + F_deltap_links + F_Ts_nodes + F_Tr_nodes + F_phi_halflinks + F_dT_halflinks

        return F_entries, F_m_nodes, F_deltap_links, F_Ts_nodes, F_Tr_nodes, F_phi_halflinks, F_dT_halflinks


    def set_x_init(self):
        """
        Creates the (initial guess for) vector x, based on the current network parameters.

        Returns
        -------
        x_init : np array
           Initial guess for variable vector x.
        """
        x_entries, unknown_m_links, unknown_m_halflinks, unknown_p_nodes, \
        unknown_Ts_nodes, unknown_Tr_nodes, unknown_Ts_halflinks, unknown_Tr_halflinks = self.get_x_entries()
        
        x_init = np.zeros(len(x_entries))

        for ind_el, el in enumerate(unknown_m_links):
            x_init[ind_el] = el.get_m()
        
        start_ind = len(unknown_m_links)
        for ind_el, el in enumerate(unknown_m_halflinks):
            x_init[ind_el+start_ind] = el.get_m()
            
        start_ind += len(unknown_m_halflinks)
        for ind_el, el in enumerate(unknown_p_nodes):
            x_init[ind_el+start_ind] = el.get_p()
            
        start_ind += len(unknown_p_nodes)
        for ind_el, el in enumerate(unknown_Ts_nodes):
            x_init[ind_el+start_ind] = el.get_Ts(Tshift=self.Ta)
            
        start_ind += len(unknown_Ts_nodes)
        for ind_el, el in enumerate(unknown_Tr_nodes):
            x_init[ind_el+start_ind] = el.get_Tr(Tshift=self.Ta)
            
        start_ind += len(unknown_Tr_nodes)
        for ind_el, el in enumerate(unknown_Ts_halflinks):
            x_init[ind_el+start_ind] = el.get_Ts(Tshift=self.Ta)
        
        start_ind += len(unknown_Ts_halflinks)
        for ind_el, el in enumerate(unknown_Tr_halflinks):
            x_init[ind_el+start_ind] = el.get_Tr(Tshift=self.Ta)
            
        return x_init


    def update(self, x):
        """
        Updates the network given variable vector x.

        Parameters
        ----------
        x : np array
            Variable vector x, scaled.
        """
        x_entries, unknown_m_links, unknown_m_halflinks, unknown_p_nodes, \
        unknown_Ts_nodes, unknown_Tr_nodes, unknown_Ts_halflinks, unknown_Tr_halflinks = self.get_x_entries()

        if not len(x) == len(x_entries):
            raise ValueError('x has the wrong length.')
        else:
            for ind_l, link in enumerate(unknown_m_links):
                m = x[ind_l]
                if link.scale_var == 'per_unit':
                    m *= link.scale_var_params['mbase']
                link.m = m

            stride = len(unknown_m_links)
            for ind_hl, hl in enumerate(unknown_m_halflinks):
                m = x[ind_hl + stride]
                if hl.scale_var == 'per_unit':
                    m *= hl.scale_var_params['mbase']
                hl.m = m

            stride += len(unknown_m_halflinks)
            for i, node in enumerate(unknown_p_nodes):
                p = x[i + stride]
                if node.scale_var == 'per_unit':
                    p *= node.scale_var_params['pbase']
                node.p = p

            stride += len(unknown_p_nodes)
            for i, node in enumerate(unknown_Ts_nodes):
                Ts = x[i + stride]

                if not self.Ta == None:
                    Ts += self.Ta
                if node.scale_var == 'per_unit':
                    Ts *= node.scale_var_params['Tbase']
                
                if Ts > node.Ts_max:
                    print('For node {}, Ts = {:.4f} which is larger than Ts_max = {:.4f}.'.format(node.name, Ts, node.Ts_max))
                elif Ts < node.Ts_min:
                    print('For node {}, Ts = {:.4f} which is smaller than Ts_min = {:.4f}.'.format(node.name, Ts, node.Ts_min))
                
                node.Ts = Ts

            stride += len(unknown_Ts_nodes)
            for i, node in enumerate(unknown_Tr_nodes):
                Tr = x[i + stride]

                if not self.Ta == None:
                    Tr += self.Ta
                if node.scale_var == 'per_unit':
                    Tr *= node.scale_var_params['Tbase']

                if Tr > node.Tr_max:
                    print('For node {}, Tr = {:.4f} which is larger than Tr_max = {:.4f}.'.format(node.name, Tr, node.Tr_max))
                elif Tr < node.Tr_min:
                    print('For node {}, Tr = {:.4f} which is smaller than Tr_min = {:.4f}.'.format(node.name, Tr, node.Tr_min))
                
                node.Tr = Tr
                if node.Tr > node.Ts:
                    print('For node {}, Tr = {:.4f} and Ts = {:.4f}, such that Tr > Ts.'.format(node.name, node.Tr, node.Ts))

            stride += len(unknown_Tr_nodes)
            for ind_hl, hl in enumerate(unknown_Ts_halflinks):
                Ts = x[ind_hl + stride]
                if hl.scale_var == 'per_unit':
                    Ts *= hl.scale_var_params['Tbase']
                hl.Ts = Ts

            stride += len(unknown_Ts_halflinks)
            for ind_hl, hl in enumerate(unknown_Tr_halflinks):
                Tr = x[ind_hl + stride]
                if hl.scale_var == 'per_unit':
                    Tr *= hl.scale_var_params['Tbase']
                hl.Tr = Tr

            # update start and end temperatures, and start and end heat power
            for i, link in enumerate(self.get_links()):
                # non-coupling links
                if (isinstance(link.start_node, HeatNode) and isinstance(link.end_node, HeatNode)):
                    # the temperature at the upstream side needs to be updated first, otherwise the flow at the downstream side is wrong
                    if link.m >= 0:
                        link.Ts_start = link.start_node.Ts
                        link.Tr_end = link.end_node.Tr

                        Tr_start = link.return_temperature_start(T_shift=self.Ta)

                        Ts_end = link.supply_temperature_end(T_shift=self.Ta)

                        if link.scale_var == 'per_unit':
                            Tr_start *= link.scale_var_params['Tbase']
                            Ts_end *= link.scale_var_params['Tbase']

                        link.Tr_start = Tr_start
                        link.Ts_end = Ts_end
                    else:
                        link.Ts_end = link.end_node.Ts
                        link.Tr_start = link.start_node.Tr
                        Ts_start = link.supply_temperature_start(T_shift=self.Ta)
                        Tr_end = link.return_temperature_end(T_shift=self.Ta)
                        if link.scale_var == 'per_unit':
                            Ts_start *= link.scale_var_params['Tbase']
                            Tr_end *= link.scale_var_params['Tbase']
                        link.Ts_start = Ts_start
                        link.Tr_end = Tr_end
                    phis_start = link.supply_heat_power_start(T_shift=self.Ta)
                    phir_start = link.return_heat_power_start(T_shift=self.Ta)
                    phis_end = link.supply_heat_power_end(T_shift=self.Ta)
                    phir_end = link.return_heat_power_end(T_shift=self.Ta)
                    if link.scale_var == 'per_unit':
                        phis_start *= link.scale_var_params['phibase']
                        phir_start *= link.scale_var_params['phibase']
                        phis_end *= link.scale_var_params['phibase']
                        phir_end *= link.scale_var_params['phibase']
                    link.phis_start = phis_start
                    link.phir_start = phir_start
                    link.phis_end = phis_end
                    link.phir_end = phir_end
        
        # update flow, heat, Ts, and Tr on half links
        slack_nodes = [0, 8, 9, 10, 11]
        general_slack_nodes = [9, 10, 11]
        for hl in self.get_half_links():
            node = hl.start_node
            # determine mass flow for slack nodes
            if (node.node_type in slack_nodes) and (hl not in unknown_m_halflinks):  # slack nodes
                if hl.link_type == 'dummy':
                    raise TypeError('Half link of node {} is of type "dummy", phi cannot be updated'.format(node.name))
                else:
                    m = 0
                    for link in hl.start_node.get_in_links():
                        if not isinstance(link, HeatHalfLink):
                            m += link.get_m()
                    for link in hl.start_node.get_out_links():
                        if not isinstance(link, HeatHalfLink):
                            m -= link.get_m()
                    if hl.scale_var == 'per_unit':
                        m *= hl.scale_var_params['mbase']
                    hl.m = m
            if hl.bc_type in [4, 5, 10, 11, 16, 17, 22, 23] and hl.dT <= 0:
                raise ValueError('Half link has dT known, but dT should be positive, not {}'.format(hl.dT))

            if self.formulation == 'standard':
                # update temperatures, assuming some are sources and some are sinks.
                if hl.source:  # sources
                    hl.Tr = node.Tr
                    if node.node_type in slack_nodes:  # slack nodes
                        hl.Ts = node.Ts
                    elif hl.bc_type in [4, 5, 10, 11, 16, 17, 22, 23]:  # dT known
                        hl.Ts = hl.dT + hl.Tr
                else:  # sinks
                    hl.Ts = node.Ts
                    if node.node_type in slack_nodes:  # slack nodes
                        hl.Tr = node.Tr
                    elif hl.bc_type in [4, 5, 10, 11, 16, 17, 22, 23]:  # dT known
                        hl.Tr = hl.Ts - hl.dT

                if node.node_type not in slack_nodes:  # non slack nodes
                    # dphi unknown
                    if hl.bc_type in [0, 1, 6, 7, 10, 11, 12, 13, 18, 19, 22, 23]:
                        raise ValueError("Encountered a half link with unknown dphi. In the standard formulation, " + \
                                         "all half links connected to non slack nodes should have known heat power loss!")
                    m = hl.flow()
                    if node.scale_var == 'per_unit':
                        m *= node.scale_var_params['mbase']
                    hl.m = m
            elif self.formulation == 'half_link_flow':
                # update temperatures, based on direction of flow
                if node.node_type in general_slack_nodes:
                    # Otherwise, Ts is already known for these halflinks, or is part of x
                    if (hl.bc_type not in [2, 6, 14, 18]) and (hl not in unknown_Ts_halflinks):
                        hl.Ts = node.Ts
                    # Otherwise, Tr is already known for these halflinks, or is part of x
                    if (hl.bc_type not in [3, 7, 15, 19]) and (hl not in unknown_Tr_halflinks):
                        hl.Tr = node.Tr
                elif node.node_type in slack_nodes:  # slack nodes
                    if hl not in unknown_Ts_halflinks:
                        hl.Ts = node.Ts
                    if hl not in unknown_Tr_halflinks:
                        hl.Tr = node.Tr
                elif hl.sink:  # sinks
                    # Otherwise, Ts is already known for these halflinks, or is part of x
                    if (hl.bc_type not in [2, 6, 14, 18]) and (hl not in unknown_Ts_halflinks):
                        hl.Ts = node.Ts
                    # dT known (Ts is updated in the previous if-statement)
                    if (hl.bc_type in [4, 5, 10, 11, 16, 17, 22, 23]) and (hl not in unknown_Tr_halflinks):
                        hl.Tr = hl.Ts - hl.dT
                else:  # sources
                    # Otherwise, Tr is already known for these halflinks, or is part of x
                    if (hl.bc_type not in [3, 7, 15, 19]) and (hl not in unknown_Tr_halflinks):
                        hl.Tr = node.Tr
                    # dT known (Tr is updated in the previous if-statement)
                    if (hl.bc_type in [4, 5, 10, 11, 16, 17, 22, 23]) and (hl not in unknown_Ts_halflinks):
                        hl.Ts = hl.dT + hl.Tr
            else:
                raise NotImplementedError("update() not implemented for formulation {}".format(self.formulation))

            # update heat powers
            if hl.bc_type in [0, 1, 6, 7, 10, 11, 12, 13, 18, 19, 22, 23]:  # dphi unknown
                dphi = hl.heat(T_shift=self.Ta)
                if hl.scale_var == 'per_unit':
                    dphi *= hl.scale_var_params['phibase']
                hl.dphi = dphi

            phis = hl.supply_heat_power(T_shift=self.Ta)
            phir = hl.return_heat_power(T_shift=self.Ta)
            if hl.scale_var == 'per_unit':
                phis *= hl.scale_var_params['phibase']
                phir *= hl.scale_var_params['phibase']
            hl.phis = phis
            hl.phir = phir


    def update_full(self, x):
        """
        Updates the full network given variable vector x.
        Unlike update(x), not only the values from x are updated, but also all
        parameters not included in x.

        Parameters
        ----------
        x : np array
            Variable vector x, scaled.
        formulation : string, optional
            Formulation used to form system of equations. Default is 'standard'. 
            Options are 'standard' and 'half_link_flow'.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        m_vec : np array
            Array with all link flows
        p_vec : np array
            Array with all unscaled nodal pressures
        Ts_vec : np array
            Array with all unscaled nodal supply temperatures
        Tr_vec : np array
            Array with all unscaled nodal return temperatures
        m_hl_vec : list
            List of arrays with all unscaled half link flows per node
        dphi_hl_vec : list
            List of array with all unscaled half link heat powers per node
        Ts_hl_vec : list
            List of array with all unscaled half link temperatures near supply line per node
        Tr_hl_vec : list
            List of array with all unscaled half link temperatures near return line per node
        """
        m_vec = np.zeros(len(list(self.get_links())))
        p_vec = np.zeros(len(list(self.get_nodes())))
        Ts_vec = np.zeros(len(list(self.get_nodes())))
        Tr_vec = np.zeros(len(list(self.get_nodes())))

        m_hl_vec = []
        dphi_hl_vec = []
        Ts_hl_vec = []
        Tr_hl_vec = []
        for i, node in enumerate(self.get_nodes()):
            p_vec[i] = node.p
            Ts_vec[i] = node.Ts
            Tr_vec[i] = node.Tr

            m_hl_node = []
            dphi_hl_node = []
            Ts_hl_node = []
            Tr_hl_node = []
            for hl in node.get_half_links():
                # get variables for every component (i.link. halflink) connected to node node
                m_hl_node.append(hl.m)
                dphi_hl_node.append(hl.dphi)
                Ts_hl_node.append(hl.Ts)
                Tr_hl_node.append(hl.Tr)
            m_hl_vec.append(m_hl_node)
            dphi_hl_vec.append(dphi_hl_node)
            Ts_hl_vec.append(Ts_hl_node)
            Tr_hl_vec.append(Tr_hl_node)

        for i, link in enumerate(self.get_links()):
            m_vec[i] = link.m

        return m_vec, p_vec, Ts_vec, Tr_vec, m_hl_vec, dphi_hl_vec, Ts_hl_vec, Tr_hl_vec


    def reset_network(self, x_init, formulation='standard', scale_var=None, scale_var_params=None, **kwargs):
        """
        Resets the full network to initial conditions given initial guess vector x.
        Also, any half links for reference slack nodes are removed.

        Parameters
        ----------
        x_init : np array
            Vector with initial guess for x.
        formulation : string, optional
            Formulation used to form system of equations. Default is 'standard'. 
            Options are 'standard' and 'half_link_flow'.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        self.update_full(x_init)
        
        for i, node in enumerate(self.get_nodes([0, 8])):
            if node.half_links:
                for hl in node.get_half_links():
                    hl.m = 0


    def solve_network(self, x_init, solver='nr', solver_parameters={}, lin_solver='lu', lin_solver_parameters={}, post_processing=False):
        """
        Solves the steady-state load flow problem for the heat network.

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
        iters : int
            Number of iterations used.
        err_vec : list
            List with the error for every iteration.
        m_vec : np array
            Array with all unscaled link flows.
        p_vec : np array
            Array with all unscaled nodal pressures.
        Ts_vec : np array
            Array with all unscaled nodal supply temperatures.
        Tr_vec : np array
            Array with all unscaled nodal return temperatures.
        m_hl_vec : list
            List of arrays with all unscaled half link flows per node.
        phi_hl_vec : list
            List of array with all unscaled half link heat powers per node.
        Ts_hl_vec : list
            List of array with all unscaled half link supply temperatures per node.
        Tr_hl_vec : list
            List of array with all unscaled half link return temperatures per node.
        """
        # solver
        if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
            self.solver = NR(tol=solver_parameters['tol'])
        elif re.fullmatch(r'aa', solver, flags=re.IGNORECASE):
            self.solver = AA(tol=solver_parameters['tol'])
        elif re.fullmatch(r'fp', solver, flags=re.IGNORECASE):
            self.solver = FP(tol=solver_parameters['tol'])

        x_sol = self.solver.solve(network=self,
                                  nlsys=NonLinearSystemHeat(self),
                                  x_init=x_init,
                                  solver_parameters=solver_parameters,
                                  lin_solver=lin_solver,
                                  lin_solver_parameters=lin_solver_parameters,
                                  post_processing=post_processing)
        
        # update the rest of the network
        m, p, Ts, Tr, m_hl, dphi_hl, Ts_hl, Tr_hl = self.update_full(x_sol)
        
        return x_sol, self.solver.iterations, self.solver.errors, m, p, Ts, Tr, m_hl, dphi_hl, Ts_hl, Tr_hl

# %% Node

class HeatNode(Node):
    """
    Heat node class.
    """

    def __init__(self, name, scale_var=None, scale_var_params=None, \
                 node_type=0, node_params={},
                 Ts=100, Tr=0, p=0, dphi=None, Ts_hl=None, Tr_hl=None, dT=None, \
                 Ts_max=500, Ts_min=-273.15, Tr_max=500, Tr_min=-273.15, T_shift=0):
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
        node_type : int
            Type of the node, 
            0 = source slack node, (T^s, p)
            1 = load (source/sink) node (T_l, dphi), 
            2 = junction node (m=0), 
            3 = source/sink reference node (T_l, p, dphi), 
            4 = source temperature node (T^s, T^s_l, dphi), 
            5 = reference node (p, m=0), 
            6 = temperature node (T^s, m=0), 
            7 = reference temperature node (T^s, p, m=0), 
            8 = sink slack node (T^r, p), 
            9 = slack node (), 
            10 = slack supply temperature node (), 
            11 = slack return temperature node (), 
            12 = source/sink temperature drop node (), 
            13 = source/sink reference temperature drop node (), 
            14 = source supply temperature temperature difference node (), 
            15 = sink return temperature temperature difference node (), 
            16 = sink temperature node ().
        Ts : float
            Nodal supply temperature, unscaled.
        Tr : float
            Nodal return temperature, unscaled.
        p : float
            Nodal pressure, unscaled.
        dphi : float, optional
            Total injected heat power, unscaled. One half link is made with this heat power. Default is None. 
        Ts_hl : float, optional
            Outflow temperature of 'total' component between supply and return line (or the other way around), 
            at the supply line side, unscaled. 
            One half links is made with this temperature. 
            Default is None. 
        Tr_hl : float, optional
            Outflow temperature of 'total' component between supply and return line (or the other way around), 
            at the supply line side, unscaled. 
            One half links is made with this temperature. 
            Default is None. 
        dT : float, optional
            Temperature difference over half link, unscaled and not shifted. 
            Default is None.
        Ts_max : float, optional
            Upper bound for supply temperature, unscaled. 
            Default is 500 C.
        Ts_min : float, optional
            Lower bound for supply temperature, unscaled. 
            Default is -273.15 C.
        Tr_max : float, optional
            Upper bound for return temperature, unscaled. 
            Default is 500 C.
        Tr_min : float, optional
            Lower bound for return temperature, unscaled. 
            Default is -273.15 C.
        T_shift : float
            Temperature shift.
        """
        super().__init__(name=name)
        
        self.scale_var = scale_var
        self.scale_var_params = scale_var_params
        
        self.node_type = node_type
        self.node_params = node_params
        
        self.Ts = Ts
        self.Ts_max = Ts_max
        self.Ts_min = Ts_min
        self.Tr = Tr
        self.Tr_max = Tr_max
        self.Tr_min = Tr_min
        self.p = p
        
        self.T_shift = T_shift
        
        
    def get_Ts(self):
        """
        Get supply temperature, optionally with scaling.

        Returns
        -------
        Ts : float
            Possibly scaled supply temperature.
        """
        Ts = self.Ts
        if self.scale_var == 'per_unit':
            Ts = (Ts - self.T_shift) / self.scale_var_params['Tbase']
            
        return Ts


    def get_Tr(self):
        """
        Get return temperature optionally with scaling.
        
        Returns
        -------
        Tr : float
            Possibly scaled return temperature.
        """
        Tr = self.Tr
        if self.scale_var == 'per_unit':
            Tr = (Tr - self.T_shift) / self.scale_var_params['Tbase']
            
        return Tr


    def get_p(self):
        """
        Get pressure optionally with scaling.

        Returns
        -------
        p : float
            Possibly scaled pressure.
        """
        p = self.p
        if self.scale_var == 'per_unit':
            p = p / self.scale_var_params['pbase']
        
        return p


    def get_head(self):
        """
        Get unscaled nodal head.

        Parameters
        ----------
        carrier : Carrier
            Carrier flowing through the pipe.

        Returns
        -------
        h : float
            Unscaled nodal head
        """       
        return self.p / (self.node_params['carrier'].rhon*self.node_params['carrier'].g)


    def get_inflow(self):
        """
        Returns the total mass inflow from links (and not half links) into a node, in the supply line.

        Returns
        -------
        ms_in : float
            Mass flow coming into the node from the links.
        """
        ms_in = 0
        for link in self.get_in_links():
            if not link in self.get_half_links():
                m = link.get_m()
                if m >= 0:  # flow is actually coming in (in supply line)
                    ms_in += m
        for link in self.get_out_links():
            if not link in self.get_half_links():
                m = link.get_m()
                if m < 0:  # flow is actually coming in (in supply line)
                    ms_in += -m
        
        return ms_in


    def get_outflow(self):
        """
        Return the total mass outflow to links (and not half links) from a node, in the supply line.

        Returns
        -------
        ms_out : float
            Mass flow coming out of the node into the links.
        """
        ms_out = 0
        for link in self.get_in_links():
            if not link in self.get_half_links():
                m = link.get_m()
                if m < 0:  # flow is actually going out (in supply line)
                    ms_out += -m
        for link in self.get_out_links():
            if not link in self.get_half_links():
                m = link.get_m()
                if m >= 0:  # flow is actually going out (in supply line)
                    ms_out += m
        
        return ms_out


    def node_law(self):
        """
        Node law for a heat node, which is conservation of mass.
        The sum of the water flows of all incoming and outgoing links and half links.

        Returns
        -------
        f : float
            The sum of the gas flows of all incoming and outgoing links and half links.
        """
        f = 0
        
        for link in self.get_in_links():
            f += link.get_m()
        for link in self.get_out_links():  # both links and half links
            f -= link.get_m()
        
        return f


    def mixing_rule(self):
        """
        Mixing rule for a heat node, which is an avarage of incoming temperatures weighted with respect to mass flow.

        Returns
        -------
        f_Ts : float
            The supply temperature mismatch: sum(ms_out)*Ts - sum(ms_in*Ts_in).
        f_Tr : float
            The return temperature mismatch: sum(mr_out)*Tr - sum(mr_in*Tr_in).
        """
        f_Ts = 0
        f_Tr = 0

        for link in self.get_in_links():
            m = link.get_m()
            Ts_in = link.get_Ts_end()
            Tr_in = link.get_Tr_end()
            f_Ts -= m*Ts_in
            f_Tr += m*Tr_in
        for link in self.get_out_links():            
            if link in self.get_half_links():  # half links
                m = link.get_m()
                Ts = link.get_Ts()
                Tr = link.get_Tr()
                f_Ts += m*Ts
                f_Tr -= m*Tr
            else:
                m = link.get_m()
                Ts_out = link.get_Ts_start()
                Tr_out = link.get_Tr_start()
                f_Ts += m*Ts_out
                f_Tr -= m*Tr_out
                
        # make adjustments in case of only inflow or only outflow
        # source nodes with only inflow in supply line
        if (self.node_type in [0, 4] or (self.node_type in [1, 3, 12, 13, 14, 15] and np.all([hl.source for hl in self.get_half_links()]))) and self.get_outflow() == 0:
            f_Ts += self.get_inflow()*self.get_Ts()
            for hl in self.get_half_links():
                f_Ts -= hl.get_m()*self.get_Ts()
        elif self.node_type in [2, 5, 6, 7] and self.get_outflow() == 0: # junction nodes with only inflow in supply line
            f_Ts += self.get_inflow()*self.get_Ts()
        # sink nodes with only outflow in supply line
        elif (self.node_type in [8, 16] or (self.node_type in [1, 3, 12, 13, 14, 15] and np.all([hl.sink for hl in self.get_half_links()]))) and self.get_inflow() == 0:
            f_Tr += self.get_outflow()*self.get_Tr()
            for hl in self.get_half_links():
                f_Tr += hl.get_m()*self.get_Tr()
        elif self.node_type in [2, 5, 6, 7] and self.get_inflow() == 0: # junction nodes with only outflow in supply line
            f_Tr += self.get_outflow()*self.get_Tr()
        
        return f_Ts, f_Tr

# %% Link

class HeatLink(Link):
    """
    Heat link class.
    """

    def __init__(self, name, start_node, end_node, \
                 m=0, Ts_start=100, Tr_start=0, dT_start=100, Ts_end=100, Tr_end=0, dT_end=100, \
                 phis_start=0, phir_start=0, dphi_start=0, phis_end=0, phir_end=0, dphi_end=0, \
                 scale_var=None, scale_var_params=None, \
                 bc_type=0, link_type='dummy', link_params={}, hydraulic_equation_formulation='dp_of_q', T_shift=0):
        """
        Creates a HeatLink object.

        Parameters
        ----------
        name : str
            The name of the half link.
        start_node : Node
            Start node of the half link.
        end_node : Node
            End node of the half link.
        m : float, optional
            Link mass flow, unscaled. Default is 0.
        Ts_start : float, optional
            Temperature at the start of the link in the supply line, unscaled. 
        Tr_start : float, optional
            Temperature at the start of the link in the return line, unscaled. 
        dT_start : float, optional
            Temperature difference between supply and return line at the start of the link, unscaled.
        Ts_end : float, optional
            Temperature at the end of the link in the supply line, unscaled. 
        Tr_end : float, optional
            Temperature at the end of the link in the return line, unscaled. 
        dT_end : float, optional
            Temperature difference between supply and return line at the end of the link, unscaled.
        phis_start : float, optional
            Heat power at the start of the link in the supply line, unscaled. 
        phir_start : float, optional
            Heat power at the start of the link in the return line, unscaled. 
        dphi_start : float, optional
            Heat power difference between supply and return line at the start of the link, unscaled.
        phis_end : float, optional
            Heat power at the end of the link in the supply line, unscaled. 
        phir_end : float, optional
            Heat power at the end of the link in the return line, unscaled.
        dphi_end : float, optional
            Heat power difference between supply and return line at the end of the link, unscaled.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        bc_type : int, optional
            Default is 0. Boundary condition of the link. 
            0 = everything unknown (source), 
            1 = everything unknown (sink), 
            2 = dphi and Ts known at start (source), 
            3 = dphi and Tr known at start (sink), 
            4 = dphi and dT known at start (source), 
            5 = dphi and dT known at start (sink), 
            6 = Ts known at start (source), 
            7 = Tr known at start (sink), 
            8 = dphi known and Ts unknown at start (source), 
            9 = dphi known and Tr unknown at start (sink), 
            10 = dT known at start (source), 
            11 = dT known at start (sink).
        link_type : str, optional.
            Type of the link. Options are:
            - 'dummy', 
            - 'isolated_resistor', 
            - 'standard_resistor',
            - 'isolated_resistor', 
            - 'standard_resistor',
            - 'isolated_pipe_low', 
            - 'standard_pipe_low',
            - 'isolated_pipe_high', 
            - 'standard_pipe_high', 
            - 'isolated_pump',
            - 'standard_pump'.
            Default is 'dummy'.
        link_params : dict, optional
            Dictionary with the link parameters required for the link type. Default is an empty dict.
        hydraulic_equation_formulation : string, optional
            Determines which link equation formulation is used. 
            Default is 'dp_of_q', which uses the pressure drop as a function of link flow (i.e. it uses fb). 
            The other option is 'q_of_dp', which uses the link flow as a function of pressure drop (i.e. it uses fa).

        Raises
        ------
        TypeError
            If start_node or end_node is not an instance of Node.
        ValueError
            If link_type is not a valid link type.
        """
        super().__init__(name, start_node, end_node)
        
        self.m = m
        self.Ts_start = Ts_start
        self.Tr_start = Tr_start
        self.dT_start = dT_start
        self.Ts_end = Ts_end
        self.Tr_end = Tr_end
        self.dT_end = dT_end
        self.phis_start = phis_start
        self.phir_start = phir_start
        self.dphi_start = dphi_start
        self.phis_end = phis_end
        self.phir_end = phir_end
        self.dphi_end = dphi_end
        
        self.scale_var = scale_var
        self.scale_var_params = scale_var_params
        
        self.bc_type = bc_type
        
        self.link_type = link_type
        self.link_params = link_params
        
        self.T_shift = T_shift
        link_params['T_shift'] = self.T_shift
        
        self.hydraulic_equation_formulation = hydraulic_equation_formulation
        
        if link_type == 'dummy':
            self.equation_thermal = thermal.dummy
            self.equation_hydraulic = hydraulic.dummy
        elif link_type == 'isolated_resistor':
            self.equation_thermal = thermal.perfect_isolated_pipe
            self.equation_hydraulic = hydraulic.resistor
        elif link_type == 'standard_resistor':
            self.equation_thermal = thermal.standard_pipe
            self.equation_hydraulic = hydraulic.resistor
        elif link_type == 'isolated_resistor_fixed':
            self.equation_thermal = thermal.perfect_isolated_pipe
            self.equation_hydraulic = hydraulic.resistor_fixed
        elif link_type == 'standard_resistor_fixed':
            self.equation_thermal = thermal.standard_pipe
            self.equation_hydraulic = hydraulic.resistor_fixed
        elif link_type == 'isolated_pipe_low':
            self.equation_thermal = thermal.perfect_isolated_pipe
            self.equation_hydraulic = hydraulic.pipe_low
        elif link_type == 'standard_pipe_low':
            self.equation_thermal = thermal.standard_pipe
            self.equation_hydraulic = hydraulic.pipe_low
        elif link_type == 'isolated_pipe_high':
            self.equation_thermal = thermal.perfect_isolated_pipe
            self.equation_hydraulic = hydraulic.pipe_high
        elif link_type == 'standard_pipe_high':
            self.equation_thermal = thermal.standard_pipe
            self.equation_hydraulic = hydraulic.pipe_high
        elif link_type == 'isolated_pump':
            self.equation_thermal = thermal.perfect_isolated_pipe
            self.equation_hydraulic = hydraulic.compressor
        elif link_type == 'standard_pump':
            self.equation_thermal = thermal.standard_pipe
            self.equation_hydraulic = hydraulic.compressor
        else:
            raise ValueError('link_type is not a valid link type.')
        
        temperature_drop_factor, temperature_drop_factor_dm, T_end_of_T_start, dT_end_dm, dT_end_dT_start = self.equation_thermal(link_params=link_params)
        pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq = self.equation_hydraulic(link_params=link_params)
        
        # hydraulic equations
        self.pipe_constant = pipe_constant
        self.dp = dp
        self.dp_of_q = dp_of_q
        self.q_of_dp = q_of_dp
        
        if hydraulic_equation_formulation == 'q_of_dp':
            self.f = fa
            self.df_ddp = dfa_ddp
            self.df_dq = dfa_dq
        elif hydraulic_equation_formulation == 'dp_of_q':
            self.f = fb
            self.df_ddp = dfb_ddp
            self.df_dq = dfb_dq
        else:
            raise ValueError('hydraulic_equation_formulation is not valid. It should be either "q_of_dp" or "dp_of_q", not {}.'.format(hydraulic_equation_formulation))
        
        self.ddp_dq = ddp_dq
        self.ddp_dp = ddp_dp

        # thermal equations
        self.temperature_drop_factor = temperature_drop_factor
        self.temperature_drop_factor_dm = temperature_drop_factor_dm
        self.T_end_of_T_start = T_end_of_T_start
        self.dT_end_dm = dT_end_dm
        self.dT_end_dT_start = dT_end_dT_start


    def set_type(self, scale_var=None, scale_var_params=None, link_type=None, link_params=None, hydraulic_equation_formulation=None, bc_type=None, T_shift=None):
        """
        Set or change the link type, and the corresponding link equations.

        Parameters
        ----------
        scale_var : string, optional
            How to scale the variable.
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables.
        link_type : str
            Type of the link.
        link_params : dict
            Dictionary with the link parameters required for the link type.
        hydraulic_equation_formulation : string, optional
            Determines which link equation formulation is used.
        bc_type : int, optional
            Boundary condition of the link.
        
        Raises
        ------
        ValueError
            If link_type is not a valid link type.
        """
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        if link_type is not None:
            self.link_type = link_type
            if link_type == 'dummy':
                self.equation_thermal = thermal.dummy
                self.equation_hydraulic = hydraulic.dummy
            elif link_type == 'isolated_resistor':
                self.equation_thermal = thermal.perfect_isolated_pipe
                self.equation_hydraulic = hydraulic.resistor
            elif link_type == 'standard_resistor':
                self.equation_thermal = thermal.standard_pipe
                self.equation_hydraulic = hydraulic.resistor
            elif link_type == 'isolated_resistor_fixed':
                self.equation_thermal = thermal.perfect_isolated_pipe
                self.equation_hydraulic = hydraulic.resistor_fixed
            elif link_type == 'standard_resistor_fixed':
                self.equation_thermal = thermal.standard_pipe
                self.equation_hydraulic = hydraulic.resistor_fixed
            elif link_type == 'isolated_pipe_low':
                self.equation_thermal = thermal.perfect_isolated_pipe
                self.equation_hydraulic = hydraulic.pipe_low
            elif link_type == 'standard_pipe_low':
                self.equation_thermal = thermal.standard_pipe
                self.equation_hydraulic = hydraulic.pipe_low
            elif link_type == 'isolated_pipe_high':
                self.equation_thermal = thermal.perfect_isolated_pipe
                self.equation_hydraulic = hydraulic.pipe_high
            elif link_type == 'standard_pipe_high':
                self.equation_thermal = thermal.standard_pipe
                self.equation_hydraulic = hydraulic.pipe_high
            elif link_type == 'isolated_pump':
                self.equation_thermal = thermal.perfect_isolated_pipe
                self.equation_hydraulic = hydraulic.compressor
            elif link_type == 'standard_pump':
                self.equation_thermal = thermal.standard_pipe
                self.equation_hydraulic = hydraulic.compressor
            else:
                raise ValueError('link_type is not a valid link type.')
        
            temperature_drop_factor, temperature_drop_factor_dm, T_end_of_T_start, dT_end_dm, dT_end_dT_start = self.equation_thermal(link_params=link_params)
            pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq = self.equation_hydraulic(link_params=link_params)
        
            # hydraulic equations
            self.pipe_constant = pipe_constant
            self.dp = dp
            self.dp_of_q = dp_of_q
            self.q_of_dp = q_of_dp
            
            if hydraulic_equation_formulation == 'q_of_dp':
                self.f = fa
                self.df_ddp = dfa_ddp
                self.df_dq = dfa_dq
            elif hydraulic_equation_formulation == 'dp_of_q':
                self.f = fb
                self.df_ddp = dfb_ddp
                self.df_dq = dfb_dq
            else:
                raise ValueError('hydraulic_equation_formulation is not valid. It should be either "q_of_dp" or "dp_of_q", not {}.'.format(hydraulic_equation_formulation))
            
            self.ddp_dq = ddp_dq
            self.ddp_dp = ddp_dp

            # thermal equations
            self.temperature_drop_factor = temperature_drop_factor
            self.temperature_drop_factor_dm = temperature_drop_factor_dm
            self.T_end_of_T_start = T_end_of_T_start
            self.dT_end_dm = dT_end_dm
            self.dT_end_dT_start = dT_end_dT_start
        
        if link_params is not None:
            self.link_params = link_params
        
        if hydraulic_equation_formulation is not None:
            self.hydraulic_equation_formulation = hydraulic_equation_formulation
        
        if bc_type is not None:
            self.bc_type = bc_type

        if self.T_shift is not None:        
            self.T_shift = T_shift
            link_params['T_shift'] = self.T_shift
                

    def get_m(self):
        """
        Get mass flow, optionally with scaling.

        Returns
        -------
        m : float
            Possible scaled mass flow.
        """
        m = self.m
        if self.scale_var == 'per_unit':
            m = m / self.scale_var_params['mbase']
        
        return m


    def get_Ts_start(self):
        """
        Get supply temperature at start of the link, optionally with scaling.

        Returns
        -------
        Ts_start : float
            Possibly scaled supply temperature at start of the link.
        """
        Ts_start = self.Ts_start
        if self.scale_var == 'per_unit':
            Ts_start = (Ts_start - self.T_shift) / self.scale_var_params['Tbase']

        return Ts_start


    def get_Tr_start(self):
        """
        Get return temperature at start of the link, optionally with scaling.

        Returns
        -------
        Tr_start : float
            Possibly scaled return temperature at start of the link.
        """
        Tr_start = self.Tr_start
        if self.scale_var == 'per_unit':
            Tr_start = (Tr_start - self.T_shift) / self.scale_var_params['Tbase']
        
        return Tr_start


    def get_dT_start(self):
        """
        Get temperature difference between supply and return at start of the link, optionally with scaling.

        Returns
        -------
        dT_start : float
            Possibly scaled temperature difference between supply and return at start of the link.
        """
        dT_start = self.dT_start
        if self.scale_var == 'per_unit':
            dT_start = (dT_start - self.T_shift) / self.scale_var_params['Tbase']
        
        return dT_start


    def get_Ts_end(self):
        """
        Get supply temperature at end of the link, optionally with scaling.

        Returns
        -------
        Ts_end : float
            Possibly scaled supply temperature at end of the link.
        """
        Ts_end = self.Ts_end
        if self.scale_var == 'per_unit':
            Ts_end = (Ts_end - self.T_shift) / self.scale_var_params['Tbase']
        
        return Ts_end


    def get_Tr_end(self):
        """
        Get return temperature at end of the link, optionally with scaling.

        Returns
        -------
        Tr_end : float
            Possibly scaled return temperature at end of the link.
        """
        Tr_end = self.Tr_end
        if self.scale_var == 'per_unit':
            Tr_end = (Tr_end - self.T_shift) / self.scale_var_params['Tbase']
        
        return Tr_end


    def get_dT_end(self):
        """
        Get temperature difference between supply and return at end of the link, 
        optionally with scaling.

        Returns
        -------
        dT_end : float
            Possibly scaled temperature difference between supply and return at end of the link.
        """
        dT_end = self.dT_end
        if self.scale_var == 'per_unit':
            dT_end = dT_end / self.scale_var_params['Tbase']
        
        return dT_end


    def get_phis_start(self):
        """
        Get heat power in supply line near start node, optionally with scaling.

        Returns
        -------
        Pstart : float
            Possibly scaled heat power in supply line at start of the link.
        """
        phis_start = self.phis_start
        if self.scale_var == 'per_unit':
            phis_start = phis_start / self.scale_var_params['phibase']
        
        return phis_start


    def get_phir_start(self):
        """
        Get heat power in return line near start node, optionally with scaling.

        Returns
        -------
        phir_start : float
            Possibly scaled heat power in return line at start of the link.
        """
        phir_start = self.phir_start
        if self.scale_var == 'per_unit':
            phir_start = phir_start / self.scale_var_params['phibase']
        
        return phir_start


    def get_dphi_start(self):
        """
        Get heat power difference between supply and return at start of link, 
        optionally with scaling.

        Returns
        -------
        Pstart : float
            Possibly scaled heat power difference between supply and return at start of link
        """
        dphi_start = self.dphi_start
        if self.scale_var == 'per_unit':
            dphi_start = dphi_start / self.scale_var_params['phibase']
        
        return dphi_start

    def get_phis_end(self):
        """
        Get heat power near in supply line end node, optionally with scaling.

        Returns
        -------
        phis_end : float
            Possibly scaled heat power in supply line at end of the link. 
        """
        phis_end = self.phis_end
        if self.scale_var == 'per_unit':
            phis_end = phis_end / self.scale_var_params['phibase']
        
        return phis_end


    def get_phir_end(self):
        """
        Get heat power in return line near the end node, optionally with scaling.

        Returns
        -------
        phir_end : float
            Possibly scaled heat power in return line at end of the link. 
        """
        phir_end = self.phir_end
        if self.scale_var == 'per_unit':
            phir_end = phir_end / self.scale_var_params['phibase']
        
        return phir_end


    def get_dphi_end(self):
        """
        Get heat power difference between supply and return at end of link, optionally with scaling.

        Parameters
        ----------
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        Pend : float
            Possibly scaled heat power difference between supply and return at end of link.
        """
        dphi_end = self.dphi_end
        if self.scale_var == 'per_unit':
            dphi_end = dphi_end / self.scale_var_params['phibase']
        
        return dphi_end


    def pres_drop(self):
        """
        Determines the pressure drop over the link.

        Returns
        -------
        dp : float
            Pressure drop over link. Pressure of start node - pressure at end node.
        """
        return self.start_node.get_p() - self.end_node.get_p()


    def pres_drop_func(self):
        """
        Determines the pressure drop function over the link.
        The function is determined by the link type.

        Returns
        -------
        dp : float
            Pressure drop function over the link. Determined by the link type.
        """
        return self.dp(self.start_node.get_p(), self.end_node.get_p())


    def flow(self):
        """
        Determines the flow through the link as a function of start and end pressures.
        This function is determined by the link type. 

        Returns
        -------
        q : float
            Link flow. 
        """
        return self.q_of_dp(self.start_node.get_p(), self.end_node.get_p(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def pres_drop_func_der_m(self):
        """
        Determines the derivative of the pressure drop function to link flow.

        Returns
        -------
        ddp_dm : float
            Derivative of pressure drop function to link flow.
        """
        return self.ddp_dq(self.get_m(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def pres_drop_func_der_p(self):
        """
        Determines the derivative of the pressure drop function to start and end pressures.

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """      
        return self.ddp_dp(self.start_node.get_p(), self.end_node.get_p())


    def psi(self):
        """
        Determine the temperature drop factor, as a function of mass flow.
        Factor is determined by the link type.
        
        Returns
        -------
        psi : float
            Temperature drop factor of the link.
        """
        return self.temperature_drop_factor(self.get_m(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def psi_der_m(self):
        """
        Determine the derivative of the temperature drop factor to the link flow.

        Returns
        -------
        dpsi_dm : float
            The derivative of the temperature drop factor of the link to the link flow.
        """
        return self.temperature_drop_factor_dm(self.get_m(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def link_equation(self):
        """
        Determines the value of the link equation.

        Returns
        -------
        f : float
            link equation f(q, p_start, p_end).
        """
        return self.f(self.get_m(), self.start_node.get_p(), self.end_node.get_p(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def f_der_dp_func(self):
        """
        Determines the derivative of the link equation to the pressure drop function.

        Returns
        -------
        df_ddp : float
            Derivative of the link equation to pressure drop function.
        """        
        return self.df_ddp(self.get_m(), self.start_node.get_p(), self.end_node.get_p(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def f_der_m(self):
        """
        Determines the derivative of the link equation to the link flow.

        Returns
        -------
        df_dm : float
            Derivative of link equation to link flow.
        """
        return self.df_dq(self.get_m(), self.start_node.get_p(), self.end_node.get_p(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def supply_temperature_start(self):
        """
        Determine the supply temperature at the start of the link, 
        based on defined direction of link. 
        Possibly a function of temperature at end of the link.

        Returns
        -------
        Ts_start : float
            Supply temperature at start of the link.
        """
        if self.get_m() >= 0:
            if isinstance(self.start_node, HeatNode):
                Ts_start = self.start_node.get_Ts()
            else:
                Ts_start = self.get_Ts_start()
        else:
            Ts_start = self.T_end_of_T_start(self.get_m(), self.get_Ts_end(), self.T_shift, scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        
        return Ts_start


    def return_temperature_start(self):
        """
        Determine the return temperature at the start of the link, 
        based on defined direction of link. 
        Possibly a function of temperature at end of the link.

        Returns
        -------
        Tr_start : float
            Return temperature at start of the link.
        """
        if self.get_m() >= 0:  # flow is in opposite direction in return line
            Tr_start = self.T_end_of_T_start(self.get_m(), self.get_Tr_end(), self.T_shift, scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        else:
            if isinstance(self.start_node, HeatNode):
                Tr_start = self.start_node.get_Tr()
            else:
                Tr_start = self.get_Tr_start()
        
        return Tr_start


    def supply_temperature_end(self):
        """
        Determine the supply temperature at the end of the link, 
        based on defined direction of link. 
        Possibly a function of temperature at start of the link.

        Returns
        -------
        Ts_end : float
            Supply temperature at end of the link.
        """
        if self.get_m() >= 0:
            Ts_end = self.T_end_of_T_start(self.get_m(), self.get_Ts_start(), self.T_shift, scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        else:
            if isinstance(self.end_node, HeatNode):
                Ts_end = self.end_node.get_Ts()
            else:
                Ts_end = self.get_Tss_end()
                
        return Ts_end


    def return_temperature_end(self):
        """
        Determine the return temperature at the end of the link, 
        based on defined direction of link. 
        Possibly a function of temperature at start of the link.

        Returns
        -------
        Tr_end : float
            Return temperature at end of the link.
        """
        if self.get_m() >= 0:  # flow is in opposite direction in return line
            if isinstance(self.end_node, HeatNode):
                Tr_end = self.end_node.get_Tr()
            else:
                Tr_end = self.get_Tr_end()
        else:
            Tr_end = self.T_end_of_T_start(self.get_m(), self.get_Tr_start(), self.T_shift, scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        
        return Tr_end


    def supply_heat_power_start(self):
        """
        Determine the heat power at the start of the link, in the supply line, 
        as a function of temperature and mass flow.

        Returns
        -------
        phis_start : float
            Heat power in supply line at start of the link.
        """
        return self.link_params['carrier'].get_Cp(scale_var=self.scale_var, scale_var_params=self.scale_var_params) * self.get_m() * self.supply_temperature_start()


    def return_heat_power_start(self):
        """
        Determine the heat power at the start of the link, in the return line, 
        as a function of temperature and mass flow.

        Returns
        -------
        phir_start : float
            Heat power in return line at start of the link.
        """
        return -self.link_params['carrier'].get_Cp(scale_var=self.scale_var, scale_var_params=self.scale_var_params)*  self.get_m() * self.return_temperature_start()


    def supply_heat_power_end(self):
        """
        Determine the heat power at the end of the link, in the supply line, 
        as a function of temperature and mass flow.

        Returns
        -------
        phis_start : float
            Heat power in supply line at end of the link.
        """
        return -self.link_params['carrier'].get_Cp(scale_var=self.scale_var, scale_var_params=self.scale_var_params) * self.get_m() * self.supply_temperature_end()


    def return_heat_power_end(self):
        """
        Determine the heat power at the end of the link, in the return line, 
        as a function of temperature and mass flow.

        Returns
        -------
        phir_start : float
            Heat power in return line at end of the link.
        """
        return self.link_params['carrier'].get_Cp(scale_var=self.scale_var, scale_var_params=self.scale_var_params) * self.get_m() * self.return_temperature_end()


    def heat_loss_supply(self):
        """
        Determines the heat loss over the pipe in the supply line. 

        Returns
        -------
        dphi : float
            Heat loss over the pipe in the supply line. 
        """
        return self.get_phis_start() + self.get_phis_end()


    def heat_loss_return(self):
        """
        Determines the heat loss over the pipe in the return line.

        Returns
        -------
        dphi : float
            Heat loss over the pipe in the return line. 
        """
        return self.get_phir_start() + self.get_phir_end()


    def supply_temperature_start_der_m(self):
        """
        Derivative of the supply temperature at the start of the link, 
        based on defined direction of link, to link mass flow

        Returns
        -------
        dTsij_dm : float
            Derivative of the start supply temperature to mass flow.
        """
        if self.get_m() >= 0:
            dTsij_dm = 0
        else:
            dTsij_dm = self.dT_end_dm(self.get_m(), self.supply_temperature_end(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        
        return dTsij_dm


    def supply_temperature_start_der_Ts(self):
        """
        Derivative of the supply temperature at the start of the link, 
        based on defined direction of link, to nodal supply temperature of start node.

        Returns
        -------
        dTsij_dTs : float, array
            Derivative of the start supply temperature to nodal supply temperature 
            of start node and to nodal return temperature of end node.
        """
        if self.get_m() >= 0:
            dTsij_dTsi = 1
            dTsij_dTsj = 0
        else:
            dTsij_dTsi = 0
            dTsij_dTsj = self.dT_end_dT_start(self.get_m(), self.supply_temperature_end(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        
        return np.array([dTsij_dTsi, dTsij_dTsj])


    def supply_temperature_end_der_m(self):
        """
        Derivative of the supply temperature at the end of the link, 
        based on defined direction of link, to link mass flow.

        Returns
        -------
        dTsji_dm : float
            Derivative of the end supply temperature to mass flow.
        """
        if self.get_m() >= 0:
            dTsji_dm = self.dT_end_dm(self.get_m(), self.supply_temperature_start(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        else:
            dTsji_dm = 0
        
        return dTsji_dm


    def supply_temperature_end_der_Ts(self):
        """
        Derivative of the supply temperature at the end of the link, 
        based on defined direction of link, to nodal supply temperature of start node.

        Returns
        -------
        dTsji_dTs : float, array
            Derivative of the end supply temperature to nodal supply temperature of 
            start node and to nodal return temperature of end node.
        """
        if self.get_m() >= 0:
            dTsji_dTsi = self.dT_end_dT_start(self.get_m(), self.supply_temperature_start(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
            dTsji_dTsj = 0
        else:
            dTsji_dTsi = 0
            dTsji_dTsj = 1
        
        return np.array([dTsji_dTsi, dTsji_dTsj])


    def return_temperature_start_der_m(self):
        """
        Derivative of the return temperature at the start of the link, 
        based on defined direction of link, to link mass flow.

        Returns
        -------
        dTrij_dm : float
            Derivative of the start return temperature to mass flow.
        """
        if self.get_m() >= 0:
            dTrij_dm = self.dT_end_dm(self.get_m(), self.return_temperature_end(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        else:
            dTrij_dm = 0
        
        return dTrij_dm


    def return_temperature_start_der_Tr(self):
        """
        Derivative of the return temperature at the start of the link, 
        based on defined direction of link, to nodal return temperature of start node 
        Note that end node based on defined direction of flow.

        Returns
        -------
        dTrij_dTr : float, array
            Derivative of the start return temperature to nodal return temperature 
            of start node and to nodal return temperature of end node.
        """
        if self.get_m() >= 0:
            dTrij_dTri = 0
            dTrij_dTrj = self.dT_end_dT_start(self.get_m(), self.return_temperature_end(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        else:
            dTrij_dTri = 1
            dTrij_dTrj = 0
        
        return np.array([dTrij_dTri, dTrij_dTrj])


    def return_temperature_end_der_m(self):
        """
        Derivative of the return temperature at the end of the link, 
        based on defined direction of link, to link mass flow.
        Note that end node based on defined direction of flow.

        Returns
        -------
        dTrij_dm : float
            Derivative of the end return temperature to mass flow.
        """
        if self.get_m() >= 0:
            dTrij_dm = 0
        else:
            dTrij_dm = self.dT_end_dm(self.get_m(), self.return_temperature_start(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
        
        return dTrij_dm


    def return_temperature_end_der_Tr(self):
        """
        Derivative of the return temperature at the end of the link, 
        based on defined direction of link, to nodal return temperature of end node.
        Note that end node based on defined direction of flow.

        Returns
        -------
        dTrij_dTr : float, array
            Derivative of the end return temperature to nodal return temperature 
            of end node and to nodal return temperature of end node.
        """
        if self.get_m() >= 0:
            dTrij_dTri = 0
            dTrij_dTrj = 1
        else:
            dTrij_dTri = self.dT_end_dT_start(self.get_m(), self.return_temperature_start(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)
            dTrij_dTrj = 0
            
        return np.array([dTrij_dTri, dTrij_dTrj])

# %% Half Link

class HeatHalfLink(HalfLink):
    """
    Heat half link class.
    The default is an outflow half link.
    """
    
    def __init__(self, name, start_node,
                 Ts=0, Tr=0, m=0, phis=0, phir=0, dphi=0, dT=0,
                 scale_var=None, scale_var_params=None, bc_type=0, link_type='dummy', link_params={}, T_shift=0):
        """
        Creates a HeatHalfLink object

        Parameters
        ----------
        name : str
            Name of the half link.
        start_node : Node
            Start node of the half link.
        m : float, optional
            Mass flow, unscaled. Default is 0.
        phis : float, optional
            Heat power near supply line, unscaled. Default is 0.
        phir : float, optional
            Heat power near return line, unscaled. Default is 0.
        dphi : float
            Heat power difference over half link. 
            That is, the heat power exchanged with surroundings in case of heat exchanger half link. Default is 0.
        Ts : float, optional
            Temperature of component near supply line, unscaled and not shifted. Default is 0.
        Tr : float, optional
            Temperature of component near return line, unscaled and not shifted. Default is 0.
        dT : float, optional
            Temperature difference over half link, unscaled and not shifted. Default is 0.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        bc_type : int, optional
            Default is 0. Boundary condition of the half link. 
            0 = everything unknown (source), 
            1 = everything unknown (sink), 
            2 = dphi and Ts known (source), 
            3 = dphi and Tr known (sink), 
            4 = dphi and dT known (source), 
            5 = dphi and dT known (sink), 
            6 = Ts known (source), 
            7 = Tr known (sink), 
            8 = dphi known and Ts unknown (source), 
            9 = dphi known and Tr unknown (sink), 
            10 = dT known (source), 
            11 = dT known (sink), 
            12 = m known (source), 
            13 = m known (sink), 
            14 = m, dphi and Ts known (source),
            15 = m, dphi and Tr known (sink), 
            16 = m, dphi and dT known (source), 
            17 = m, dphi and dT known (sink), 
            18 = m, Ts known (source), 
            19 = m, Tr known (sink), 
            20 = m, dphi known and Ts unknown (source), 
            21 = m, dphi known and Tr unknown (sink), 
            22 = m, dT known (source),
            23 = m, dT known (sink).
        link_type : string, optional
            Type of the half link, options are 
            - 'dummy',
            - 'heat_exchanger'. 
            Default is 'dummy', which creates a half link with no model.
        link_params : dict, optional
            Dictionary of halflink parameters needed for a specific halflink type. 
            Default is an empty dict.
        T_shift : float
            Temperature shift.

        Raises
        ------
        TypeError
            If start_node is not an instance of Node.
        ValueError
            If halflink_type is not a valid half link type.
        """
        super().__init__(name=name, start_node=start_node)
        
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        self.bc_type = bc_type
        
        # list of bc types for which the half link acts as a sink
        if self.bc_type in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
            self.sink = True
            self.source = False
        else:
            self.sink = False
            self.source = True

        self.link_type = link_type
        self.link_params = link_params

        self.T_shift = T_shift

        self.m = m
        self.phis = phis
        self.phir = phir
        self.dphi = dphi
        self.Ts = Ts
        self.Tr = Tr
        self.dT = dT

        # Setting-up functions corresponding to terminal link
        if link_type == 'dummy':
            m_of_phi, phi_of_m, dm_dTs, dm_dTr, dphi_dm, dphi_dTs, dphi_dTr = halflink_thermal.dummy(link_params=link_params)
        elif link_type == 'heat_exchanger':
            m_of_phi, phi_of_m, dm_dTs, dm_dTr, dphi_dm, dphi_dTs, dphi_dTr = halflink_thermal.heat_exchanger(link_params=link_params)
        else:
            raise ValueError("link_type should be either 'dummy' or 'heat_exchanger' not {}".format(link_type))

        self.m_of_phi = m_of_phi
        self.phi_of_m = phi_of_m
        self.dm_dTs = dm_dTs
        self.dm_dTr = dm_dTr
        self.dphi_dm = dphi_dm
        self.dphi_dTs = dphi_dTs
        self.dphi_dTr = dphi_dTr


    def set_type(self, scale_var=None, scale_var_params=None, link_type=None, link_params=None, bc_type=None, T_shift=None):
        """
        Set or change the half link type, and the corresponding link equations.

        Parameters
        ----------
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        bc_type : int, optional
            Default is None, meaning that the same bc_type is not changed. 
            Boundary condition of the half link. 
            0 = everything unknown (source), 
            1 = everything unknown (sink), 
            2 = dphi and Ts known (source), 
            3 = dphi and Tr known (sink), 
            4 = dphi and dT known (source), 
            5 = dphi and dT known (sink), 
            6 = Ts known (source), 
            7 = Tr known (sink), 
            8 = dphi known and Ts unknown (source), 
            9 = dphi known and Tr unknown (sink), 
            10 = dT known (source), 
            11 = dT known (sink), 
            12 = m known (source), 
            13 = m known (sink), 
            14 = m, dphi and Ts known (source), 
            15 = m, dphi and Tr known (sink), 
            16 = m, dphi and dT known (source), 
            17 = m, dphi and dT known (sink), 
            18 = m, Ts known (source), 
            19 = m, Tr known (sink), 
            20 = m, dphi known and Ts unknown (source), 
            21 = m, dphi known and Tr unknown (sink), 
            22 = m, dT known (source), 
            23 = m, dT known (sink). 
        link_type : str
            (New) type of the link. Must be 
            'dummy', 
            'heat_exchanger_source', 
            'heat_exchanger_sink',
            'heat_exchanger_general'.
        link_params : dict
            Dictionary with the link parameters required for the (new) link type
        T_shift : float
            Temperature shift.

        Raises
        ------
        ValueError
            If link_type is not a valid half link type
        """
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        if link_type is not None:
            self.link_type = link_type
            if link_type == 'dummy':
                m_of_phi, phi_of_m, dm_dTs, dm_dTr, dphi_dm, dphi_dTs, dphi_dTr = halflink_thermal.dummy(link_params)
            elif link_type == 'heat_exchanger':
                m_of_phi, phi_of_m, dm_dTs, dm_dTr, dphi_dm, dphi_dTs, dphi_dTr = halflink_thermal.heat_exchanger(link_params)
            else:
                raise ValueError("link_type should be either 'dummy' or 'heat_exchanger' not {}".format(link_type))
        if link_params is not None:
            self.link_params = link_params
            
        if bc_type is not None:  # Need to check if not None, because if bc_type = 0, it should be changed
            self.bc_type = bc_type
            # list of bc types for which the half link acts as a sink
            if self.bc_type in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
                self.sink = True
                self.source = False
            else:
                self.sink = False
                self.source = True
        
        if T_shift is not None:
            self.T_shift = T_shift
        
        self.m_of_phi = m_of_phi
        self.phi_of_m = phi_of_m
        self.dm_dTs = dm_dTs
        self.dm_dTr = dm_dTr
        self.dphi_dm = dphi_dm
        self.dphi_dTs = dphi_dTs
        self.dphi_dTr = dphi_dTr


    def get_m(self):
        """
        Get mass flow, optionally with scaling.

        Returns
        -------
        m : float
            Possibly scaled mass flow.
        """        
        if self.scale_var == 'per_unit':
            return self.m / self.scale_var_params['mbase']
        else:
            return self.m


    def get_phis(self):
        """
        Get heat power near supply line, optionally with scaling.

        Returns
        -------
        phis : float
            Possibly scaled heat power near supply line.
        """
        if self.scale_var == 'per_unit':
            return self.phis / self.scale_var_params['phibase']
        else:  
            return self.phis


    def get_phir(self):
        """
        Get heat power near return line, optionally with scaling.

        Returns
        -------
        phir : float
            Possibly scaled heat power near return line.
        """
        if self.scale_var == 'per_unit':
            return self.phir / self.scale_var_params['phibase']
        else:
            return self.phir


    def get_dphi(self):
        """
        Get heat power difference over half link, optionally with scaling.

        Returns
        -------
        dphi : float
            Possibly scaled heat power difference over half link.
        """
        if self.scale_var == 'per_unit': 
            return self.dphi / self.scale_var_params['phibase']
        else: 
            return self.dphi


    def get_Ts(self):
        """
        Get temperature near supply line, optionally with scaling and shifted.

        Returns
        -------
        Ts : float
            Possibly scaled and shifted temperature near supply line.
        """
        if self.scale_var == 'per_unit':
            return (self.Ts - self.T_shift) / self.scale_var_params['Tbase']
        else:            
            return self.Ts - self.T_shift


    def get_Tr(self):
        """
        Get temperature near return line, optionally with scaling and shifted.

        Returns
        -------
        Tr : float
            Possibly scaled and shifted temperature near return line.
        """
        if self.scale_var == 'per_unit':
            return (self.Tr - self.T_shift) / self.scale_var_params['Tbase']
        else:            
            return self.Tr - self.T_shift


    def get_dT(self):
        """
        Get temperature difference, optionally with scaling.

        Returns
        -------
        dT : float
            Possibly scaled temperature difference.
        """
        if self.scale_var == 'per_unit':
            return self.dT / self.scale_var_params['Tbase']
        else:            
            return self.dT


    def heat_power(self):
        """
        Heat power equation.

        Returns
        -------
        f_phi : float
            The heat power equation f_phi(phi, m, To, Ts_node) or f_phi(phi, m, To, Tr_node)
        """
        return -self.get_dphi() + \
                self.phi_of_m(self.get_m(), self.supply_temperature(), self.return_temperature(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def temperature_difference(self):
        """
        Temperature difference equation.

        Returns
        -------
        f_dT : float
            The temperature difference equation f_dT(Ts, Tr).
        """
        if self.link_type == 'heat_exchanger':
            f_dT = self.supply_temperature() - self.return_temperature() - self.get_dT()
        else:
            f_dT = None
            
        return f_dT


    def ddT_der_Tshl(self):
        """
        Derivative of the temperature difference to the half link temperature near supply line.

        Returns
        -------
        ddT_dTshl : float
            Derivative of the temperature difference to the supply temperature.
        """
        return 1


    def ddT_der_Ts(self):
        """
        Derivative of the temperature difference to the nodal supply temperature.

        Returns
        -------
        ddT_dTs : float
            Derivative of the temperature difference to the supply temperature
        """
        return self.ddT_der_Tshl() * self.supply_temperature_der_Ts()


    def ddT_der_Trhl(self):
        """
        Derivative of the temperature difference to the half link temperature near return line.

        Returns
        -------
        ddT_dTrhl : float
            Derivative of the temperature difference to the return temperature.
        """
        return -1


    def ddT_der_Tr(self):
        """
        Derivative of the temperature difference to the nodal return temperature.

        Returns
        -------
        ddT_dTr : float
            Derivative of the temperature difference to the return temperature.
        """
        return self.ddT_der_Trhl() * self.return_temperature_der_Tr()


    def flow(self):
        """
        Determines the flow through the half link as a function of heat power and outflow temperature.

        Returns
        -------
        m : float
            Half link flow.
        """
        return self.m_of_phi(self.get_dphi(), self.get_Ts(), self.get_Tr(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def heat(self, scale_var=None, scale_var_params=None, T_shift=None):
        """
        Determines the heat power through the half link as a function of flow and outflow temperature.

        Returns
        -------
        phi : float
            Half link heat power.
        """
        return self.phi_of_m(self.get_m(), self.supply_temperature(), self.return_temperature(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def supply_temperature_der_Ts(self):
        """
        Derivative of the half link temperature near supply line to the nodal supply temperature.

        Returns
        -------
        dTshl_dTs : float
            Derivative of the link flow to the supply temperature.
        """
        if self.start_node.node_type in [9, 10, 11]: # general slack nodes
            dTshl_dTs = 1
        elif self.sink:
            dTshl_dTs = 1
        else:
            dTshl_dTs = 0
            
        return dTshl_dTs


    def return_temperature_der_Tr(self):
        """
        Derivative of the half link temperature near return line to the nodal return temperature.

        Returns
        -------
        dTrhl_dTr : float
            Derivative of the link flow to the supply temperature
        """
        if self.start_node.node_type in [9, 10, 11]: # general slack nodes
            dTrhl_dTr = 1
        elif self.sink:
            dTrhl_dTr = 0
        else:
            dTrhl_dTr = 1
            
        return dTrhl_dTr


    def m_der_Ts(self):
        """
        Derivative of the half link flow (as a function of heat) to the nodal supply temperature.

        Returns
        -------
        dm_dTs : float
            Derivative of the link flow to the supply temperature.
        """
        if self.start_node.node_type in [0, 8, 9, 10, 11]:  # slack nodes, so m is expressed via conservation of mass, not as function of heat power
            return 0
        else:
            return self.dm_dTs(self.get_dphi(), self.supply_temperature(), self.return_temperature(), scale_var=self.scale_var, scale_var_params=self.scale_var_params) * \
                   self.supply_temperature_der_Ts()


    def m_der_Tr(self):
        """
        Derivative of the half link flow (as a function of heat) to the return temperature.

        Returns
        -------
        dm_dTr : float
            Derivative of the link flow to the supply temperature.
        """
        if self.start_node.node_type in [0, 8, 9, 10, 11]:  # slack nodes, so m is expressed via conservation of mass, not as function of heat power
            return 0
        else:
            return self.dm_dTr(self.get_dphi(), self.supply_temperature(), self.return_temperature(), scale_var=self.scale_var, scale_var_params=self.scale_var_params) * \
                   self.return_temperature_der_Tr()


    def phi_der_m(self):
        """
        Derivative of the half link heat power difference to the half link flow.

        Returns
        -------
        dphi_dm : float
            Derivative of the heat power to flow.
        """
        return self.dphi_dm(self.get_m(), self.supply_temperature(), self.return_temperature(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def phi_der_Tshl(self):
        """
        Derivative of the half link heat power difference to the half link temperature near supply line.

        Returns
        -------
        dphi_dTshl : float
            Derivative of the half link heat to the supply temperature
        """
        return self.dphi_dTs(self.get_m(), self.return_temperature(), self.start_node.get_Ts(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def phi_der_Ts(self):
        """
        Derivative of the half link heat power difference to the nodal supply temperature.

        Returns
        -------
        dphi_dTs : float
            Derivative of the half link heat to the supply temperature.
        """
        return self.dphi_dTs(self.get_m(), self.return_temperature(), self.start_node.get_Ts(), scale_var=self.scale_var, scale_var_params=self.scale_var_params) * self.supply_temperature_der_Ts()


    def phi_der_Trhl(self):
        """
        Derivative of the half link heat power difference to the half link temperature near return line.

        Returns
        -------
        dphi_dTrhl : float
            Derivative of the half link heat to the return temperature.
        """
        return self.dphi_dTr(self.get_m(), self.supply_temperature(), self.start_node.get_Tr(), scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def phi_der_Tr(self):
        """
        Derivative of the half link heat power difference to the nodal return temperature.

        Returns
        -------
        dphi_dTr : float
            Derivative of the half link heat to the return temperature.
        """
        return self.dphi_dTr(self.get_m(), self.supply_temperature(), self.start_node.get_Tr(), scale_var=self.scale_var, scale_var_params=self.scale_var_params) * self.return_temperature_der_Tr()


    def supply_temperature(self):
        """
        Determine the temperature near the supply line, based on actual direction of flow. 
        Possibly a function of temperature at end of the link.

        Returns
        -------
        Ts : float
            Supply temperature.
        """
        if self.sink:
            return self.start_node.get_Ts()
        else:
            return self.get_Ts()


    def return_temperature(self):
        """
        Determine the temperature near the return line, based on actual direction of flow. 
        Possibly a function of temperature at end of the link.

        Returns
        -------
        Tr : float
            Return temperature.
        """
        if self.source and isinstance(self.start_node, HeatNode):
            return self.start_node.get_Tr()
        else:
            return self.get_Tr()


    def supply_heat_power(self):
        """
        Determine the heat power near the supply line, as a function of temperature and mass flow.

        Returns
        -------
        phis_start : float
            Heat power in supply line at start of the link.
        """
        return self.link_params['carrier'].get_Cp(scale_var=self.scale_var, scale_var_params=self.scale_var_params) * self.get_m() * self.get_Ts()


    def return_heat_power(self):
        """
        Determine the heat power near the return line, as a function of temperature and mass flow.

        Returns
        -------
        phir_start : float
            Heat power in return line at start of the link.
        """
        return -self.link_params['carrier'].get_Cp(scale_var=self.scale_var, scale_var_params=self.scale_var_params) * self.get_m() * self.get_Tr()