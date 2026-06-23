"""
Node equations for coupling nodes.
"""
import numpy as np

# %% Dummy

def dummy(unit_params={}):
    """
    Creates all node equations needed for a dummy node.
    
    Parameters
    ----------
    unit_params : dict
        Contains relevant parameters for the coupling unit.

    Returns
    -------
    node_law : function
        Node law.
    dnode_law_dE : function
        Derivative of node law w.r.t. all relevant energy carriers.
    """
    def node_law(*args, **kwargs):
        pass


    def dnode_law_dE(*args, **kwargs):
        pass

    return node_law, dnode_law_dE


# %% P2G

def p2g(unit_params={}):
    """
    Creates all node equations needed for a Power to Gas (P2G) plant.

    Parameters
    ----------
    unit_params : dict
        Contains relevant parameters for the coupling unit.

    Returns
    -------
    node_law : function
        Node law.
    dnode_law_dE : function
        Derivative of node law w.r.t. all relevant energy carriers.
    """
 
    def node_law(E_in, E_out, scale_var=None, scale_var_params=None, bounded=False):
        """
        Node law of the coupling node, based on conservation of energy.
        Uses outgoing energy as a function of incoming energy.

        Parameters
        ----------
        E_in : float
            Incoming energy, i.e. active power.
        E_out : float
            Outgoing energy, i.e. gas flow.
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.

        Returns
        -------
        f : np array
            Node law.
        """
        P = E_in[1][0]
        q = E_out[0][0]
        
        if bounded:
            if q < 0:
                q = 0
            elif q > unit_params['q_max']:
                q = unit_params['q_max']
                
            if P < 0:
                P = 0
            elif P > unit_params['P_max']:
                P = unit_params['P_max']
            
            # P_ = np.sqrt(P**2 + 10**-6) + P
            # result = unit_params['eta']*P_ - unit_params['GHV']*q
            result = unit_params['eta'] * P - unit_params['GHV'] * q
        else:          
            result = unit_params['eta'] * P - unit_params['GHV'] * q
        
        if scale_var == 'per_unit':
            result /= scale_var_params['Ebase']
        
        return result


    def dnode_law_dE(E_in, E_out, *args, scale_var=None, scale_var_params=None, bounded=False, **kwargs):
        """
        Derivative of node law of the coupling node to outgoing energy.

        Parameters
        ----------
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.       

        Returns
        -------
        df_dE : np array
            Derivative [df/dq, df/dP].
        """
        result = np.array([-unit_params['GHV'], unit_params['eta']])
        
        # if bounded:
        #     P = E_in[1][0]
        #     result[1] *= (P / np.sqrt(P**2 + 10**-6) + 1)

        if scale_var == 'per_unit':
            result[0] /= scale_var_params['GHVbase']
                    
        return result

    return node_law, dnode_law_dE

# %% Gas-fired generator

def gas_fired_generator(unit_params={}):
    """
    Creates all node equations needed for a gas-fired generator.

    Parameters
    ----------
    unit_params : dict
        Contains relevant parameters for the coupling unit.

    Returns
    -------
    node_law : function
        Node law.
    dnode_law_dE : function
        Derivative of node law w.r.t. all relevant energy carriers.
    """
 
    def node_law(E_in, E_out, scale_var=None, scale_var_params=None, bounded=False):
        """
        Node law of the coupling node, based on conservation of energy.
        Uses outgoing energy as a function of incoming energy.

        Parameters
        ----------
        E_in : float
            Incoming energy, i.e. active power.
        E_out : float
            Outgoing energy, i.e. gas flow.
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.

        Returns
        -------
        f : np array
            Node law.
        """
        P = E_out[1][0]
        q = E_in[0][0]

        if bounded:
            if q < 0:
                q = 0
            elif q > unit_params['q_max']:
                q = unit_params['q_max']
                
            if P < 0:
                P = 0
            elif P > unit_params['P_max']:
                P = unit_params['P_max']

            # q_ = np.sqrt(q**2 + 10**-6) + q
            # result = P - unit_params['eta']*unit_params['GHV'] * q_
            result = P - unit_params['eta']*unit_params['GHV'] * q
        else:      
            result = P - unit_params['eta']*unit_params['GHV'] * q

        if scale_var == 'per_unit':
            result /= scale_var_params['Ebase']
                    
        return result


    def dnode_law_dE(E_in, E_out, *args, scale_var=None, scale_var_params=None, bounded=False, **kwargs):
        """
        Derivative of node law of the coupling node to outgoing energy.

        Parameters
        ----------
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.       

        Returns
        -------
        df_dE : np array
            Derivative [df/dq, df/dP].
        """
        result = np.array([-unit_params['eta']*unit_params['GHV'], 1])
        
        if bounded:
            q = E_in[0][0]
            # result[0] *= (q / np.sqrt(q**2 + 10**-6) + 1)
            
        if scale_var == 'per_unit':
            result[0] /= scale_var_params['GHVbase']
        
        return result

    return node_law, dnode_law_dE