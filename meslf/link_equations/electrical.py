"""
Electrical link equations.
"""

from math import cos, sin

# %% dummy

def dummy(*args, **kwargs):
    """
    Creates all link equations needed for a dummy link.
    
    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
    
    Returns
    --------
    P_start_of_V_delta : function
        Active power at start of line as function of nodal voltage amplitudes and angles.
    Q_start_of_V_delta : function
        Reactive power at start of line as function of nodal voltage amplitudes and angles.
    P_end_of_V_delta : function
        Active power at end of line as function of nodal voltage amplitudes and angles.
    Q_end_of_V_delta : function
        Reactive power at end of line as function of nodal voltage amplitudes and angles.
    """

    def P_start_of_V_delta(*args, **kwargs):
        pass
    
    
    def Q_start_of_V_delta(*args, **kwargs):
        pass
    
    
    def P_end_of_V_delta(*args, **kwargs):
        pass
    
    
    def Q_end_of_V_delta(*args, **kwargs):
        pass
        
    return P_start_of_V_delta, Q_start_of_V_delta, P_end_of_V_delta, Q_end_of_V_delta

# %% short line

def short_line(*args, **kwargs):
    """
    Creates the link equations for a short line model.
    
    Parameters
    ----------
    link_params : dict
        Contains relevant link parameters.
        
    Returns
    --------
    P_start_of_V_delta : function
        Active power at start of line as function of nodal voltage amplitudes and angles.
    Q_start_of_V_delta : function
        Reactive power at start of line as function of nodal voltage amplitudes and angles.
    P_end_of_V_delta : function
        Active power at end of line as function of nodal voltage amplitudes and angles.
    Q_end_of_V_delta : function
        Reactive power at end of line as function of nodal voltage amplitudes and angles.
    """
    
    def P_start_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, **kwargs):
        """
        Active power at start of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        """
        return g*V_start**2 - V_start*V_end*(g*cos(delta_start-delta_end) + b*sin(delta_start-delta_end))


    def Q_start_of_V_delta(V_start, V_end,delta_start, delta_end, *args, g=None, b=None, **kwargs):
        """
        Reactive power at start of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        """        
        return -b*V_start**2 - V_start*V_end*(g*sin(delta_start-delta_end) - b*cos(delta_start-delta_end))
    
    
    def P_end_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, **kwargs):
        """
        Active power at end of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        """        
        return g*V_end**2 - V_start*V_end*(g*cos(delta_start-delta_end) - b*sin(delta_start-delta_end))
    
    
    def Q_end_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, **kwargs):
        """
        Reactive power at end of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        """        
        return -b*V_end**2 - V_start*V_end*(-g*sin(delta_start-delta_end) - b*cos(delta_start-delta_end))
    
    return P_start_of_V_delta, Q_start_of_V_delta, P_end_of_V_delta, Q_end_of_V_delta
    
# %% pi line

def pi_line(*args, **kwargs):
    """
    Creates the link equations for a pi-line model.
        
    Returns
    --------
    P_start_of_V_delta : function
        Active power at start of line as function of nodal voltage amplitudes and angles.
    Q_start_of_V_delta : function
        Reactive power at start of line as function of nodal voltage amplitudes and angles.
    P_end_of_V_delta : function
        Active power at end of line as function of nodal voltage amplitudes and angles.
    Q_end_of_V_delta : function
        Reactive power at end of line as function of nodal voltage amplitudes and angles.
    """
    
    def P_start_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, **kwargs):
        """
        Active power at start of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        """        
        return (g + 0.5*g_sh)*V_start**2 - V_start*V_end*(g*cos(delta_start-delta_end) + b*sin(delta_start-delta_end))


    def Q_start_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, **kwargs):
        """
        Reactive power at start of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        """      
        return -(b + 0.5*b_sh)*V_start**2 - V_start*V_end*(g*sin(delta_start-delta_end) - b*cos(delta_start-delta_end))
    
    
    def P_end_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, **kwargs):
        """
        Active power at end of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        """
        return (g + 0.5*g_sh)*V_end**2 - V_start*V_end*(g*cos(delta_start-delta_end) - b*sin(delta_start-delta_end))
    
    
    def Q_end_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, **kwargs):
        """
        Reactive power at end of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        """
        return -(b + 0.5*b_sh)*V_end**2 - V_start*V_end*(-g*sin(delta_start-delta_end) - b*cos(delta_start-delta_end))
    
    return P_start_of_V_delta, Q_start_of_V_delta, P_end_of_V_delta, Q_end_of_V_delta

# %% pi-line transformer

def pi_line_trafo(*args, **kwargs):
    """
    Creates the link equations for a pi-line model with a transformer at the start end of the link.
            
    Returns
    --------
    P_start_of_V_delta : function
        Active power at start of line as function of nodal voltage amplitudes and angles.
    Q_start_of_V_delta : function
        Reactive power at start of line as function of nodal voltage amplitudes and angles.
    P_end_of_V_delta : function
        Active power at end of line as function of nodal voltage amplitudes and angles.
    Q_end_of_V_delta : function
        Reactive power at end of line as function of nodal voltage amplitudes and angles.
    """
    
    def P_start_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, n=None, **kwargs):
        """
        Active power at start of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        n : complex float
            Transformer ratio.
        """
        return 1/abs(n)**2*(g + 0.5*g_sh)*V_start**2 - 1/abs(n)*V_start*V_end*(g*cos(delta_start-delta_end) + b*sin(delta_start-delta_end))


    def Q_start_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, n=None, **kwargs):
        """
        Reactive power at start of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        n : complex float
            Transformer ratio.
        """
        return -1/abs(n)**2*(b + 0.5*b_sh)*V_start**2 - 1/abs(n)*V_start*V_end*(g*sin(delta_start-delta_end) - b*cos(delta_start-delta_end))

    
    def P_end_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, n=None, **kwargs):
        """
        Active power at end of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        n : complex float
            Transformer ratio.
        """
        return (g + 0.5*g_sh)*V_end**2 - 1/abs(n)*V_start*V_end*(g*cos(delta_start-delta_end) - b*sin(delta_start-delta_end))

    
    def Q_end_of_V_delta(V_start, V_end, delta_start, delta_end, *args, g=None, b=None, g_sh=None, b_sh=None, n=None, **kwargs):
        """
        Reactive power at end of link as function of start and end voltage amplitudes and angles.
        
        Parameters
        ----------
        V_start : float
            Start voltage amplitude.
        V_end : float
            End voltage amplitude.
        delta_start : float
            Start voltage angle.
        delta_end : float
            End voltage angle.
        g : float
            Short circuit conductance.
        b : float
            Short circuit susceptance.
        g_sh : float
            Magnetising conductance.
        b_sh : float
            Magnetising susceptance.
        n : complex float
            Transformer ratio.
        """
        return -(b + 0.5*b_sh)*V_end**2 - 1/abs(n)*V_start*V_end*(-g*sin(delta_start-delta_end) - b*cos(delta_start-delta_end))
    
    return P_start_of_V_delta, Q_start_of_V_delta, P_end_of_V_delta, Q_end_of_V_delta