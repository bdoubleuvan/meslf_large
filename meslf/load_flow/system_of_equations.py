"""
Base class to create the (non-linear) system of equations, and the Jacobian matrix, for steady-state load flow analysis.
"""

import abc
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sps
import time

# %% Base

class NonLinearSystem(metaclass=abc.ABCMeta):
    """
    Abstract class that creates the non-linear system of equations F(x) = 0
    and the corresponding Jacobian matrix J(x).
    """
    @abc.abstractmethod
    def F(self, x):
        """
        Abstract (instance) method to determine F(x).

        Parameters
        ----------
        x : np array
            Variable vector, possible scaled.

        Returns
        -------
        F : np array
            (non-linear) system of equations evaluated at x
        """

    @abc.abstractmethod
    def J(self, x):
        """
        Abstract (instance) method to determine J(x), based on analytical expressions.

        Parameters
        ----------
        x : np array
            Variable vector, possible scaled.

        Returns
        -------
        J : sps matrix
            Jacobian matrix evaluated at x
        """

# %% Gas

class NonLinearSystemGas(NonLinearSystem):
    """
    Class that creates the (non-linear) system of equations F(x) = 0
    and the corresponding Jacobian matrix J(x) for a gas network.
    """

    def __init__(self, network):
        """
        Creates a NonLinearSystemGas object.
        """
        self.network = network
                
        self.index_x = []
        self.index_q = []
        self.index_p = []
        self.index_F = []
        self.index_Fn = []
        self.index_Fl = []
                
        for element in self.network.x_entries:
            self.index_x.append(element.number)
            
            if 'Link' in type(element).__name__:
                self.index_q.append(element.number)
            elif 'Node' in type(element).__name__:
                self.index_p.append(element.number)
                
        for element in self.network.F_entries:
            self.index_F.append(element.number)
            
            if 'Link' in type(element).__name__:
                self.index_Fl.append(element.number)
            elif 'Node' in type(element).__name__:
                self.index_Fn.append(element.number)
                
        self.F_values = np.zeros(len(self.index_F))
        self.J_values = None
        
        self.dFl_der_p_row = []
        self.dFl_der_p_col = []
        for i, link in enumerate(self.network.links):
            self.dFl_der_p_row.append(i)
            self.dFl_der_p_col.append(link.start_node.number)
            
            self.dFl_der_p_row.append(i)
            self.dFl_der_p_col.append(link.end_node.number)
    
                
    def F(self, *args, **kwargs):
        """
        Determines F(x) for a gas network.

        Returns
        -------
        F : np array
            Non-linear system of equations evaluated at x.
        """
        for i, element in enumerate(self.network.F_entries):
            if i < len(self.index_Fn):
                self.F_values[i] = element.node_law()
            else:
                self.F_values[i] = element.link_equation()
                
        return self.F_values


    def J(self, *args, return_full=False, **kwargs):
        """
        Determines J(x) for a gas network, based on analytical expressions.

        Parameters
        ----------
        return_full : boolean
            True, whole Jacobian including state and derived variables. 
            False, only returns Jacobian related to the state variable.
            Default is False.

        Returns
        -------
        J : np array
            Jacobian matrix evaluated at x.
        """        
        if self.network.formulation == 'nodal':
            diag_data = []
            dp_der_data = []
            dp_der_row = []
            dp_der_col = []
            
            for i, element in enumerate(self.network.links):
                diag_data.append(-element.f_der_dp())
                der_start, der_end = element.dp_der_p()
                
                dp_der_data.append(der_start)
                dp_der_row.append(i)
                dp_der_col.append(element.start_node.number)

                dp_der_data.append(der_end)
                dp_der_row.append(i)
                dp_der_col.append(element.end_node.number)
                    
            D_f_der_dp = sps.diags(diag_data)
            dp_der = sps.csr_matrix((dp_der_data, (dp_der_row, dp_der_col)), 
                                    shape=(self.network.number_of_links, self.network.number_of_nodes))
            
            if return_full:
                self.J_values = (self.network.A.dot(D_f_der_dp)).dot(dp_der)
            else:
                dp_der_tilde = dp_der[:, self.index_x]
                A_prime = self.network.A[self.index_F, :]
                self.J_values = (A_prime.dot(D_f_der_dp)).dot(dp_der_tilde)
        elif self.network.formulation == 'full':
            dFq_dq = np.zeros(self.network.number_of_links)
            
            dFl_der_p_data = []
            
            for i, link in enumerate(self.network.links):
                dFq_dq[link.number] = link.f_der_q()
                
                dFl_der_p_start, dFl_der_p_end = link.f_der_p()
                dFl_der_p_data.append(dFl_der_p_start)
                dFl_der_p_data.append(dFl_der_p_end)
            
            dFl_dp = sps.csr_matrix((dFl_der_p_data, (self.dFl_der_p_row, self.dFl_der_p_col)), shape=(self.network.number_of_links, self.network.number_of_nodes))
            dFl_dq = sps.diags(dFq_dq).tocsr()
            
            if return_full:
                J = sps.bmat([[self.network.A, None], [dFl_dq, dFl_dp]]).tocsr()
            else:
                J = sps.bmat([[self.network.A[self.index_Fn, :][:, self.index_q], None],
                              [dFl_dq[self.index_Fl, :][:, self.index_q], dFl_dp[self.index_Fl, :][:, self.index_p]]]).tocsr()
        
        return J
        
        
    def p_check(self, x, mode='local'):
        """
        Changes negative pressure to positive. 

        Parameters
        ----------
        x : np array
            Variable vector x.

        mode : str
            'global' only works properly if the pressure drop is quadratic for every link. 
            Otherwise it gives wrong answer. Use 'local' if not all links have quadratic pressure drop.
            
        Returns
        -------
        x : np array
           Variable vector x with positive pressure values
        """
        
        if mode == 'global':
            if self.network.formulation == 'full':
                x[-self.network.number_of_unknown_p:] = np.abs(x[-self.network.number_of_unknown_p:])
            elif self.network.formulation == 'nodal':
                x = np.abs(x)   
        elif mode == 'local':
            if len(self.network.index_p_high) == 0:
                if self.network.formulation == 'full':
                        for i, element in enumerate(self.network.x_entries):
                            all_high = True
                            if 'Node' in str(type(element)):
                                for link in element.get_links():
                                    if ('Half' not in str(type(link))) and ('high' not in link.link_type):
                                        all_high = False
                                        break
                            if all_high:
                                self.network.index_p_high.append(i)
                elif self.network.formulation == 'nodal':
                    for i, element in enumerate(self.network.x_entries):
                        for link in element.get_links():
                                if 'high' in link.link_type: # if first encounter with high pressure model
                                    self.network.index_p_high.append(i)
                                    break
                                
            x[self.network.index_p_high] = np.abs(x[self.network.index_p_high])
        else:
            pass
                
        return x

# %% Electrical

class NonLinearSystemElectrical(NonLinearSystem):
    """
    Class that creates the (non-linear) system of equations F(x)=0
    and the corresponding Jacobian matrix J(x) for an electrical network.
    """

    def __init__(self, network):
        """
        Creates a NonLinearSystemElectrical obJ_ect.

        Parameters
        ----------
        network : ElectricalNetwork
            Electrial network for which the sytem of equations is made.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params : dict
            Dictionary with parameters needed for scaling.
        """
        self.network = network
                
        self.index_FP = []
        self.index_FQ = []
        self.index_delta = []
        self.index_V = []
        
        self.index_dummy_link_start = []
        self.index_dummy_link_end = []

        self.V = []
        self.delta = []
        
        self.set_known_P = set(self.network.known_P_nodes)
        self.set_known_Q = set(self.network.known_Q_nodes)
        self.set_unknown_V = set(self.network.unknown_V_nodes)
        self.set_unknown_delta = set(self.network.unknown_delta_nodes)
        
        for i, node in enumerate(self.network.nodes):
            self.V.append(node.get_V())
            self.delta.append(node.delta)
                  
            if node in self.set_known_P:
                self.index_FP.append(i)
            if node in self.set_known_Q:
                self.index_FQ.append(i)
            if node in self.set_unknown_V:
                self.index_V.append(i)
            if node in self.set_unknown_delta:
                self.index_delta.append(i)
            
        for link in self.network.dummy_links:
            index = self.network.nodes.index(link.start_node)
            self.index_dummy_link_start.append(index)
            
            index = self.network.nodes.index(link.end_node)
            self.index_dummy_link_end.append(index)
            
        self.V = np.array(self.V)
        self.delta = np.array(self.delta)
          
        self.F_values = np.zeros(len(self.network.known_P_nodes)+len(self.network.known_Q_nodes))
        self.J_values = None
        
        self.first = True
 
                
    def delta_check(self, x):
        x[:len(self.network.unknown_delta_nodes)] = x[:len(self.network.unknown_delta_nodes)] % (2*np.pi)
        
        return x


    def F(self, *args, **kwargs):
        """
        Determines F(x) for an electrical network.

        Returns
        -------
        F : np array
            (non-linear) system of equations evaluated at x
        """        
        for i, node in enumerate(self.network.known_P_nodes):
            fP = node.node_law()[0]
            self.F_values[i] = fP
       
        offset = len(self.network.known_P_nodes)
        for i, node in enumerate(self.network.known_Q_nodes):
            fQ = node.node_law()[1]
            self.F_values[i + offset] = fQ
            
        return self.F_values


    def J(self, x, return_full=False):
        """
        Determines J(x) for an electrical network, based on analytical expressions.

        Parameters
        ----------
        x : np array
            Variable vector, possible scaled.

        Returns
        -------
        J : np array
            Jacobian matrix evaluated at x
        """        
        self.delta[self.index_delta] = x[:len(self.network.unknown_delta_nodes)]
        if self.network.dummy_links:
            self.V[self.index_V] = x[len(self.network.unknown_delta_nodes):-2*len(self.network.dummy_links)]
        else:
            self.V[self.index_V] = x[len(self.network.unknown_delta_nodes):]
          
        V = self.V*np.exp(self.delta*1j)
        V_abs_inv = sps.diags(abs(V)**-1)
        I = sps.diags(self.network.Y.dot(V))
        V = sps.diags(V)
        
        dS_ddelta = 1j*V.dot(I.conjugate() - (self.network.Y.dot(V)).conjugate())
        dP_ddelta = dS_ddelta.real
        dQ_ddelta = dS_ddelta.imag
        
        dS_dV = (V.dot(I.conjugate() + (self.network.Y.dot(V)).conjugate())).dot(V_abs_inv)
        dP_dV = dS_dV.real
        dQ_dV = dS_dV.imag
        
        if self.first:
            self.first = False
            # self.iterations = 0
            if self.network.dummy_links:
                data_P = []
                row_P = []
                col_P = []
                data_Q = []
                row_Q = []
                col_Q = []
                for i, link in enumerate(self.network.dummy_links):
                    data_P.append(1) # P_start
                    row_P.append(self.index_dummy_link_start[i])
                    col_P.append(i)
                    
                    data_Q.append(1) # Q_start
                    row_Q.append(self.index_dummy_link_start[i])
                    col_Q.append(i)
                    
                    data_P.append(-1) # P_end
                    row_P.append(self.index_dummy_link_end[i])
                    col_P.append(i)
                    
                    data_Q.append(-1) # Q_end
                    row_Q.append(self.index_dummy_link_end[i])
                    col_Q.append(i)
                
                self.dP_dP = sps.csr_matrix((data_P, (row_P, col_P)), shape=(len(self.network.nodes), len(self.network.dummy_links)))
                self.dQ_dQ = sps.csr_matrix((data_Q, (row_Q, col_Q)), shape=(len(self.network.nodes), len(self.network.dummy_links)))
                
                if not return_full:
                    self.dP_dP = self.dP_dP[self.index_FP, :]
                    self.dQ_dQ = self.dQ_dQ[self.index_FQ, :]
                    
            else:
                self.dP_dP = None
                self.dQ_dQ = None
        
        if return_full:
            J = sps.bmat([[dP_ddelta, dP_dV, self.dP_dP, None],
                          [dQ_ddelta, dQ_dV, None, self.dQ_dQ]])
        else:
            J = sps.bmat([[dP_ddelta[self.index_FP, :][:, self.index_delta], dP_dV[self.index_FP, :][:, self.index_V],
                           self.dP_dP, None],
                          [dQ_ddelta[self.index_FQ, :][:, self.index_delta], dQ_dV[self.index_FQ, :][:, self.index_V],
                           None, self.dQ_dQ]])
        
        
        # if self.iterations == 0:
        #     print("Shape = {} x {}".format(J.shape[0], J.shape[1]))
        #     plt.figure(figsize=(8, 8), dpi=1000)
        #     plt.spy(J, aspect='equal', marker=',')
        #     plt.grid()
        #     plt.savefig('jacobian_{}.png'.format(self.iterations), bbox_inches='tight', pad_inches=0.1)
        #     self.iterations += 1
                                    
        return J.tocsr()

# %% Heat

class NonLinearSystemHeat(NonLinearSystem):
    pass

# %% Heterogeneous

class NonLinearSystemHeterogeneous(NonLinearSystem):
    """
    Class that creates the system of equations F(x) = 0 and the corresponding Jacobian matrix J(x) for a heterogeneous network.
    """

    def __init__(self, network):
        """
        Creates a NonLinearSystemHeterogeneous object.

        Parameters
        ----------
        network : HeterogeneousNetwork
            Heterogeneous network for which the sytem of equations is made.
        """
        self.network = network

        self.nlsys_gas = []
        for network in self.network.get_networks():
            if 'GasNetwork' in type(network).__name__:
                self.nlsys_gas.append(NonLinearSystemGas(network))
        
        self.nlsys_electrical = []
        for network in self.network.get_networks():
            if 'ElectricalNetwork' in type(network).__name__:
                self.nlsys_electrical.append(NonLinearSystemElectrical(network))
                
        self.F_values = np.zeros(len(self.network.F_entries))
        self.J_gg = None
        self.J_ee = None
        self.J_cc = None
        
        self.set_unknown_q_links = set(self.network.unknown_q_links)
        self.set_unknown_q_halflinks = set(self.network.unknown_q_halflinks)
        self.set_unknown_P_links = set(self.network.unknown_P_links)
        self.set_unknown_P_halflinks = set(self.network.unknown_P_halflinks)
                
        self.initial_diagonal = True
        self.initial_off_diagonal = True


    def F(self, *args, **kwargs):
        """
        Determines F(x) for a heterogeneous network.

        Returns
        -------
        F : np array
            Non-linear system of equations evaluated at x.
        """
        # Homogeneous part
        for nlsys in self.nlsys_gas+self.nlsys_electrical:
            self.F_values[nlsys.network.F_start_index:nlsys.network.F_end_index] = nlsys.F()
        
        # Heterogeneous part
        for i, node in enumerate(self.network.F_c_entries, start=self.network.F_start_index):
            self.F_values[i] = node.node_law()
            
        return self.F_values


    def J(self, x, *args, return_full=False, **kwargs):
        """
        Determines J(x) for a heterogeneous network, based on analytical expressions.

        Parameters
        ----------
        x : np array
            Variable vector, possible scaled.

        Returns
        -------
        J : np array
            Jacobian matrix evaluated at x.
        """         
        for nlsys in self.nlsys_gas:
            self.J_gg = nlsys.J(x[nlsys.network.x_start_index:nlsys.network.x_end_index])
        
        for nlsys in self.nlsys_electrical:
            self.J_ee = nlsys.J(x[nlsys.network.x_start_index:nlsys.network.x_end_index])
        
        if self.initial_diagonal: # coupling part (diagonal block in Jacobian)
            self.J_cc_row = []
            self.J_cc_col = []
        J_cc_data = []
        
        for i, node in enumerate(self.network.F_c_nodes):
            df_c_dE = node.dnode_law_dE()
            df_c_dq = df_c_dE[0]
            df_c_dP = df_c_dE[1]
                
            for link in node.get_links():
                if link in self.set_unknown_q_links:
                    if self.initial_diagonal:
                        self.J_cc_row.append(i)
                        self.J_cc_col.append(self.network.unknown_q_links.index(link))
                    J_cc_data.append(df_c_dq)
                elif link in self.set_unknown_q_halflinks:
                    if self.initial_diagonal:
                        self.J_cc_row.append(i)
                        self.J_cc_col.append(len(self.network.unknown_q_links) + self.network.unknown_q_halflinks.index(link))
                    J_cc_data.append(df_c_dq)
                elif link in self.set_unknown_P_links:
                    if self.initial_diagonal:
                        self.J_cc_row.append(i)
                        self.J_cc_col.append(len(self.network.unknown_q_links) + len(self.network.unknown_q_halflinks) + self.network.unknown_P_links.index(link))
                    J_cc_data.append(df_c_dP)
                elif link in self.set_unknown_P_halflinks:
                    if self.initial_diagonal:
                        self.J_cc_row.append(i)
                        self.J_cc_col.append(len(self.network.unknown_q_links) + len(self.network.unknown_q_halflinks) + len(self.network.unknown_P_links) + self.network.unknown_P_halflinks.index(link))
                    J_cc_data.append(df_c_dP)
                    
        self.initial_diagonal = False
  
        if J_cc_data:
            self.J_cc = sps.csr_matrix((J_cc_data, (self.J_cc_row, self.J_cc_col)), shape=(len(self.network.F_c_nodes), len(self.network.x_c_entries)))

        if self.initial_off_diagonal:  # off-diagonal matrices
            if J_cc_data:
                self.J_gc_row = []
                self.J_gc_col = []
                self.J_gc_data = []
                self.J_ec_row = []
                self.J_ec_col = []
                self.J_ec_data = []
            else:
                self.J_gc_data = None
                self.J_ec_data = None
                
            for i, node in enumerate(self.network.F_c_nodes):
                for link in node.out_links:
                    if ('q' in link.end_node.bc_type) and (link in self.set_unknown_q_links):
                        # dFg_node/dq_c
                        self.J_gc_row.append(self.network.F_g_entries.index(link.end_node))
                        self.J_gc_col.append(self.network.unknown_q_links.index(link))
                        self.J_gc_data.append(1)
                    elif ('P' in link.end_node.bc_type) and (link in self.set_unknown_P_links):
                            # dFP/dP_c_end = -dFP/dP_c_start
                            self.J_ec_row.append(self.network.F_e_entries.index(link.end_node))
                            self.J_ec_col.append(len(self.network.unknown_q_links) + len(self.network.unknown_q_halflinks) + self.network.unknown_P_links.index(link))
                            self.J_ec_data.append(-1)
                
                for link in node.in_links:
                    if ('q' in link.start_node.bc_type) and (link in self.set_unknown_q_links):
                        # dFg_node/dq_c
                        self.J_gc_row.append(self.network.F_g_entries.index(link.start_node))
                        self.J_gc_col.append(self.network.unknown_q_links.index(link))
                        self.J_gc_data.append(-1)
                    elif ('P' in link.start_node.bc_type) and (link in self.set_unknown_P_links):
                            # dFP/dP_c_end = -dFP/dP_c_start
                            self.J_ec_row.append(self.network.F_e_entries.index(link.start_node))
                            self.J_ec_col.append(len(self.network.unknown_q_links) + len(self.network.unknown_q_halflinks) + self.network.unknown_P_links.index(link))
                            self.J_ec_data.append(1)
                        
        self.initial_off_diagonal = False
        
        if self.J_gc_data:
            self.J_gc = sps.csr_matrix((self.J_gc_data, (self.J_gc_row, self.J_gc_col)), shape=(self.J_gg.shape[0], self.J_cc.shape[1]))
        else:
            self.J_gc = None
        
        if self.J_ec_data:
            self.J_ec = sps.csr_matrix((self.J_ec_data, (self.J_ec_row, self.J_ec_col)), shape=(self.J_ee.shape[0], self.J_cc.shape[1]))
        else:
            self.J_ec = None

        # construct Jacobian matrix
        J = sps.bmat([[self.J_gg, None,           self.J_gc],
                      [None,      self.J_ee,      self.J_ec],
                      [None,      None,           self.J_cc]], 
                     format='csc')
        
        return J


    def delta_check(self, x):
        for network in self.network.get_networks():
            if 'ElectricalNetwork' in type(network).__name__:
                x[network.x_start_index:network.x_start_index+len(network.unknown_delta_nodes)] = x[network.x_start_index:network.x_start_index+len(network.unknown_delta_nodes)] % (2*np.pi)
        
        return x
    
    
    def p_check(self, x, mode='local'):
        """
        Changes negative pressure to positive. 

        Parameters
        ----------
        x : np array
            Variable vector x.

        mode : str
            'global' only works properly if the pressure drop is quadratic for every link. 
            Otherwise it gives wrong answer. Use 'local' if not all links have quadratic pressure drop.
            
        Returns
        -------
        x : np array
           Variable vector x with positive pressure values
        """
        for network in self.network.get_networks():
            if 'GasNetwork' in type(network).__name__:
                if mode == 'global':
                    if network.formulation == 'full':
                        x[network.x_end_index-network.number_of_unknown_p:network.x_end_index] = np.abs(x[network.x_end_index-network.number_of_unknown_p:network.x_end_index])
                    elif network.formulation == 'nodal':
                        x = np.abs(x)   
                elif mode == 'local':
                    if len(network.index_p_high) == 0:
                        if network.formulation == 'full':
                                for i, element in enumerate(network.x_entries):
                                    all_high = True
                                    if 'Node' in str(type(element)):
                                        for link in element.links:
                                            if ('Half' not in str(type(link))) and ('high' not in link.link_type):
                                                all_high = False
                                                break
                                    if all_high:
                                        network.index_p_high.append(network.x_start_index+i)
                        elif network.formulation == 'nodal':
                            for i, element in enumerate(network.x_entries):
                                for link in element.links:
                                        if 'high' in link.link_type: # if first encounter with high pressure model
                                            network.index_p_high.append(network.x_start_index+i)
                                            break
                                        
                    x[network.index_p_high] = np.abs(x[network.index_p_high])
                else:
                    pass
                
        return x
    
    
    def coupling_bounds_check(self, x):
        if 'HeterogeneousNetwork' in type(self.network).__name__:
            for i, link in enumerate(self.network.unknown_q_links):
                if x[self.network.x_start_index+i] < 0:
                    link.q = 0
                    x[self.network.x_start_index+i] = 0
                elif link.scale_var_params['qbase'] * x[self.network.x_start_index+i] > link.q_max:
                    link.q = link.q_max
                    x[self.network.x_start_index+i] = link.q_max / link.scale_var_params['qbase']

            for i, link in enumerate(self.network.unknown_P_links):
                if x[self.network.x_start_index+len(self.network.unknown_q_links)+i] < 0:
                    link.P_start = 0
                    link.P_end = 0
                    x[self.network.x_start_index+len(self.network.unknown_q_links)+i] = 0
                elif link.scale_var_params['Sbase'] * x[self.network.x_start_index+len(self.network.unknown_q_links)+i] > link.P_max:
                    link.P_start = link.P_max
                    link.P_end = -link.P_max
                    x[self.network.x_start_index+len(self.network.unknown_q_links)+i] = link.P_max / link.scale_var_params['Sbase']
        return x