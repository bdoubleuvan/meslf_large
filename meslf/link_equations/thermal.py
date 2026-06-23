"""
Thermal link equations, such as temperature drops for pipes.
"""

import numpy as np

# %% Dummy

def dummy(link_params={}):
    """
    Creates all link equations needed for a dummy link.
    
    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.

    Returns
    --------
    temperature_drop_factor : function
        Temperature drop factor.
    temperature_drop_factor_dm : function
        Derivative of the temperature drop factor to (mass) flow.
    T_end_of_T_start : function
        Temperature at the end of the link, 
        as a function of (mass) flow and temperature at the start of the link. 
        Start and end with respect to actual direction of flow.
    dT_end_dm : function
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, to link mass flow. 
        Start and end with respect to actual direction of flow.
    dT_end_dT_start : function
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, to temperature at start of link. 
        Start and end with respect to actual direction of flow.
    """

    def temperature_drop_factor(m, scale_var=None, scale_var_params=None):
        """
        Temperature drop factor

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return 1


    def temperature_drop_factor_dm(m, scale_var=None, scale_var_params=None):
        """
        Derivate of the temperature drop factor with respect to (mass) flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return 0


    def T_end_of_T_start(m, T_start, *args, scale_var=None, scale_var_params=None, **kwargs):
        """
        Temperature at the end of the link, 
        as a function of of mass flow and temperature at the start of the link. 
        Start and end with respect to actual direction of flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return T_start


    def dT_end_dm(m, T_start, *args, scale_var=None, scale_var_params=None, **kwargs):
        """
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to link mass flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return 0


    def dT_end_dT_start(m, T_start, scale_var=None, scale_var_params=None):
        """
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to temperature at start of link.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return 1

    return temperature_drop_factor, temperature_drop_factor_dm, T_end_of_T_start, dT_end_dm, dT_end_dT_start

# %% Isolated

def perfect_isolated_pipe(link_params={}):
    """
    Creates all link equations needed for a perfectly isolated pipe.
    
    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.

    Returns
    --------
    temperature_drop_factor : function
        Temperature drop factor.
    temperature_drop_factor_dm : function
        Derivative of the temperature drop factor to (mass) flow.
    T_end_of_T_start : function
        Temperature at the end of the link, 
        as a function of (mass) flow and temperature at the start of the link. 
        Start and end with respect to actual direction of flow.
    dT_end_dm : function
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, to link mass flow. 
        Start and end with respect to actual direction of flow.
    dT_end_dT_start : function
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to temperature at start of link. Start and end with respect to actual direction of flow.
    """
    
    def temperature_drop_factor(m, scale_var=None, scale_var_params=None):
        """
        Temperature drop factor.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return 1


    def temperature_drop_factor_dm(m, scale_var=None, scale_var_params=None):
        """
        Derivate of the temperature drop factor with respect to (mass) flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return 0


    def T_end_of_T_start(m, T_start, *args, scale_var=None, scale_var_params=None, **kwargs):
        """
        Temperature at the end of the link, 
        as a function of of mass flow and temperature at the start of the link. 
        Start and end with respect to actual direction of flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return temperature_drop_factor(m, scale_var=scale_var, scale_var_params=scale_var_params) * T_start


    def dT_end_dm(m, T_start, *args, scale_var=None, scale_var_params=None, **kwargs):
        """
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to link mass flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return temperature_drop_factor_dm(m, scale_var=scale_var, scale_var_params=scale_var_params) * T_start


    def dT_end_dT_start(m, T_start, scale_var=None, scale_var_params=None):
        """
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to temperature at start of link.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return temperature_drop_factor(m, scale_var=scale_var, scale_var_params=scale_var_params)

    return temperature_drop_factor, temperature_drop_factor_dm, T_end_of_T_start, dT_end_dm, dT_end_dT_start

# %% Standard

def standard_pipe(link_params={}):
    """
    Creates all link equations needed for a perfectly isolated pipe.

    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    
    Returns
    --------
    temperature_drop_factor : function
        Temperature drop factor.
    temperature_drop_factor_dm : function
        Derivative of the temperature drop factor to (mass) flow.
    T_end_of_T_start : function
        Temperature at the end of the link, 
        as a function of (mass) flow and temperature at the start of the link. 
        Start and end with respect to actual direction of flow.
    dT_end_dm : function
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to link mass flow. Start and end with respect to actual direction of flow.
    dT_end_dT_start : function
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to temperature at start of link. Start and end with respect to actual direction of flow.
    """
    
    def temperature_drop_factor(m, scale_var=None, scale_var_params=None):
        """
        Temperature drop factor (uses the unscaled flow)

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        if scale_var == 'per_unit':
            m *= scale_var_params['qbase']
            
        return np.exp(-np.pi*link_params['D']*link_params['U']*link_params['L'] / (link_params['carrier'].Cp*np.abs(m)))


    def temperature_drop_factor_dm(m, scale_var=None, scale_var_params=None):
        """
        Derivate of the temperature drop factor with respect to (mass) flow (uses the unscaled flow).

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        psi_ac = temperature_drop_factor(m,scale_var=scale_var, scale_var_params=scale_var_params)  # scales m itself
        
        if scale_var == 'per_unit':
            m *= scale_var_params['qbase']
        
        der = np.sign(m) * psi_ac * np.pi*link_params['D'] * link_params['U'] * link_params['L'] / \
              link_params['carrier'].Cp * np.abs(m)**-2
        
        if scale_var == 'per_unit':
            der *= scale_var_params['qbase']
        
        return der


    def T_end_of_T_start(m, T_start, T_shift, scale_var=None, scale_var_params=None):
        """
        Temperature at the end of the link, 
        as a function of of mass flow and temperature at the start of the link. 
        Start and end with respect to actual direction of flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        T_shift : float
            Temperature shift.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        if scale_var == 'per_unit':
            T_shift /= scale_var_params['Tbase']
            
        return temperature_drop_factor(m, scale_var=scale_var, scale_var_params=scale_var_params)*(T_start-T_shift) + T_shift


    def dT_end_dm(m, T_start, T_shift, scale_var=None, scale_var_params=None):
        """
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, to link mass flow.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        T_start : float
            Temperature at start of the link in the supply line.
        T_shift : float
            Temperature shift.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        if scale_var == 'per_unit':
            T_shift /= scale_var_params['Tbase']
            
        return temperature_drop_factor_dm(m, scale_var=scale_var, scale_var_params=scale_var_params)*(T_start-T_shift)


    def dT_end_dT_start(m, scale_var=None, scale_var_params=None):
        """
        Derivative of temperature at start of the link, 
        as function of mass flow and temperature at start of the link, 
        to temperature at start of link.

        Parameters
        ----------
        m : float
            (mass) flow in the link.
        scale_var : string, optional
            How to scale the variable. Default is no scaling.
        scale_var_params: dict, optional
            Dictionary with values needed for scaling variables. Default is None.
        """
        return temperature_drop_factor(m, scale_var=scale_var, scale_var_params=scale_var_params)

    return temperature_drop_factor, temperature_drop_factor_dm, T_end_of_T_start, dT_end_dm, dT_end_dT_start
