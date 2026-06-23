"""
Hydraulic (gas and heat) link equations
"""

import numpy as np

# %% dummy

def dummy(link_params={}):
    """
    Creates all link equations needed for a dummy link.
    
    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    """
    
    def pipe_constant(scale_var=None, scale_var_params=None):
        pass


    def dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure.
        p_end : float
            End pressure.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dp : float
            Basic pressure drop, i.e. p_start - p_end.
        """
        return p_start - p_end


    def q_of_dp(p_start, p_end, scale_var=None, scale_var_params=None):
        pass


    def dp_of_q(q, scale_var=None, scale_var_params=None):
        pass


    def fa(q, p_start, p_end, scale_var=None, scale_var_params=None):
        pass


    def fb(q, p_start, p_end, scale_var=None, scale_var_params=None):
        pass


    def ddp_dp(p_start, p_end, scale_var=None, scale_var_parms=None):
        """
        Derivative of pressure drop equation to start and end pressure.

        Parameters
        ----------
        p_start : float
            Start pressure.
        p_end : float
            End pressure.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """
        return 1, -1


    def ddp_dq(q, scale_var=None, scale_var_params=None):
        """
        Derivative of pressure drop equation to mass flow.

        Parameters
        ----------
        q : float
            Mass flow.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of pressure drop to mass flow.
        """
        return 0


    def dq_ddp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure.
        p_end : float
            End pressure.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dq_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return 0


    def dfa_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure.
        p_end : float
            End pressure.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return 0


    def dfb_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure.
        p_end : float
            End pressure.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfb_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return 0


    def dfa_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure.
        p_end : float
            End pressure.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        return 0, 0


    def dfb_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure.
        p_end : float
            End pressure.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        return 0, 0


    def dfa_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return 1


    def dfb_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return 1

    return pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq

# %% pipe_high_pressure

def pipe_high(link_params={}):
    """
    Creates all link equations needed for high pressure pipe flow.

    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    """
        
    def pipe_constant(scale_var=None, scale_var_params=None):
        """
        Pipe constant.

        Parameters
        ----------
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        C : float
            Pipe constant, possibly scaled.
        """
        C = 0.125 * np.pi * np.sqrt(link_params['D']**5 / (link_params['L']*link_params['carrier'].R_gas*link_params['carrier'].T*link_params['carrier'].Z))

        if scale_var == 'per_unit':
            C /= scale_var_params['qbase'] / scale_var_params['pbase']

        return C


    def dp(p_start, p_end):
        """
        Pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        dp : float
            Pressure drop function for the standard pipe equation
        """
        return p_start**2 - p_end**2


    def q_of_dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Mass flow as function of start and end pressures.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        q : float
            Mass flow in kg/s.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        dp_value = dp(p_start, p_end)
        
        return C * np.sign(dp_value) * np.sqrt(np.abs(dp_value) / link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params))


    def dp_of_q(q, scale_var=None, scale_var_params=None):
        """
        Pressure drop as a function of mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dp : float
            Pressure drop function.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params) * C**-2 * q * np.abs(q)


    def fa(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return q - q_of_dp(p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def fb(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return dp(p_start, p_end) - dp_of_q(q, scale_var=scale_var, scale_var_params=scale_var_params)


    def ddp_dp(p_start, p_end):
        """
        Derivative of pressure drop equation to start and end pressure.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """
        return 2*p_start, -2*p_end


    def ddp_dq(q, scale_var=None, scale_var_params=None):
        """
        Derivative of pressure drop equation to mass flow.

        Parameters
        ----------
        q : float
            Mass flow.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        ddp_dq : float
            Derivative of pressure drop to mass flow.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return 2*link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params) * C**-2 * np.abs(q)


    def dq_ddp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dq_ddp : float
            Derivative of mass flow to pressure drop.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        dp_value = dp(p_start, p_end)
        
        return 0.5*C / np.sqrt(np.abs(dp_value)*link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params))


    def dfa_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return -dq_ddp(p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfb_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return 1


    def dfa_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfa_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return 1


    def dfb_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return -ddp_dq(q, scale_var=scale_var, scale_var_params=scale_var_params)

    return pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq

# %% pipe_low_pressure

def pipe_low(link_params={}):
    """
    Creates all link equations needed for a pipe with standard flow in a low pressure system.

    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    """

    def pipe_constant(scale_var=None, scale_var_params=None):
        """
        Pipe constant.

        Parameters
        ----------
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        C : float
            Pipe constant, possibly scaled.
        """
        C = 0.125 * np.pi* np.sqrt(2*link_params['carrier'].pn*link_params['D']**5 / (link_params['L'] * link_params['carrier'].R_gas * link_params['carrier'].Tn))

        if scale_var == 'per_unit':
            C /= scale_var_params['qbase'] / np.sqrt(scale_var_params['pbase'])
        
        return C


    def dp(p_start, p_end):
        """
        Pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        dp : float
            Pressure drop function for the standard pipe equation.
        """
        return p_start - p_end


    def q_of_dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Mass flow as function of start and end pressures.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        q : float
            Mass flow in kg/s.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        dp_value = dp(p_start, p_end)
        
        return C * np.sign(dp_value) * np.sqrt(np.abs(dp_value) / link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params))


    def dp_of_q(q, scale_var=None, scale_var_params=None):
        """
        Pressure drop as a function of mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dp : float
            Pressure drop function.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params) * C**-2 * q * np.abs(q)


    def fa(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return q - q_of_dp(p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def fb(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return dp(p_start, p_end) - dp_of_q(q, scale_var=scale_var, scale_var_params=scale_var_params)


    def ddp_dp(p_start, p_end):
        """
        Derivative of pressure drop equation to start and end pressure.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """
        return 1, -1


    def ddp_dq(q, scale_var=None, scale_var_params=None):
        """
        Derivative of pressure drop equation to mass flow.

        Parameters
        ----------
        q : float
            Mass flow.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of pressure drop to mass flow.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return 2*link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params) * C**-2 * np.abs(q)


    def dq_ddp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dq_ddp : float
            Derivative of mass flow to pressure drop.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        dp_value = dp(p_start, p_end)
        
        return 0.5*C / np.sqrt(np.abs(dp_value) * link_params['friction'](link_params=link_params, scale_var=scale_var, scale_var_params=scale_var_params))


    def dfa_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return -dq_ddp(p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfb_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return 1


    def dfa_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfa_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return 1


    def dfb_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return -ddp_dq(q, scale_var=scale_var, scale_var_params=scale_var_params)

    return pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq

# %% compressor

def compressor(link_params={}):
    """
    Create all link equations needed for a compressor link.

    Parameters
    ----------
    link_params : dict optional
        Contains relevant link parameters.
    """
    
    def pipe_constant(scale_var=None, scale_var_params=None):
        """
        Pipe constant.

        Parameters
        ----------
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
        """
        r = link_params['r']
        
        if scale_var == 'per_unit':
            r /= scale_var_params['rbase']
        
        return r


    def dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Pressure drop function for compressor with a fixed ratio r.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dp : float
            Pressure drop for compressor.
        """
        r = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return r*p_start - p_end


    def q_of_dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Mass flow as function of start and end pressures.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        q : float
            Mass flow in kg/s.
        """
        pass


    def dp_of_q(q, scale_var=None, scale_var_params=None):
        """
        Pressure drop as a function of mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dp : float
            Pressure drop function.
        """
        pass


    def fa(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return -dp(p_start, p_end)


    def fb(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return fa(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def ddp_dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of pressure drop equation to start and end pressure.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """
        r = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return r, -1


    def ddp_dq(q, scale_var=None, scale_var_params=None):
        """
        Derivative of pressure drop equation to mass flow.

        Parameters
        ----------
        q : float
            Mass flow.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of pressure drop to mass flow.
        """
        return 0


    def dq_ddp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dq_ddp : float
            Derivative of mass flow to pressure drop.
        """
        pass


    def dfa_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return -1


    def dfb_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfb_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfa_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the Start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        return dfa_dp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfa_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return 0


    def dfb_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return dfa_dq(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)

    return pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq

# %% resistor

def resistor(link_params={}):
    """
    Create all link equations for a resistor.

    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    """

    def pipe_constant(scale_var=None, scale_var_params=None):
        """
        Pipe constant.

        Parameters
        ----------
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
        """
        C = link_params['C']
        if scale_var == 'per_unit':
            C /= scale_var_params['pbase'] / scale_var_params['qbase']
            
        return C


    def dp(p_start, p_end):
        """
        Pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        dp : float
            Pressure drop function for the standard pipe equation.
        """
        return p_start - p_end


    def q_of_dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Mass flow as function of start and end pressures.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        q : float
            Mass flow in kg/s.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        dp_value = dp(p_start, p_end)
        
        return np.sign(dp_value) * np.sqrt(np.abs(dp_value) / C)


    def dp_of_q(q, scale_var=None, scale_var_params=None):
        """
        Pressure drop as a function of mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dp : float
            Pressure drop function.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return C * q * np.abs(q)


    def fa(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return q - q_of_dp(p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def fb(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return dp(p_start, p_end) - dp_of_q(q, scale_var=scale_var, scale_var_params=scale_var_params)


    def ddp_dp(p_start, p_end):
        """
        Derivative of pressure drop equation to start and end pressure.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """
        return 1, -1


    def ddp_dq(q, scale_var=None, scale_var_params=None):
        """
        Derivative of pressure drop equation to mass flow.

        Parameters
        ----------
        q : float
            Mass flow.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        ddp_dq : float
            Derivative of pressure drop to mass flow.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return 2 * C * np.abs(q)


    def dq_ddp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dq_ddp : float
            Derivative of mass flow to pressure drop.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        dp_value = dp(p_start, p_end)
        
        return 0.5 / np.sqrt(C * np.abs(dp_value))


    def dfa_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return -dq_ddp(p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfb_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return 1


    def dfa_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfa_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfa_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return 1


    def dfb_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return -ddp_dq(q, scale_var=scale_var, scale_var_params=scale_var_params)

    return pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq

# %% resistor with fixed pressure loss

def resistor_fixed(link_params={}):
    """
    Create all link equations needed for a resistor with a fixed pressure loss.

    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    """
    
    def pipe_constant(scale_var=None, scale_var_params=None):
        """
        Pipe constant.

        Parameters
        ----------
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        C : float
            Resistor constant.
        """
        if scale_var == 'per_unit':
            return link_params['C'] / scale_var_params['pbase']
        else:                
            return link_params['C']


    def dp(p_start, p_end):
        """
        Pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        dp : float
            Pressure drop.
        """
        return p_start - p_end


    def q_of_dp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Mass flow as function of start and end pressures.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
        """
        pass


    def dp_of_q(q, scale_var=None, scale_var_params=None):
        """
        Pressure drop as a function of mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        dp : float
            Pressure drop function
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return C * np.sign(q)


    def fa(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
        
        Returns
        -------
        f : float
            Value of link equation.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return C*q - np.abs(q)*dp(p_start, p_end)


    def fb(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Link equation.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        f : float
            Value of link equation.
        """
        return dp(p_start, p_end) - dp_of_q(q, scale_var=scale_var, scale_var_params=scale_var_params)


    def ddp_dp(p_start, p_end):
        """
        Derivative of pressure drop equation to start and end pressure.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.

        Returns
        -------
        ddp_dp_start : float
            Derivative of pressure drop function to the start pressure.
        ddp_dp_end : float
            Derivative of pressure drop function to the end pressure.
        """
        return 1, -1


    def ddp_dq(q, scale_var=None, scale_var_params=None):
        """
        Derivative of pressure drop equation to mass flow.

        Parameters
        ----------
        q : float
            Mass flow.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        ddp_dq : float
            Derivative of pressure drop w.r.t. mass flow
        """
        return 0


    def dq_ddp(p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop function.

        Parameters
        ----------
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
        """
        pass


    def dfa_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfa_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return -np.abs(q)


    def dfb_ddp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of mass flow to pressure drop.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        dfb_ddp : float
            Derivative of mass flow to pressure drop.
        """
        return 1


    def dfa_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfb_dp(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equation to the start and end pressure.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dp_start : float
            Derivative of the link equation to the start pressure.
        df_dp_end : float
            Derivative of the link equation to the end pressure.
        """
        ddp_dp_start, ddp_dp_end = ddp_dp(p_start, p_end)
        
        return ddp_dp_start*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params), ddp_dp_end*dfb_ddp(q, p_start, p_end, scale_var=scale_var, scale_var_params=scale_var_params)


    def dfa_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.
            
        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        C = pipe_constant(scale_var=scale_var, scale_var_params=scale_var_params)
        
        return C - np.sign(q)*dp(p_start, p_end)


    def dfb_dq(q, p_start, p_end, scale_var=None, scale_var_params=None):
        """
        Derivative of link equations to mass flow.

        Parameters
        ----------
        q : float
            Mass flow in kg/s.
        p_start : float
            Start pressure in N/m^2.
        p_end : float
            End pressure in N/m^2.
        scale_var : string
            How to scale the variable. Default is no scaling.
        scale_var_params: dict
            Dictionary with values needed for scaling variables. Default is None.

        Returns
        -------
        df_dq : float
            Derivative of the link equations to the mass flow.
        """
        return -ddp_dq(q, scale_var=scale_var, scale_var_params=scale_var_params)

    return pipe_constant, dp, fa, fb, q_of_dp, dp_of_q, ddp_dp, ddp_dq, dq_ddp, dfa_ddp, dfb_ddp, dfa_dp, dfb_dp, dfa_dq, dfb_dq

# %% friction

def friction_pole(link_params={}, scale_var=None, scale_var_params=None):
    """
    Friction factor for Pole's equations (for low pressure).

    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    scale_var : string
        How to scale the variable. Default is no scaling.
    scale_var_params: dict
        Dictionary with values needed for scaling variables. Default is None.

    Returns
    -------
    friction : float
        The friction factor.
    """
    return 0.0065


def friction_weymouth(link_params={}, scale_var=None, scale_var_params=None):
    """
    Friction factor for the Weymouth equation (for high pressure).

    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    scale_var : string
        How to scale the variable. Default is no scaling.
    scale_var_params: dict
        Dictionary with values needed for scaling variables. Default is None.

    Returns
    -------
    friction : float
        The friction factor.
    """
    return 1 / (20.64**2 * link_params['D']**(1/3) * link_params['E']**2)
