"""
Classes needed to create a gas network.
"""

import numpy as np
import re
import scipy.sparse as sps

from meslf.link_equations import hydraulic
from meslf.load_flow.system_of_equations import NonLinearSystemGas
from meslf.load_flow.non_linear_solvers import *
from meslf.networks.network import Network, Node, Link, HalfLink

# %% Network

class GasNetwork(Network):
    """
    Gas network class. Subclass of Network.

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
    formulation : str
        Formulation used to form system of equations.
    A : scipy sparse csr_matrix
        Branch-nodal incidence matrix.
    number_of_unknown_p : int
        Number of unknown p.
    node_known_q : list
        All nodes with known q.
    node_unknown_p : list
        All nodes with unknown p.
    node_link_unknown_q : list
        All links with unknown q.
    link_type_nodal_list : list
        All compatible link types with 'nodal' formulation.
    index_p_high : list
        List with indices of nodes connected with only quadratic pressure drop model (high-pressure).
    """

    def __init__(self, name, formulation='full'):
        """
        Creates a GasNetwork object.

        Parameters
        ----------
        name : str
            The name of the network.
        formulation : str
            Formulation used to form system of equations. Options are 'full' or 'nodal'.
            Default is 'full'.
        """       
        super().__init__(name=name)
        
        self.A = None
        
        self.link_type_nodal_list = ['pipe_low',
                                     'pipe_high',
                                     'resistor',
                                     'resistor_fixed'] # has mass flow in equations
        
        self.number_of_unknown_p = 0
                             
        self.node_known_q = []
        self.node_unknown_p = []
        self.link_unknown_q = []
        self.dummy_link_unknown_q = []
                
        self.formulation = formulation
        
        self.index_p_high = []


    def add_node(self, node, position=None):
        """
        Adds a node to the network.
        A node is only added if it is a GasNode.

        Parameters
        ----------
        node : GasNode
            Node to be added to the network.
        position : integer
            Position (index) in the list of nodes of the network where the node should be inserted. 
            Default is insert at end of list (append).

        Warns
        ------
        UserWarning
            If node is not an instance of GasNode.
        """
        if isinstance(node, GasNode):
            super().add_node(node=node, position=position)


    def add_link(self, link, position=None):
        """
        Adds link to the network.
        A link can only be added if it is a GasLink.
        If the start node or the end node are not yet added to the network, 
        they will be added to the list of nodes.

        Parameters
        ----------
        link : GasLink
            Link to be added to the network.
        position : integer
            Position (index) in the list of links of the network where the link should be inserted. 
            Default is insert at end of list (append).

        Raises
        ------
        TypeError
            If link is not an instance of GasLink.
        """
        if not isinstance(link, GasLink):
            raise TypeError("Only a GasLink object can be added.")
        
        if (self.formulation == 'nodal') and (link.link_type not in self.link_type_nodal_list):
            raise TypeError("Link type '{}' is not compatible with nodal formulation.".format(link.link_type))

        super().add_link(link=link, position=position)


    def add_half_link(self, half_link, position=None):
        """
        Adds half_link to the network.
        A half link can only be added if it a GasHalfLink.
        If the start node is not yet added to the network, 
        it will be added to the list of nodes.

        Parameters
        ----------
        half_link : GasHalfLink
            Half link to be added to the network.
        position : integer
            Position (index) in the list of half links of the network where the half link should be inserted. 
            Default is insert at end of list (append).

        Raises
        ------
        TypeError
            If half_link is not an instance of GasHalfLink.
        """
        if not isinstance(half_link, GasHalfLink):
            raise TypeError("Only a GasHalfLink object can be added.")
        
        super().add_half_link(half_link, position=position)


    def create_incidence_matrix(self):
        """
        Creates the branch-nodal incidence matrix A. 
        It also assigns a number to all nodes and links.
        """
        row = []
        col = []
        data = []
              
        for link in self.links:
            if isinstance(link.start_node, GasNode): # out, check if start_node is in the network, i.e. if it is a GasNode
                row.append(link.start_node.number)
                col.append(link.number)
                data.append(-1)
            if isinstance(link.end_node, GasNode): # in, check if end_node is in the network, i.e. if it is a GasNode
                row.append(link.end_node.number)
                col.append(link.number)
                data.append(1)
                
        self.A = sps.csr_matrix((data, (row, col)), shape=(self.number_of_nodes, self.number_of_links))


    def initialize(self):
        """
        Creates the branch-nodal incidence matrix of the network.
        Also tracks down network elements corresponding to unknowns and equations.
        """
        for node in self.nodes:
            if 'p' not in node.bc_type:
                self.node_unknown_p.append(node)
                self.number_of_unknown_p += 1
                
            if 'q' in node.bc_type:
                self.node_known_q.append(node)
        
        for link in self.links:
            if 'q' not in link.bc_type:
                if link.link_type == 'dummy':
                    if isinstance(link.start_node, GasNode) and isinstance(link.end_node, GasNode):
                        self.dummy_link_unknown_q.append(link)
                else:
                    self.link_unknown_q.append(link)
        
        self.create_incidence_matrix()
        
        self.set_F_entries()
        self.set_x_entries()
       
        
    def set_x_entries(self):
        """
        Creates a list of all the nodes, links, and half links that have an entry in variable vector x.
        
        Returns
        -------
        x_entries : list
           List of all the nodes, links, and half links that contribute to x.
        """
        if self.formulation == 'full':
            self.x_entries = self.link_unknown_q + self.dummy_link_unknown_q + self.node_unknown_p 
        elif self.formulation == 'nodal':
            self.x_entries = self.node_unknown_p
        else:
            raise ValueError("Enter valid formulation. Either 'full' or 'nodal'.")
        

    def set_F_entries(self):
        """
        Creates a list of all the nodes, links, and half links that have an entry in function vector F.
        
        Returns
        -------
        F_entries : list
           List of all the nodes, links, and half links that contribute to F.
        """
        if self.formulation == 'full':
            self.F_entries = self.node_known_q + self.link_unknown_q
        elif self.formulation == 'nodal':
            self.F_entries = self.node_known_q
        else:
            raise ValueError("Enter valid formulation. Either 'full' or 'nodal'.")


    def set_x_init(self):
        """
        Creates the initial guess based on the current network parameters.

        Returns
        -------
        x_init : np array
            Variable vector x, based on the current network values.
        """        
        x_init = np.zeros(len(self.x_entries))
        
        for i, element in enumerate(self.x_entries):
            if isinstance(element, GasLink):
                x_init[i] = element.get_q()
            elif isinstance(element, GasNode):
                x_init[i] = element.get_p()
        
        return x_init
    
    
    def update(self, x):
        """
        Updates the network given variable vector x.

        Parameters
        ----------
        x : np array
            Variable vector x.
        """        
        if self.formulation == 'full':
            for i, element in enumerate(self.x_entries):
                if isinstance(element, GasLink):
                    element.q = x[i]
                    if element.scale_var == 'per_unit':
                        element.q *= element.scale_var_params['qbase']
                elif isinstance(element, GasNode):
                    element.p = x[i] 
                    if element.scale_var == 'per_unit':
                        element.p *= element.scale_var_params['pbase']
        elif self.formulation == 'nodal':
            for i, element in enumerate(self.x_entries):
                element.p = x[i] 
                if element.scale_var == 'per_unit':
                    element.p *= element.scale_var_params['pbase']
            
            for link in self.links: # non-coupling links
                if isinstance(link.start_node, GasNode) and isinstance(link.end_node, GasNode):
                    link.q = link.flow()
                    if element.scale_var == 'per_unit':
                        link.q *= link.scale_var_params['qbase']
        else:
            raise ValueError("Enter valid formulation. Either 'full' or 'nodal'.")


    def update_full(self):
        """
        Updates the full network given variable vector x.
        Unlike update(x), not only the values from x are updated, 
        but also all parameters not included in x.

        Parameters
        ----------
        x : np array
            Variable vector x.

        Returns
        -------
        p : np array
            Array with all unscaled nodal pressures.
        q : np array
            Array with all unscaled link flows.
        q_inj : np array
            Array with all unscaled nodal injected flows.
        """        
        p = np.zeros(self.number_of_nodes)
        q = np.zeros(self.number_of_links)
        q_inj = np.zeros(self.number_of_nodes) # np.zeros(self.number_of_half_links)

        for i, link in enumerate(self.links):
            q[i] = link.q

        q_inj_calc = self.A @ q
        for node in self.nodes:
            p[node.number] = node.p
            
            if 'q' not in node.bc_type: # node.bc_type in self.bc_type_unknown_q_list:
                if node.half_links:
                    for i, hl in enumerate(node.half_links):
                        if i == 0:
                            hl.q = q_inj_calc[node.number]
                        else:
                            node.half_links[0].q -= hl.q
                else:
                    self.add_half_link(GasHalfLink(name=node.name + "_hl", node=node, q=q_inj_calc[node.number]))
            
            for hl in node.half_links:
                q_inj[node.number] += hl.q

        return p, q, q_inj


    def reset_network(self, x):
        """
        Resets the full network to a given vector x.

        Parameters
        ----------
        x_init : np array
            Vector with initial guess for x.
        """
        self.update(x)
        self.update_full()


    def solve_network(self, x_init, solver='nr', solver_parameters={}, lin_solver='lu', lin_solver_parameters={}, post_processing=True):
        """
        Solves the steady-state load flow problem for the gas network.

        Parameters
        ----------
        x_init : array like
            Scaled initial guess.
        solver : string
            Solver used. Default is standard NR. Options are 'NR', 'AA' and 'FP'.
        solver_parameters : dict
            Parameters required for solver saved in a dictionary.
        lin_solver : string
            Linear solver used. Options are:
            'bicgstab',
            'gmres',
            'lsqr',
            'lu'.
            Default is 'lu' (direct solver).
        lin_solver_parameters : dict
            Parameters required for linear solver saved in a dictionary.
        post_processing : bool
            Adjusts the solution after the last solution. For gas networks, 
            the pressures at nodes connected with only high pressure elements are changed to positive pressures.

        Returns
        -------
        x_sol : np array
            Solution vector x, scaled.
        iters : int
            Number of iterations used.
        err_vec : list
            List with the error for every iteration.
        p_sol : np array
            Vector with unscaled nodal pressures.
        q_sol : np array
            Vector with unscaled link flows.
        q_inj : np array
            Vector with unscaled injected nodal flows.
        """
        # solver
        if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
            self.solver = NR(tol=solver_parameters['tol'])
        elif re.fullmatch(r'aa', solver, flags=re.IGNORECASE):
            self.solver = AA(tol=solver_parameters['tol'])
        elif re.fullmatch(r'fp', solver, flags=re.IGNORECASE):
            self.solver = FP(tol=solver_parameters['tol'])

        # solve
        x_sol = self.solver.solve(network=self,
                                  nlsys=NonLinearSystemGas(self),
                                  x_init=x_init,
                                  solver_parameters=solver_parameters,
                                  lin_solver=lin_solver,
                                  lin_solver_parameters=lin_solver_parameters,
                                  post_processing=post_processing)

        # update the rest of the network
        p_sol, q_sol, q_inj = self.update_full()

        return x_sol, self.solver.iterations, self.solver.errors, p_sol, q_sol, q_inj

# %% Node

class GasNode(Node):
    """
    Gas node class.

    Attributes
    ----------
    name : str
        The name of the node.
    number : int
        Number of the node.
    scale_var : string
        How to scale the variable.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    in_links : list
        List of ingoing links connected to the node, except half links.
    out_links : list
        List of outgoing links connected to the node, except half links.
    half_links : list
        List of half links connected to the node.
    bc_type : list
        List of strings that contains the identifier for known variables.
    p : float
        Unscaled nodal pressure.
    """

    def __init__(self, name, number=None, scale_var=None, scale_var_params=None, bc_type=[], p=0):
        """
        Creates a GasNode object.

        Parameters
        ----------
        name : str
            The name of the node.
        number : int
            Number of the node.
        scale_var : string
            How to scale the variable. Default is no scaling. Alternative option is 'per_unit'.
        scale_var_params : dict
            Dictionary with values needed for scaling variables. Default is None.
        bc_type : list
            List of strings that contains the identifier for known variables.
            Options are: 'p' and 'q'.
            You can also use 'load', 'reference' or 'slack' as shortcuts.
        p : float
            Unscaled nodal pressure.

        """
        super().__init__(name=name, number=number,
                         scale_var=scale_var, scale_var_params=scale_var_params)
        
        if bc_type == 'load':
            bc_type = ['q']
        elif bc_type == 'reference':
            bc_type = ['p']
        elif bc_type == 'slack':
            bc_type = []
        self.bc_type = bc_type
        
        self.p = p


    def get_p(self):
        """
        Get nodal pressure with scaling.

        Returns
        -------
        p : float
            Possible scaled nodal pressure.
        """
        if self.scale_var == 'per_unit':
            return self.p / self.scale_var_params['pbase']
        else:
            return self.p


    def node_law(self):
        """
        Node law for a gas node, which is conservation of flow.
        The sum of the gas flows of all incoming and outgoing links and half links. (Both)

        Returns
        -------
        f : float
            The sum of the gas flows of all incoming and outgoing links and half links.
        """
        f = 0
        
        # add mass flow going to the node
        for link in self.in_links:
            f += link.get_q()
        
        # subtract mass flow going from the node
        for link in self.out_links:
            f -= link.get_q()
         
        # subtract injected flow from the node   
        for hl in self.half_links:
            f -= hl.get_q()
        
        return f

# %% Link

class GasLink(Link):
    """
    Gas link class.

    Attributes
    ----------
    name : str
        The name of the link.
    start_node : Node
        Start node of the link.
    end_node : Node
        End node of the link.
    number : int
        Number of the link.
    scale_var : string
        How to scale the variable.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    q : float
        Link flow, unscaled.
    bc_type : list
        A list containing the identifiers of the known variables.
    link_equation_formulation : string
        Determines which link equation formulation is used.
    link_params: dict
        Dictionary of link parameters needed by the specific link equation.
    link_type : string
        Type of the link, e.g. a pipe or compressor. Determines the link equation.
    equation : function
        A function that outputs all functions corresponding with the link.
    f : function
        The link equation.
    df_dq : function
        Derivative of f w.r.t. to mass flow.
    df_ddp : function
        Derivative of f w.r.t. to pressure drop.
    df_dp : function
        Derivative of f w.r.t to start and end pressure.
    fa : function
        The link equation for 'q_of_dp'.
    dfa_dq : function
        Derivative of f w.r.t. to mass flow for 'q_of_dp'.
    dfa_ddp : function
        Derivative of f w.r.t. to pressure drop for 'q_of_dp'.
    dfa_dp : function
        Derivative of f w.r.t to start and end pressure for 'q_of_dp'.
    fb : function
        The link equation for 'dp_of_q'.
    dfb_dq : function
        Derivative of f w.r.t. to mass flow for 'dp_of_q'.
    dfb_ddp : function
        Derivative of f w.r.t. to pressure drop for 'dp_of_q'.
    dfb_dp : function
        Derivative of f w.r.t to start and end pressure for 'dp_of_q'.
    pipe_constant : function
        Pipe constant function.
    dp : function
        Pressure drop function.
    q_of_dp : function
        Mass flow expressed in pressure drop.
    dp_of_q : function
        Pressure drop expressed in mass flow.
    ddp_dp : function
        Derivative of pressure drop w.r.t. start and end pressure.
    ddp_dq : function
        Derivative of pressure drop w.r.t. mass flow.
    dq_ddp : function
        Derative of mass flow w.r.t. pressure drop.
    """

    def __init__(self, name, start_node, end_node, number=None, 
                 scale_var=None, scale_var_params=None,
                 bc_type=[], q=0, q_max=None, link_equation_formulation='dp_of_q', link_params={}, link_type='dummy'):
        """
        Creates a GasLink object.

        Parameters
        ----------
        name : str
            Name of the link.
        start_node : Node
            Start node of the link.
        end_node : Node
            End node of the link.
        number : int
            Number of the link.
        scale_var : string
            How to scale the variable. Default is no scaling. Alternative option is 'per_unit'.
        scale_var_params : dict
            Dictionary with values needed for scaling variables. Default is None.
        q : float
            Link flow, unscaled. Default is 0.
        bc_type : list
            A list containing the identifiers of the known variables. Options are empty list or list containing known variable: 'q'.
            Default is empty list.
        link_equation_formulation : string
            Determines which link equation formulation is used. 
            Default is 'dp_of_q', which uses the pressure drop as a function of the mass flow (i.e. it uses fb). 
            The other option is 'q_of_dp', which uses the mass flow as a function of the pressure drop.
        link_params: dict
            Dictionary of link parameters needed by the specific link equation. 
            Default is an empty dict.
        link_type : string
            Type of the link, e.g. a pipe or compressor. Determines the link equation.  
            Options are: 
            'dummy',
            'pipe_low',
            'pipe_high',
            'compressor',
            'resistor',
            'resistor_fixed,
            'valve'.
            Default is 'dummy'.

        Raises
        ------
        TypeError
            If start_node or end_node is not an instance of Node.
        ValueError
            If link_type or link_equation_formulation is not a valid link type.
        """
        super().__init__(name=name, start_node=start_node, end_node=end_node, number=number, \
                         scale_var=scale_var, scale_var_params=scale_var_params)
        
        self.q = q
        self.q_max = q_max
        
        self.bc_type = bc_type
        
        self.link_equation_formulation = link_equation_formulation
        self.link_params = link_params
        self.link_type = link_type
                
        self.equation = None
        if self.link_type == 'dummy':
            self.equation = hydraulic.dummy
        elif self.link_type == 'pipe_low':
            self.equation = hydraulic.pipe_low
        elif self.link_type == 'pipe_high':
            self.equation = hydraulic.pipe_high
        elif self.link_type == 'compressor':
            self.equation = hydraulic.compressor
            self.scale_var_params['rbase'] = self.start_node.scale_var_params['pbase'] / self.end_node.scale_var_params['pbase']
        elif self.link_type == 'resistor':
            self.equation = hydraulic.resistor
        elif self.link_type == 'resistor_fixed':
            self.equation = hydraulic.resistor_fixed
        elif self.link_type == 'valve':
            self.equation = hydraulic.compressor
        else:
            raise ValueError("link_type should be either 'dummy', \
                             'pipe_low', 'pipe_high', 'compressor' \
                             'resistor' 'resistor_fixed' or 'valve' not {}".format(link_type))
            
        try:
            if link_params['friction'] == 'friction_pole':
                link_params['friction'] = hydraulic.friction_pole
            elif link_params['friction'] == 'friction_weymouth':
                link_params['friction'] = hydraulic.friction_weymouth
        except:
            pass
                     
        self.pipe_constant, self.dp, self.fa, self.fb, \
        self.q_of_dp, self.dp_of_q, self.ddp_dp, self.ddp_dq, self.dq_ddp, \
        self.dfa_ddp, self.dfb_ddp, self.dfa_dp, self.dfb_dp, self.dfa_dq, \
        self.dfb_dq = self.equation(link_params=self.link_params)
                
        if link_equation_formulation == 'q_of_dp':
            self.f = self.fa
            self.df_dq = self.dfa_dq
            self.df_ddp = self.dfa_ddp
            self.df_dp = self.dfa_dp
        elif link_equation_formulation == 'dp_of_q':
            self.f = self.fb
            self.df_dq = self.dfb_dq
            self.df_ddp = self.dfb_ddp
            self.df_dp = self.dfb_dp
        else:
            raise ValueError("link_equation_formulation is not valid. It should be either 'q_of_dp' or 'dp_of_q', not {}.".format(link_equation_formulation))


    def set_type(self, scale_var=None, scale_var_params=None, bc_type=None, link_equation_formulation=None, link_params=None, link_type=None):
        """
        Set or change the link type, and the corresponding link equations.

        Parameters
        ----------
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values required for scaling variables.
        bc_type : int
            Boundary condition of the link. Options are empty list, list containing 'q' or None.
            Default is None, meaning that the same bc_type is not changed.
        link_equation_formulation : string
            Determines which link equation formulation is used.
            Default is None, meaning that the same formulation is used.
        link_params : dict
            Dictionary with the link parameters required for the (new) link type.
            Default is None, meaning that the same link_params are used.
        link_type : str
            Type of the link. Must be one the following:
            'dummy',
            'pipe_low',
            'pipe_high',
            'compressor',
            'resistor',
            'resistor_fixed',
            'valve'.
            Default is None, meaning that the same link_type is used.

        Raises
        ------
        ValueError
            If link_type or link_equation_formulation is not a valid link type.
        """
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        if bc_type is not None:
            self.bc_type = bc_type
        
        if link_equation_formulation is not None:
            self.link_equation_formulation = link_equation_formulation
        if link_params is not None:
            self.link_params = link_params
        if link_type is not None:
            self.link_type = link_type
                
        self.equation = None
        if self.link_type == 'dummy':
            self.equation = hydraulic.dummy
        elif self.link_type == 'pipe_low':
            self.equation = hydraulic.pipe_low
            self.scale_var_params['Cbase'] = self.scale_var_params['pbase'] / self.scale_var_params['qbase']
        elif self.link_type == 'pipe_high':
            self.equation = hydraulic.pipe_high
            self.scale_var_params['Cbase'] = self.scale_var_params['pbase'] / self.scale_var_params['qbase']**2
        elif self.link_type == 'compressor':
            self.equation = hydraulic.compressor
            self.scale_var_params['rbase'] = self.end_node.scale_var_params['pbase'] / self.start_node.scale_var_params['pbase']
        elif self.link_type == 'resistor':
            self.equation = hydraulic.resistor
            self.scale_var_params['Cbase'] = self.scale_var_params['pbase'] / self.scale_var_params['qbase']
        elif self.link_type == 'resistor_fixed':
            self.equation = hydraulic.resistor_fixed
            self.scale_var_params['Cbase'] = self.scale_var_params['pbase']
        elif self.link_type == 'valve':
            self.equation = hydraulic.compressor
            self.scale_var_params['rbase'] = self.end_node.scale_var_params['pbase'] / self.start_node.scale_var_params['pbase']
        else:
            raise ValueError("link_type should be either 'dummy', \
                             'pipe_low', 'pipe_high', 'compressor' \
                             'resistor' 'resistor_fixed' or 'valve' not {}".format(link_type))
            
        if link_params['friction'] == 'friction_pole':
            link_params['friction'] = hydraulic.friction_pole
        elif link_params['friction'] == 'friction_weymouth':
            link_params['friction'] = hydraulic.friction_weymouth
                    
        self.pipe_constant, self.dp, self.fa, self.fb, \
        self.q_of_dp, self.dp_of_q, self.ddp_dp, self.ddp_dq, self.dq_ddp, \
        self.dfa_ddp, self.dfb_ddp, self.dfa_dp, self.dfb_dp, self.dfa_dq, \
        self.dfb_dq = self.equation(link_params=self.link_params)
                
        if link_equation_formulation == 'q_of_dp':
            self.f = self.fa
            self.df_dq = self.dfa_dq
            self.df_ddp = self.dfa_ddp
            self.df_dp = self.dfa_dp
        elif link_equation_formulation == 'dp_of_q':
            self.f = self.fb
            self.df_dq = self.dfb_dq
            self.df_ddp = self.dfb_ddp
            self.df_dp = self.dfb_dp
        else:
            raise ValueError("link_equation_formulation is not valid. It should be either 'q_of_dp' or 'dp_of_q', not {}.".format(link_equation_formulation))


    def get_q(self):
        """
        Get link flow with scaling.

        Parameters
        ----------

        Returns
        -------
        q : float
            Possible scaled link flow.
        """
        if self.scale_var == 'per_unit':
            return self.q / self.scale_var_params['qbase']
        else:
            return self.q


    def dp(self):
        """
        Determines the pressure drop function over the link.
        The pressure drop function is determined by the link type. (Nowhere)

        Parameters
        ----------

        Returns
        -------
        dp : float
            Pressure drop function over the link. Determined by the link type.
        """            
        return self.dp(self.start_node.get_p(), self.end_node.get_p())


    def flow(self):
        """
        Determines the flow through the link as a function of start and end pressures.
        This function is determined by the link type. (Update)

        Parameters
        ----------

        Returns
        -------
        q : float
            Link flow.
        """
        return self.q_of_dp(self.start_node.get_p(), self.end_node.get_p(), \
                            scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def link_equation(self):
        """
        Evaluates the link equation.
        The link equation is determined by the link type. (Full)

        Parameters
        ----------

        Returns
        -------
        f : float
            Link equation f(q,p_start,p_end).
        """
        return self.f(self.get_q(), self.start_node.get_p(), self.end_node.get_p(), \
                      scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def f_der_dp(self):
        """
        Determines the derivative of the link equation to the pressure drop function. (Nodal)

        Parameters
        ----------

        Returns
        -------
        df_ddp : float
            Derivative of the link equation to pressure drop fucntion.
        """
        return self.df_ddp(self.get_q(), self.start_node.get_p(), self.end_node.get_p(), \
                           scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def f_der_p(self):
        """
        Determines the derivative of the link equation to the start and end pressures. (Full)

        Parameters
        ----------

        Returns
        -------
        df_ddp : float
            Derivative of the link equation to pressure drop fucntion.
        """
        return self.df_dp(self.get_q(), self.start_node.get_p(), self.end_node.get_p(), \
                          scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def f_der_q(self):
        """
        Determines the derivative of the link equation to the link flow. (Full)

        Parameters
        ----------
        
        Returns
        -------
        df_dq : float
            Derivative of link equation to link flow.
        """            
        return self.df_dq(self.get_q(), self.start_node.get_p(), self.end_node.get_p(), \
                          scale_var=self.scale_var, scale_var_params=self.scale_var_params)


    def dp_der_p(self):
        """
        Determines the derivative of the pressure drop function to start and end pressures. (Nodal)

        Parameters
        ----------

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """            
        return self.ddp_dp(self.start_node.get_p(), self.end_node.get_p())

# %% Half link

class GasHalfLink(HalfLink):
    """
    Gas half link class.
    The default is an outflow half link.

    Attributes
    ----------
    name : str
        Name of the half link.
    number : int
        Number of the half link.
    start_node : Node
        Start node of the half link.
    scale_var : string
        How to scale the variable.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    q : float
        Gas flow, unscaled.
    bc_type : list
        List containing the identifier for known variables.
    link_params : dict
        Containing relevant link parameters.
    """

    def __init__(self, name, start_node, q=0, scale_var=None, scale_var_params=None, bc_type=[], link_params={}):
        """
        Creates a GasHalfLink object

        Parameters
        ----------
        name : str
            Name of the half link.
        start_node : Node
            Start node of the half link.
        q : float
            Gas flow, unscaled.
        scale_var : string
            How to scale the variable. Default is None, which defaults to scaling at node.
        scale_var_params : dict
            Dictionary with values needed for scaling variables. Default is None, which defaults to scaling at node.
        bc_type : list
            List containing the identifier for known variables. 
            Default is an empty list.
        link_params : dict
            Dictionary of halflink parameters needed for a specific halflink type. 
            Default is an empty dict.
        """
        super().__init__(name=name, start_node=start_node)
        
        self.q = q
        
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        self.bc_type = bc_type
        self.link_params = link_params
      
        
    def get_q(self):
        """
        Get mass flow of half link.

        Returns
        -------
        q : float
            Half link flow.
        """
        if self.scale_var == 'per_unit':
            return self.q / self.scale_var_params['qbase']
        else:
            return self.q
