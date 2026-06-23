"""
Electrical network base class, including Network, Node, and Link.
"""

import numpy as np
import re
import scipy.sparse as sps

import meslf.half_link_equations.electrical as halflink_electrical

from meslf.networks.network import Network, Node, Link, HalfLink
from meslf.link_equations import electrical
from meslf.load_flow.system_of_equations import NonLinearSystemElectrical
from meslf.load_flow.non_linear_solvers import *

# %% Network

class ElectricalNetwork(Network):
    """
    Class for electrical networks which is a subclass of Network.

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
    Y : scipy sparse csr_matrix
        Admittance incidence matrix.
    known_P_nodes : list
        Collection of nodes with known active power.
    known_Q_nodes : list
        Collection of nodes with known reactive power.
    unknown_V_nodes : list
        Collection of nodes with unknown voltage magnitude.
    unknown_delta_nodes : list
        Collection of nodes with unknown voltage angle.  
    """

    def __init__(self, name, formulation='complex_power'):
        """
        Creates an ElectricalNetwork object.

        Parameters
        ----------
        name : str
            The name of the network.
        formulation : str
            Formulation used to form system of equations. Option is 'complex_power'.
            Default is 'complex_power'.
        """
        super().__init__(name=name)
                        
        self.Y = None
        
        self.known_P_nodes = []
        self.known_Q_nodes = []
        
        self.unknown_V_nodes = []
        self.unknown_delta_nodes = []
        
        self.dummy_links = []        
        self.formulation = formulation


    def add_node(self, node, position=None):
        """
        Adds a node to the network. 
        A node is only added if it is an ElectricalNode.

        Parameters
        ----------
        node : ElectricalNode
            Node object to be added to the network.
        position : integer
            Position (index) in the list of nodes of the network where the node should be inserted. 
            Default is insert at end of list (append).

        Warns
        ------
        UserWarning
            If node is not an instance of ElectricalNode.
        """
        if isinstance(node, ElectricalNode):
            super().add_node(node=node, position=position)


    def add_link(self, link, position=None):
        """
        Adds link to the network. 
        A link can only added if it is am ElectricalLink.
        If the start node or the end node are not yet added to the network, 
        they will be added to the list of nodes. 

        Parameters
        ----------
        link : ElectricalLink
            Link object to be added to the network.
        position : integer
            Position (index) in the list of links of the network where the link should be inserted. 
            Default is insert at end of list (append).

        Raises
        ------
        TypeError
            If link is not an instance of ElectricalLink.
        """
        if isinstance(link, ElectricalLink):
            super().add_link(link, position=position)
        else:
            raise TypeError("Only an ElectricalLink object can be added. Object type is {}.".format(type(link)))
            

    def add_half_link(self, half_link, position=None):
        """
        Adds half_link to the network. 

        A half link can only added if it is an ElectricalHalfLink.
        If the start node is not yet added to the network, 
        it will be added to the list of nodes.

        Parameters
        ----------
        half_link : ElectricalHalfLink
            Half link object to be added to the network.

        Raises
        ------
        TypeError
            If half_link is not an instance of ElectricalHalfLink.
        """
        if isinstance(half_link, ElectricalHalfLink):
            super().add_half_link(half_link, position=position)
        else:
            raise TypeError("Only a ElectricalHalfLink object can be added. Object type is {}.".format(type(half_link)))


    def create_admittance_matrix(self):
        """
        Makes the admittance matrix Y for the unscaled network. 
        Assigns a number to all nodes and links.
        """
        row = []
        col = []
        data = []
            
        # diagonal elements
        for i, node in enumerate(self.nodes):
            data_diag = 0
            
            for link in node.out_links:
                if link.link_type == 'short_line':
                    data_diag += complex(link.g, link.b)
                elif link.link_type == 'pi_line':
                    data_diag += complex(link.g + 0.5*link.g_sh, link.b + 0.5*link.b_sh)
                elif link.link_type == 'pi_line_trafo':
                    data_diag += complex(link.g+ 0.5*link.g_sh, link.b + 0.5*link.b_sh) / abs(link.n)**2 # abs(link.ratio)**2
                    
            for link in node.in_links:
                if link.link_type == 'short_line':
                    data_diag += complex(link.g, link.b)
                elif link.link_type == 'pi_line':
                    data_diag += complex(link.g + 0.5*link.g_sh, link.b + 0.5*link.b_sh)
                elif link.link_type == 'pi_line_trafo':
                    data_diag += complex(link.g + 0.5*link.g_sh, link.b + 0.5*link.b_sh)
            
            for hl in node.get_half_links(link_types=['nodal_shunt']):
                data_diag += complex(hl.g_sh, hl.b_sh)
            
            if data_diag != 0:
                row.append(node.number)
                col.append(node.number)
                data.append(data_diag)
        
        # off-diagonal elements
        for i, link in enumerate(self.links):
            link.number = i
            if link.link_type == 'short_line':
                row.append(link.start_node.number)
                col.append(link.end_node.number)
                data.append(-complex(link.g, link.b))
                
                row.append(link.end_node.number)
                col.append(link.start_node.number)
                data.append(-complex(link.g, link.b))
            elif link.link_type == 'pi_line':
                row.append(link.start_node.number)
                col.append(link.end_node.number)
                data.append(-complex(link.g, link.b))
                
                row.append(link.end_node.number)
                col.append(link.start_node.number)
                data.append(-complex(link.g, link.b))
            elif link.link_type == 'pi_line_trafo':
                row.append(link.start_node.number)
                col.append(link.end_node.number)
                data.append(-complex(link.g, link.b) / link.n.conj()) # data.append(-complex(e.g, e.b)/e.n)
               
                row.append(link.end_node.number)
                col.append(link.start_node.number)
                data.append(-complex(link.g, link.b) / link.n) # data.append(-complex(e.g, e.b)/e.n.conj())

        self.Y = sps.csr_matrix((data, (row, col)), shape=(self.number_of_nodes, self.number_of_nodes))


    def initialize(self):
        """
        Create the admittance matrix.
        Also tracks down network elements corresponding to unknowns and equations.
        """
        for node in self.nodes:
            if 'P' in node.bc_type:
                self.known_P_nodes.append(node)
            if 'Q' in node.bc_type:
                self.known_Q_nodes.append(node)
            if 'V' not in node.bc_type:
                self.unknown_V_nodes.append(node)
            if 'delta' not in node.bc_type:
                self.unknown_delta_nodes.append(node)
     
                
        for link in self.links:
            if link.link_type == 'dummy':
                if (isinstance(link.start_node, ElectricalNode) and isinstance(link.end_node, ElectricalNode)):
                    self.dummy_links.append(link)

                            
        self.create_admittance_matrix()
        
        
        self.set_F_entries()
        self.set_x_entries()
    
    
    def set_x_entries(self):
        """
        Returns all the nodes, links, and half links that have an entry in variable vector x
        
        Returns
        -------
        x_entries : list
        List of all the nodes, links, and half links that contribute to x.
        """        
        if self.formulation == 'complex_power':
            self.x_entries = self.unknown_delta_nodes + self.unknown_V_nodes + 2*self.dummy_links
        else:
            raise ValueError("Enter valid formulation. Only option is 'complex power' at the moment.")
        
        
    def set_F_entries(self):
        """
        Returns all the nodes, links, and half links that have an entry in function vector F
        
        Returns
        -------
        F_entries : list
        List of all the nodes, links, and half links that contribute to F.
        """
        if self.formulation == 'complex_power':
            self.F_entries = self.known_P_nodes + self.known_Q_nodes
        else:
            raise ValueError("Enter valid formulation. Only option is 'complex power' at the moment.")


    def set_x_init(self):
        """
        Creates the initial gues based on the current network parameters.

        Returns
        -------
        x_init : np array
           Initial guess for variable vector x.
        """
        x_init = np.zeros(len(self.x_entries))
        
        for i, node in enumerate(self.unknown_delta_nodes):
            x_init[i] = node.get_delta()
        
        for i, node in enumerate(self.unknown_V_nodes):
            x_init[i+len(self.unknown_delta_nodes)] = node.get_V()
        
        return x_init


    def update(self, x):
        """
        Updates the network given variable vector x.

        Parameters
        ----------
        x : np array
            Variable vector x. 
        """           
        for i, node in enumerate(self.unknown_delta_nodes):
            node.delta = x[i]
            if node.scale_var == 'per_unit':
                node.delta *= node.scale_var_params['deltabase']
                
        offset = len(self.unknown_delta_nodes)
        for i, node in enumerate(self.unknown_V_nodes):
            node.V = x[i + offset]
            if node.scale_var == 'per_unit':
                node.V *= node.scale_var_params['Vbase']
                
        # update active and reactive power on half link
        for hl in self.half_links:
            if hl.link_type == 'nodal_shunt':
                hl.P = hl.get_P_of_V()
                hl.Q = hl.get_Q_of_V()
                if node.scale_var == 'per_unit':
                    hl.P *= hl.scale_var_params['Sbase']
                    hl.Q *= hl.scale_var_params['Sbase']
        
        for i, link in enumerate(self.links):
            if (isinstance(link.start_node, ElectricalNode) and isinstance(link.end_node, ElectricalNode)): # non-coupling links
                if link.link_type != 'dummy':
                    link.P_start = link.P_start_function()
                    link.Q_start = link.Q_start_function()
                    link.P_end = link.P_end_function()
                    link.Q_end = link.Q_end_function()
                    
                    if link.scale_var == 'per_unit':
                        link.P_start *= link.scale_var_params['Sbase']
                        link.Q_start *= link.scale_var_params['Sbase']
                        link.P_end *= link.scale_var_params['Sbase']
                        link.Q_end *= link.scale_var_params['Sbase']
        
        offset += len(self.unknown_V_nodes)
        for i, link in enumerate(self.dummy_links):
            link.P_start = x[i + offset]
            link.Q_start = x[i + offset + len(self.dummy_links)]
            link.P_end = -link.P_start
            link.Q_end = -link.Q_start
            
            if link.scale_var == 'per_unit':
                link.P_start *= link.scale_var_params['Sbase']
                link.Q_start *= link.scale_var_params['Sbase']
                link.P_end *= link.scale_var_params['Sbase']
                link.Q_end *= link.scale_var_params['Sbase']


    def update_full(self):
        """
        Updates all variables present in the network.
        Unlike update(x), not only the values from x are updated, 
        but also all parameters not included in x.

        Parameters
        ----------
        x : np array
            Variable vector x.

        Returns
        -------
        delta : np array
            Array with all nodal voltage angles.
        V : np array
            Array with all nodal voltage amplitudes.
        S_inj : np array
            Array with all injected complex powers.
        P_link : np array
            Array with all link active powers.
        Q_link : np array
            Array with all link reactive powers.
        """
        delta = np.zeros(self.number_of_nodes)
        V = np.zeros(self.number_of_nodes)

        for i, node in enumerate(self.nodes):
            delta[i] = node.delta
            V[i] = node.V
            
            if ('P' not in node.bc_type) and ('Q' not in node.bc_type):
                P_inj, Q_inj = node.node_law()
                if node.scale_var == 'per_unit':
                    P_inj *= node.scale_var_params['Sbase']
                    Q_inj *= node.scale_var_params['Sbase']
                if node.half_links:
                    node.half_links[0].P = -P_inj
                    node.half_links[0].Q = -Q_inj
                else:
                    if type(node.name) is str:
                        name = node.name + "_hl"
                    else:
                        name = str(node.name) + "_hl"
            elif 'P' not in node.bc_type:
                P_inj = -node.node_law()[0]
                if node.scale_var == 'per_unit':
                    node.half_links[0].P = P_inj * node.scale_var_params['Sbase']
                else:
                    node.half_links[0].P = P_inj
            elif 'Q' not in node.bc_type:
                Q_inj = -node.node_law()[1]
                if node.scale_var == 'per_unit':
                    node.half_links[0].Q = Q_inj * node.scale_var_params['Sbase']
                else:
                    node.half_links[0].Q = Q_inj

        S_inj = np.zeros(self.number_of_nodes, dtype=complex)
        for i, node in enumerate(self.nodes):
            for hl in node.half_links:
                S_inj[i] += hl.P + 1j*hl.Q

        P_link = np.zeros(2*self.number_of_links)
        Q_link = np.zeros(2*self.number_of_links)
        for i, link in enumerate(self.links):
            P_link[i] = link.P_start
            Q_link[i] = link.Q_start
            P_link[i+self.number_of_links] = link.P_end
            Q_link[i+self.number_of_links] = link.Q_end

        return delta, V, S_inj, P_link, Q_link
    
    
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


    def solve_network(self, x_init, solver='nr', solver_parameters={}, lin_solver='lu', lin_solver_parameters={}, post_processing=False):
        """
        Solves the steady-state load flow problem for the electrical network.

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
                                  nlsys=NonLinearSystemElectrical(self),
                                  x_init=x_init,
                                  solver_parameters=solver_parameters,
                                  lin_solver=lin_solver,
                                  lin_solver_parameters=lin_solver_parameters,
                                  post_processing=post_processing)

        # update the rest of the network
        delta, V, S_inj, P_link, Q_link = self.update_full()
        
        return x_sol, self.solver.iterations, self.solver.errors, delta, V, S_inj, P_link, Q_link

# %% Node

class ElectricalNode(Node):
    """
    Electrical node class.

    Attributes
    ----------
    name : str
        The name of the node.
    number : int
        Number of the node.
    scale_var : string
        How to scale the variable. Default is no scaling.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    out_links : list
        List of outgoing links and half links connected to the node.
    in_links : list
        List of ingoing links and half links connected to the node.
    half_links : list
        List of half links connected to the node.
    bc_type : list
        List of strings that contains the known variables.
    V : float
        Nodal voltage amplitude, unscaled.
    delta : float
        Nodal voltage angle, unscaled.
    """

    def __init__(self, name, number=None, 
                 scale_var=None, scale_var_params=None,
                 V=1, delta=0, bc_type=[]):
        """
        Creates an ElectricalNode object.

        Parameters
        ----------
        name : str
            Name of the node.
        V : float
            Nodal voltage amplitude, unscaled. Default is 1. 
        delta : float
            Nodal voltage angle, unscaled. Default is 0.
        bc_type : list
            List of string that specifies the known variables.
            Options are: 
            - 'P',
            - 'Q',
            - 'V',
            - 'delta'.
            Default is an empty list which means that all variables are unknown.
            For example, to specify a known active and reactive power, use ['P', 'Q'].
            You can also use 'generator', 'load' and 'slack' as shortcuts.
        """
        super().__init__(name=name, number=number, \
                         scale_var=scale_var, scale_var_params=scale_var_params)
        
        if bc_type == 'generator':
            bc_type = ['P', 'V']
        elif bc_type == 'load':
            bc_type = ['P', 'Q']
        elif bc_type == 'slack':
            bc_type = ['V', 'delta']
            
        self.bc_type = bc_type
        
        self.V = V
        self.delta = delta
        
        
    def get_V(self):
        """
        Get scaled voltage amplitude.

        Returns
        -------
        V : float
            Scaled voltage amplitude.
        """
        if self.scale_var == 'per_unit':   
            return self.V / self.scale_var_params['Vbase']
        else:
            return self.V


    def get_delta(self):
        """
        Get scaled voltage angle.

        Returns
        -------
        delta : float
            Scaled voltage angle.
        """
        if self.scale_var == 'per_unit':
            return self.delta / self.scale_var_params['deltabase']
        else:
            return self.delta


    def node_law(self):
        """
        Node law for an electrical node, which is conservation of complex power. 
        The sum of the active and reactive powers of all incoming and outgoing links and half links.

        Returns
        -------
        fP : float
            The sum of the active powers of all incoming and outgoing links and half links.
        fQ : float
            The sum of the reactive powers of all incoming and outgoing links and half links.
        """
        fP = 0
        fQ = 0
                
        for link in self.in_links:
            fP += link.get_P_end()
            fQ += link.get_Q_end()      
                                 
        for link in self.out_links:
            fP += link.get_P_start()
            fQ += link.get_Q_start()

        for hl in self.half_links:
            fP += hl.get_P()
            fQ += hl.get_Q()
            
        return fP, fQ

# %% Link

class ElectricalLink(Link):
    """
    Electrical link class. 

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
    P_start : float
        Active power at start of the link, unscaled.
    Q_start : float 
        Reactive power at start of the link, unscaled.
    P_end : float
        Active power at end of the link, unscaled.
    Q_end : float 
        Reactive power at end of the link, unscaled.
    bc_type : list
        A list which specifies known variables.
    link_type : string
        Type of the link.
    link_params: dict
        Dictionary of link parameters required by the specific link equation.
    equation : function
        A function that creates the relevant equations.
    P_start_of_V_delta : function
        Active power at the start of link depending on voltage magnitude and voltage angle.
    Q_start_of_V_delta : function
        Reactive power at the start of link depending on voltage magnitude and voltage angle.
    P_end_of_V_delta : function
        Active power at the end of link depending on voltage magnitude and voltage angle.
    Q_end_of_V_delta : function
        Reactive power at the end of link depending on voltage magnitude and voltage angle.
    b : float
        Susceptance.
    g : float
        Conductance.
    b_sh : float
        Shunt susceptance.
    g_sh : float
        Shunt conductance.
    ratio : float
        Transformer ratio magnitude.
    phase_shift : float
        Transformer phase shift in radians.
    n : float
        Transformer ratio.
    """

    def __init__(self, name, start_node, end_node, number=None,
                 scale_var=None, scale_var_params=None,
                 P_start=0, Q_start=0, P_end=0, Q_end=0, P_max=None,
                 bc_type=[], link_params={}, link_type='dummy'):
        """
        Creates a ElectricalLink object.

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
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values required for scaling variables.
        P_start : float
            Active power at start of the link. Default is 0.
        Q_start : float
            Reactive power at start of the link. Default is 0.
        P_end : float
            Active power at end of the link. Default is 0.
        Q_end : float 
            Reactive power at end of the link. Default is 0.
        bc_type : list
            A list which specifies known variables. Variable options are limited to: 
            - 'P_start', 
            - 'Q_start', 
            - 'P_end',
            - 'Q_end'. 
            To specify some variables as known use a list with strings.
            For example, ['P_start', 'Q_end'] means that P_start and Q_end are known.
            Default is an empty list [] meaning that every variable is unknown.
        link_params: dict
            Dictionary of link parameters required by the specific link type. 
            Default is an empty dict.
        link_type : string
            Type of the link. Determines the link equations. Default is 'dummy'. 
            Options are:
            - 'dummy'
            - 'short_line'
            - 'pi_line'
            - 'pi_line_trafo'. 

        Raises
        ------
        ValueError
            If link_type is not a valid link type.
        """
        super().__init__(name=name, start_node=start_node, end_node=end_node, number=number, \
                         scale_var=scale_var, scale_var_params=scale_var_params)
        
        self.P_start = P_start
        self.Q_start = Q_start
        self.P_end = P_end
        self.Q_end = Q_end
        
        self.P_max = P_max
        
        self.bc_type = bc_type
        
        self.link_type = link_type
        self.link_params = link_params
        
        self.b = None
        self.g = None
        self.b_sh = None
        self.g_sh = None
        self.ratio = None
        self.n = None
        
        if self.scale_var == 'per_unit':
            if 'trafo' not in self.link_type:
                self.scale_var_params['Zbase'] = self.scale_var_params['Vbase']**2 / self.scale_var_params['Sbase']
            else:
                self.scale_var_params['Zbase'] = self.scale_var_params['Vbase_to']**2 / self.scale_var_params['Sbase_net']
        
        if self.link_type != 'dummy':
            self.b = link_params['b']
            self.g = link_params['g']
            
            if self.scale_var == 'per_unit':
                self.b *= self.scale_var_params['Zbase']
                self.g *= self.scale_var_params['Zbase']
            
        if 'pi_line' in self.link_type:
            self.b_sh = link_params['b_sh']
            self.g_sh = link_params['g_sh']
                            
            if self.scale_var == 'per_unit':
                self.b_sh *= self.scale_var_params['Zbase']
                self.g_sh *= self.scale_var_params['Zbase']
          
        if self.link_type == 'pi_line_trafo':
            self.phase_shift = link_params['phase_shift']
            self.ratio = link_params['ratio']
            if self.scale_var == 'per_unit':
                self.ratio *= self.scale_var_params['Vbase_to'] / self.scale_var_params['Vbase_from']
            self.n = self.ratio*np.exp(1j*self.phase_shift)
            
                 
        self.equation = None
        if self.link_type == 'dummy':
            self.equation = electrical.dummy
        elif self.link_type == 'short_line':
            self.equation = electrical.short_line
        elif self.link_type == 'pi_line':
            self.equation = electrical.pi_line
        elif self.link_type == 'pi_line_trafo':
            self.equation = electrical.pi_line_trafo
        else:
            raise ValueError("link_type should be either 'dummy', 'short_line', " + \
                             "'pi_line', or 'pi_line_trafo', not {}.".format(link_type))
                
        self.P_start_of_V_delta, self.Q_start_of_V_delta, self.P_end_of_V_delta, \
        self.Q_end_of_V_delta = self.equation()


    def set_type(self, scale_var=None, scale_var_params=None, bc_type=None, link_params=None, link_type=None):
        """
        Set or change the link type, and the corresponding link equations

        Parameters
        ----------
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values required for scaling variables.
        bc_type : list
            A list which specifies known variables. Variable options are limited to: 
            - 'P_start', 
            - 'Q_start', 
            - 'P_end',
            - 'Q_end'. 
            Default is None, meaning that the same bc_type is used.
        link_params : dict
            Dictionary of link parameters required by the specific link type.
            Default is None, meaning that the same link_params are used.
        link_type : str
            Type of the link. Determines the link equations.
            Options are:
            - 'dummy'
            - 'short_line'
            - 'pi_line'
            - 'pi_line_trafo'.
        Default is None, meaning that the same link_type is used.

        Raises
        ------
        ValueError
            If link_type is not a valid link type.
        """
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = self.scale_var_params
        
        if bc_type is not None:
            self.bc_type = bc_type
        
        if link_type is not None:
            self.link_type = link_type
        if link_params is not None:
            self.link_params = link_params
                    
            if self.scale_var == 'per_unit':
                if 'trafo' not in self.link_type:
                    self.scale_var_params['Zbase'] = self.scale_var_params['Vbase']**2 / self.scale_var_params['Sbase']
                else:
                    self.scale_var_params['Zbase'] = self.scale_var_params['Vbase_to']**2 / self.scale_var_params['Sbase_net']
            
            if self.link_type != 'dummy':
                self.b = link_params['b']
                self.g = link_params['g']
                
                if self.scale_var == 'per_unit':
                    self.b *= self.scale_var_params['Zbase']
                    self.g *= self.scale_var_params['Zbase']
                
            if 'pi_line' in self.link_type:
                self.b_sh = link_params['b_sh']
                self.g_sh = link_params['g_sh']
                                
                if self.scale_var == 'per_unit':
                    self.b_sh *= self.scale_var_params['Zbase']
                    self.g_sh *= self.scale_var_params['Zbase']
            
            if self.link_type == 'pi_line_trafo':
                self.phase_shift = link_params['phase_shift']
                self.ratio = link_params['ratio']
                if self.scale_var == 'per_unit':
                    self.ratio *= self.scale_var_params['Vbase_to'] / self.scale_var_params['Vbase_from']
                self.n = self.ratio*np.exp(1j*self.phase_shift)
            
        self.equation = None
        if self.link_type == 'dummy':
            self.equation = electrical.dummy
        elif self.link_type == 'short_line':
            self.equation = electrical.short_line
        elif self.link_type == 'pi_line':
            self.equation = electrical.pi_line
        elif self.link_type == 'pi_line_trafo':
            self.equation = electrical.pi_line_trafo
        else:
            raise ValueError("link_type should be either 'dummy', 'short_line', " + \
                             "'pi_line', or 'pi_line_trafo', not {}.".format(link_type))
                
        self.P_start_of_V_delta, self.Q_start_of_V_delta, \
        self.P_end_of_V_delta, self.Q_end_of_V_delta = self.equation()


    def get_P_start(self):
        """
        Get scaled active power at start of the link.

        Returns
        -------
        P_start : float
            Scaled active power at start of the link.
        """
        if self.scale_var == 'per_unit':
            return self.P_start / self.scale_var_params['Sbase']
        else:
            return self.P_start


    def get_Q_start(self):
        """
        Get scaled reactive power at start of the link.

        Returns
        -------
        Q_start : float
            Scaled reactive power at start of the link.
        """
        if self.scale_var == 'per_unit':
            return self.Q_start / self.scale_var_params['Sbase']
        else:
            return self.Q_start


    def get_P_end(self):
        """
        Get scaled active power at end of the link. 

        Returns
        -------
        P_end : float
            Scaled active power at end of the link. 
        """
        if self.scale_var == 'per_unit':
            return self.P_end / self.scale_var_params['Sbase']
        else:
            return self.P_end


    def get_Q_end(self):
        """
        Get scaled reactive power at end of the link.

        Returns
        -------
        Q_end : float
            Scaled reactive power at end of the link. 
        """
        if self.scale_var == 'per_unit':
            return self.Q_end / self.scale_var_params['Sbase']
        else:
            return self.Q_end


    def V_drop(self):
        """
        Voltage amplitude drop function. 

        Returns
        -------
        dV : float
            Voltage amplitude drop.
        """
        return self.start_node.get_V() - self.end_node.get_V()


    def delta_drop(self):
        """
        Voltage angle drop function.

        Returns
        -------
        ddelta : float
            Voltage angle drop.
        """
        return self.start_node.get_delta() - self.end_node.get_delta()


    def P_start_function(self):
        """
        Determine the active power at the start of the link, 
        as a function of nodal voltage amplitudes and angles.

        Returns
        -------
        P_start : float
            Active power at start of the link.
        """
        return self.P_start_of_V_delta(self.start_node.get_V(), self.end_node.get_V(), \
                                       self.start_node.get_delta(), self.end_node.get_delta(), \
                                       g=self.g, b=self.b, g_sh=self.g_sh, b_sh=self.b_sh, n=self.n)


    def Q_start_function(self):
        """
        Determine the reactive power at the start of the link, 
        as a function of nodal voltage amplitudes and angles.

        Returns
        -------
        Q_start : float
            Reactive power at start of the link.
        """
        return self.Q_start_of_V_delta(self.start_node.get_V(), self.end_node.get_V(), \
                                       self.start_node.get_delta(), self.end_node.get_delta(), \
                                       g=self.g, b=self.b, g_sh=self.g_sh, b_sh=self.b_sh, n=self.n)


    def P_end_function(self):
        """
        Determine the active power at the end of the link, 
        as a function of nodal voltage amplitudes and angles.

        Returns
        -------
        P_end : float
            Active power at end of the link.
        """
        return self.P_end_of_V_delta(self.start_node.get_V(), self.end_node.get_V(), \
                                     self.start_node.get_delta(), self.end_node.get_delta(), \
                                     g=self.g, b=self.b, g_sh=self.g_sh, b_sh=self.b_sh, n=self.n)


    def Q_end_function(self):
        """
        Determine the reactive power at the end of the link, 
        as a function of nodal voltage amplitudes and angles. 

        Returns
        -------
        Q_end : float
            Reactive power at end of the link.
        """
        return self.Q_end_of_V_delta(self.start_node.get_V(), self.end_node.get_V(), \
                                     self.start_node.get_delta(), self.end_node.get_delta(), \
                                     g=self.g, b=self.b, g_sh=self.g_sh, b_sh=self.b_sh, n=self.n)


    def complex_power_loss(self):
        """
        Complex power loss over the link. 

        Returns
        -------
        S_loss : float
            Complex power loss.
        """
        return complex(self.P_start + self.P_end, self.Q_start + self.Q_end)

# %% Half Link

class ElectricalHalfLink(HalfLink):
    """
    Electrical half link class.
    The default is an outflow half link.

    Attributes
    ----------
    name : str
        Name of the half link.
    start_node : Node
        Start node of the half link.
    number : int
        Number of the half link.
    scale_var : string
        How to scale the variable.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    P : float
        Active power, unscaled.
    Q : float 
        Reactive power, unscaled.
    bc_type : list
        Boundary condition of the half link. Use string to denote known variable.
        For example, ['P', 'Q'] means known active and reactive power.
    link_type : string
        Type of the half link, options are 'flow' or 'nodal_shunt'. 
    link_params : dict
        Dictionary of halflink parameters needed for a specific halflink type.
    P_of_V : function
        Active power dependent on nodal voltage.
    Q_of_V : function
        Reactive power dependent on nodal voltage.
    b : float
        Susceptance.
    g: float
        Conductance.
    """

    def __init__(self, name, start_node, scale_var=None, scale_var_params=None, P=0, Q=0, bc_type=[], link_type='flow', link_params={}):
        """
        Creates an ElectricalHalfLink object

        Parameters
        ----------
        name : str
            Name of the half link.
        start_node : Node
            Start node of the half link.
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.
        P : float
            Active power. Default is 0.
        Q : float 
            Reactive power. Default is 0.
        bc_type : list
            Boundary condition of the half link. Use string to denote known variable.
            For example, ['P', 'Q'] means known active and reactive power.
            Default is an empty list, which means that all variables are unknown.
        link_type : string
            Type of the half link, options are 'flow' or 'nodal_shunt'. 
            Default is 'flow', which represents an in- or outflow.
        link_params : dict
            Dictionary of halflink parameters needed for a specific halflink type. 
            Default is an empty dict


        Raises
        ------
        TypeError
            If start_node is not an instance of Node
        ValueError
            If halflink_type is not 'flow' or 'nodal_shunt'.
        """
        super().__init__(name=name, start_node=start_node)
        
        self.bc_type = bc_type
        self.link_type = link_type
        self.link_params = link_params
        
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        self.P = P
        self.Q = Q
        
        self.b_sh = None
        self.g_sh = None
        
        if link_type == 'flow':
            self.P_of_V, self.Q_of_V = halflink_electrical.flow()
        elif link_type == 'nodal_shunt':
            self.b_sh = link_params['b_sh']
            self.g_sh = link_params['g_sh']
            if self.scale_var == 'per_unit':
                self.b_sh /= self.scale_var_params['Sbase'] # like pandapower, normally V^2 / S
                self.g_sh /= self.scale_var_params['Sbase']
            self.P_of_V, self.Q_of_V = halflink_electrical.shunt()
        else:
            raise ValueError("link_type should be either 'flow' or 'nodal_shunt', not {}.".format(link_type))


    def set_type(self, scale_var=None, scale_var_params=None, bc_type=None, link_type=None, link_params=None):
        """
        Set or change the half link type, and the corresponding link equations.

        Parameters
        ----------
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.
        bc_type : list
            Boundary condition of the half link.
        link_type : str
            (New) type of the link. Must be 'flow' or 'nodal_shunt'.
        link_params : dict
            Dictionary with the link parameters required for the (new) link type.

        Raises
        ------
        ValueError
            If link_type is not a valid half link type.
        """
        if bc_type is not None:
            self.bc_type = bc_type
        if link_type is not None:
            self.link_type = link_type
        if link_params is not None:
            self.link_params = link_params
        
        if scale_var is not None:
            self.scale_var = scale_var
        if scale_var_params is not None:
            self.scale_var_params = scale_var_params
        
        if link_type == 'flow':
            self.P_of_V, self.Q_of_V = halflink_electrical.flow()
        elif link_type == 'nodal_shunt':
            self.b_sh = link_params['b_sh']
            self.g_sh = link_params['g_sh']
            if self.scale_var == 'per_unit':
                self.b_sh /= self.scale_var_params['Sbase']
                self.g_sh /= self.scale_var_params['Sbase']
            self.P_of_V, self.Q_of_V = halflink_electrical.shunt()
        else:
            raise ValueError("link_type should be either 'flow' or 'nodal_shunt', not {}.".format(link_type))


    def get_P(self):
        """
        Get scaled active power.

        Returns
        -------
        P : float
            Scaled active power.
        """
        if self.scale_var == 'per_unit':
            return self.P / self.scale_var_params['Sbase']
        else:
            return self.P


    def get_Q(self):
        """
        Get scaled reactive power.

        Returns
        -------
        Q : float
            Scaled reactive power. 
        """
        if self.scale_var == 'per_unit':
            return self.Q / self.scale_var_params['Sbase']
        else:
            return self.Q


    def get_P_of_V(self):
        """
        Determine the active power of the half link as a function of the nodal voltage amplitude.

        Returns
        -------
        P : float
            Active power of the half link.
        """
        return self.P_of_V(self.start_node.get_V(), g_sh=self.g_sh)


    def get_Q_of_V(self):
        """
        Determine the reactive power of the half link as a function of the nodal voltage amplitude.

        Returns
        -------
        Q : float
            Reactive power of the half link.
        """
        return self.Q_of_V(self.start_node.get_V(), b_sh=self.b_sh)