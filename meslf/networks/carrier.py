"""
Carrier base class
"""

# %% Abstract class for Carrier

class Carrier():
    """
    Carrier class
    """

    def __init__(self, name):
        """Creates a Carrier object

        Parameters
        ----------
        name : string
            name of the carrier
        """
        self.name = name

# %% Gas

class Gas(Carrier):
    """
    Gas Carrier class
    """

    def __init__(self, name, R_gas, Z, pn, Tn, T=None, mu=None):
        """
        Creates a Gas object

        Parameters
        ----------
        name : string
            name of the carrier
        R_gas : float
            Gas constant in Nm/kgK (=J/kgK)
        pn : float
            standard pressure in N/m^2 (=Pa)
        T : float
            temperature of the gas in K
        Tn : float
            standard temperature in K
        Z : float
            compressibility factor of the gas
        mu : float, optional
            dynamic viscosity of gas in m^2/s. Default is None
        """
        super().__init__(name)
        self.R_gas = R_gas
        self.T = T
        self.Z = Z
        self.mu = mu
        
        self.pn = pn
        self.Tn = Tn
        
        if T is None:
            self.T = self.Tn
        
        self.rhon = self.pn / (self.R_gas*self.Tn)

# %% Water

class Water(Carrier):
    """
    Water Carrier class
    """

    def __init__(self, name, Cp, rho=None, mu=None, g=9.81):
        """
        Creates a Water object

        Parameters
        ----------
        name : string
            name of the carrier
        Cp : float
            specific heat of the carrier in J/(kgK)
        rho : float, optional
            Density of carrier in kg/m^3. Default is None
        mu : float, optional
            Viscosity of carrier in m^2/s. Default is None
        g : float, optional
            Gravitational constant in m/s^2. Default is 9.81
        """
        super().__init__(name)
        self.Cp = Cp
        self.rhon = rho
        self.mu = mu
        self.g = g

    @property
    def Cp(self):
        """
        getter of _Cp
        """
        return self._Cp

    @Cp.setter
    def Cp(self, Cp):
        """
        setter of _Cp
        """
        self._Cp = Cp

    def get_Cp(self, scale_var=None, scale_var_params=None):
        """
        Get specific heat of carrier, optionally with scaling.

        Parameters
        ----------
        scale_var : string, optional
            How to scale the variable. Default is no scaling
        scale_var_params : dict, optional
            Dictionary with values needed for scaling variables. Default is None

        Returns
        -------
        Cp : float
            Specific heat of the carrier, possibly scaled. When unscaled in J/(kgK).
        """
        Cp = self.Cp
        if scale_var == 'per_unit':
            Cb = scale_var_params['phibase'] / \
                (scale_var_params['qbase']*scale_var_params['Tbase'])
            Cp = Cp/Cb
        return Cp

    @property
    def rhon(self):
        """
        getter of _rhon
        """
        return self._rhon

    @rhon.setter
    def rhon(self, rhon):
        """
        setter of _rho
        """
        self._rhon = rhon

    @property
    def mu(self):
        """
        getter of _mu
        """
        return self._mu

    @mu.setter
    def mu(self, mu):
        """
        setter of _mu
        """
        self._mu = mu

    @property
    def g(self):
        """
        getter of _g
        """
        return self._g

    @g.setter
    def g(self, g):
        """
        setter of _g
        """
        self._g = g
