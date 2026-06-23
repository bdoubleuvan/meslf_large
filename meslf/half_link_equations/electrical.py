"""
Electrical half link equations, such as a nodal shunt.
"""

# %% flow

def flow(*args, link_params={}, **kwargs):
    """
    Creates the half link equations for a basic (out)flow half link.
    
    Returns
    --------
    P_of_V : function
        Active power of half link (i.e. injected active power) as function of nodal voltage amplitude.
    Q_of_V : function
        Reactive power of half link (i.e. injected reactive power) as function of nodal voltage amplitude.
    """

    def P_of_V(V, scale_var=None, scale_var_params=None):
        pass
    
    def Q_of_V(V, scale_var=None, scale_var_params=None):
        pass
    
    return P_of_V, Q_of_V

# %% shunt

def shunt(*args, **kwargs):
    """
    Creates the half link equations for a shunt half link.
        
    Returns
    --------
    P_of_V : function
        Active power of half link (i.e. injected active power) as function of nodal voltage amplitude.
    Q_of_V : function
        Reactive power of half link (i.e. injected reactive power) as function of nodal voltage amplitude.
    """
    
    def P_of_V(V, *args, g_sh=None, **kwargs):
        """
        Active power of half link (i.e. injected active power) as function of nodal voltage amplitude.
        
        Parameters
        ----------
        V : float
            Voltage amplitude of start node.
        """
        return g_sh * V**2
    
    def Q_of_V(V, *args, b_sh=None, **kwargs):
        """
        Reactive power of half link (i.e. injected reactive power) as function of nodal voltage amplitude.
        
        Parameters
        ----------
        V : float
            Voltage amplitude of start node.
        """
        return -b_sh * V**2
    
    return P_of_V, Q_of_V