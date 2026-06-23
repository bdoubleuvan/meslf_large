import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)).rsplit('/', 2)[0],'code'))

import matplotlib.pyplot as plt
import numpy as np

from meslf.networks.gas_network import GasNetwork, GasNode, GasLink, GasHalfLink
from meslf.networks.carrier import Gas

from meslf.networks.electrical_network import ElectricalNetwork, ElectricalNode, ElectricalLink, ElectricalHalfLink

from meslf.networks.heterogeneous_network import HeterogeneousNetwork, HeterogeneousNode
from meslf.utils.constants import bar, MW

# %% gas

def create_gas(gas_type='hydrogen', data=None, M=28.9652e-3, R=8.31446261815324, Z=1):
    # Set-up gas properties
    R_air = R / M # [J/kgK] specific gas constant for air
    
    pn = 101325 # [Pa] standard condition
    Tn = 273.15 # [K] standard condition
    
    if gas_type in ['natural']:
        mu = 1.02 * 10**-5 # based on methane
        S = 0.7611058 / 1.2922 # specific gravity of natural gas
    elif gas_type in ['hydrogen']:
        mu = 8.4 * 10**-5
        S = 0.08988 / 1.2922 # specific gravity of hydrogen gas
        
    R_gas = R_air / S
    
    if gas_type in ['natural']: # set temperature of gas equal to first node in data
        if data['gasTemperature_unit'] in ['C', 'Celsius']:
            T_gas = 273.15 + data['gasTemperature_value']
        elif data['gasTemperature_unit'] in ['K', 'Kelvin']:
            T_gas = data['gasTemperature_value']
        else:
            # T_gas = Tn
            raise ValueError("Invalid temperature unit " + \
                             "'{}', which is not implemented or wrong name. ".format(data['gasTemperature_unit']) + \
                             "Use 'C', 'Celsius', 'K' or 'Kelvin'.")
    else: # set temperature equal to normal temperature
        T_gas = Tn
    
    return Gas('gas', R_gas=R_gas, T=T_gas, Z=Z, pn=pn, Tn=Tn, mu=mu)

# %%

def create_network(p2g=True, eta=1, GHV=1.418*10**8):
    scale_var = 'per_unit'
    
    qbase = 1
    pbase = 70*bar
    
    Sbase = 100*MW
    Vbase = 230*10**3
    
    scale_var_params_g = {'qbase' : qbase,
                          'pbase' : pbase}
    
    scale_var_params_e = {'Sbase' : Sbase,
                          'Vbase' : Vbase,
                          'deltabase' : 1}
    
    scale_var_params_c = {'Ebase' : Sbase,
                          'GHVbase' : Sbase / qbase}
    
    unit_params = {'eta': eta,
                   'GHV': GHV}

    if p2g:
        unit_type = 'p2g'
        
        c_network = HeterogeneousNetwork('Test network for 1 coupling unit')
        c0 = HeterogeneousNode('c0', bc_type=[], unit_type=unit_type, unit_params=unit_params,
                            scale_var=scale_var, scale_var_params=scale_var_params_c)
        c_network.add_node(c0)   
        
        
        g_network = GasNetwork('Gas', formulation='full')
        g0 = GasNode(name='g0', bc_type=['p', 'q'], p=10*bar,
                     scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_node(g0)
        g0_hl = GasHalfLink(name='g0_load', start_node=g0, bc_type=['q'], q=0)
        g_network.add_half_link(g0_hl)
        c0g0 = GasLink(name='c0g0', start_node=c0, end_node=g0, link_type='dummy', 
                       scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_link(c0g0)
        
        g1 = GasNode(name='g1', bc_type=['q'],
                     scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_node(g1)
        g1_hl = GasHalfLink(name='g1_load', start_node=g1, q=1)
        g_network.add_half_link(g1_hl)
        g0g1 = GasLink(name='g0g1', start_node=g0, end_node=g1, link_type='pipe_high',
                       link_params={'D' : 1, 'L' : 1000, 'carrier' : create_gas(), 'friction' :'friction_weymouth', 'E' : 1},
                       scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_link(g0g1)
        
        
        e_network = ElectricalNetwork('Electricity', formulation='complex_power')
        e0 = ElectricalNode(name='e0', bc_type=['V', 'delta'], V=1*Vbase, delta=0,
                            scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_node(e0)
        e0_hl = ElectricalHalfLink(name='e0_slack', start_node=e0)
        e_network.add_half_link(e0_hl)
        e0c0 = ElectricalLink(name='e0c0', start_node=e0, end_node=c0, bc_type=['Q_start'], Q_start=0, link_type='dummy', 
                              scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_link(e0c0)
        
        e1 = ElectricalNode(name='e1', bc_type=['P', 'Q'],
                            scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_node(e1)
        e1_hl = ElectricalHalfLink(name='e1_load', start_node=e1, P=186591550.797925, Q=-62135427.245244026)
        e_network.add_half_link(e1_hl)
        e1e0 = ElectricalLink(name='e1e0', start_node=e1, end_node=e0, link_type='pi_line', link_params={'b' : -0.036065, 'g' : 0.007213, 'g_sh' : 0, 'b_sh' : 0.000194},
                              scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_link(e1e0)        


        c_network.add_network(g_network)
        c_network.add_network(e_network)
    else:   
        unit_type = 'gas_fired_generator'
             
        c_network = HeterogeneousNetwork('Test network for 1 coupling unit')
        
        c0 = HeterogeneousNode('c0', bc_type=[], unit_type=unit_type, unit_params=unit_params,
                               scale_var=scale_var, scale_var_params=scale_var_params_c)
        c_network.add_node(c0)   
        

        g_network = GasNetwork('Gas', formulation='full')
        
        g0 = GasNode(name='g0', bc_type=['p', 'q'], p=pbase,
                     scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_node(g0)
        g0_hl = GasHalfLink(name='g0_load', start_node=g0, q=0)
        g_network.add_half_link(g0_hl)
        g0c0 = GasLink(name='g0c0', start_node=g0, end_node=c0, link_type='dummy', 
                       scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_link(g0c0)
        
        g1 = GasNode(name='g1', bc_type=['q'],
                     scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_node(g1)
        g1_hl = GasHalfLink(name='g1_load', start_node=g1, q=-1)
        g_network.add_half_link(g1_hl)
        g1g0 = GasLink(name='g1g0', start_node=g1, end_node=g0, link_type='pipe_high',
                       link_params={'D' : 1, 'L' : 1000, 'carrier' : create_gas(), 'friction' :'friction_weymouth', 'E' : 1},
                       scale_var=scale_var, scale_var_params=scale_var_params_g)
        g_network.add_link(g1g0)
        
                
        e_network = ElectricalNetwork('Electricity', formulation='complex_power')
        
        e0 = ElectricalNode(name='e0', bc_type=['V', 'delta'], V=1*Vbase, delta=0,
                            scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_node(e0)
        e0_hl = ElectricalHalfLink(name='e0_slack', start_node=e0, scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_half_link(e0_hl)
        c0e0 = ElectricalLink(name='c0e0', start_node=c0, end_node=e0, bc_type=['Q_start'], Q_start=0, link_type='dummy', 
                              scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_link(c0e0)
        
        e1 = ElectricalNode(name='e1', bc_type=['P', 'Q'],
                            scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_node(e1)
        e1_hl = ElectricalHalfLink(name='e1_load', start_node=e1, P=190451709.06390667, Q=-23231420.18533802)
        e_network.add_half_link(e1_hl)
        e0e1 = ElectricalLink(name='e0e1', start_node=e0, end_node=e1, link_type='pi_line', link_params={'b' : -0.036065, 'g' : 0.007213, 'g_sh' : 0, 'b_sh' : 0.000194},
                              scale_var=scale_var, scale_var_params=scale_var_params_e)
        e_network.add_link(e0e1)


        c_network.add_network(g_network)
        c_network.add_network(e_network)
        
    return g_network, e_network, c_network

# %%

if __name__ == '__main__':
    p2g = False
    eta = 1
    GHV = 1.418*10**8
    
    g_network, e_network, c_network  = create_network(p2g=p2g, eta=eta, GHV=GHV)
    
    c_network.initialize()
    
    x_init = np.zeros(len(c_network.x_entries))
    

    
    if p2g:
        x_init[0] = 0 # q
        x_init[1] = 0.99 # p
        x_init[2] = 0 # delta
        x_init[3] = 1 # V
        x_init[4] = 0 # q
        x_init[5] = 0 # P
    else:
        x_init[0] = 1 # q
        x_init[1] = 0.99 # p
        x_init[2] = 0 # delta
        x_init[3] = 1 # V
        x_init[4] = 0 # q
        x_init[5] = 0 # P
        
    # non-linear solver settings
    solver = 'nr'
    solver_parameters = {'m' : 10, # Anderson acceleration
                         'max_iterations' : 20,
                         'optimal_multiplier' : False,
                         'residual_q' : False,
                         'tol' : 1e-6}
    
    # linear solver settings
    lin_solver = 'lu'
    lin_solver_parameters = {'diag_pivot_thresh' : 0.1,
                             'drop_tol' : 1e-4,
                             'drop_rule' : ['basic', 'area'],
                             'fill_factor': 1,
                             'max_iterations': 100,
                             'reorderfornonzerodiagonal' : False, # also affects ordering for petsc
                             'options' : {'Equil' : True},
                             'permc_spec': 'colamd',
                             'preconditioner': 'ilu',
                             'preconditioners_for_blocks': [],
                             'preconditioners_for_two_level': [],
                             'rcm' : False,
                             'shift_value': 0.1,
                             'tol' : 1e-6,
                             'gmres_restart' : 100,
                             'petsc_fill-in' : 0,
                             'petsc_gamglevels': None, # None is default
                             'petsc_gamgsmooths' : None, # None is default
                             'petsc_gamgtype' : 'agg', # 'agg' # 'classical'
                             'petsc_gmres_restart' : 100,
                             'petsc_lin_solver' : 'gmres',
                             'petsc_max_iterations': 100,
                             'petsc_nzdiag' : 0,
                             'petsc_ord_type' : 'qmd', # 'natural' # 'nd' # 'qmd' # 'rcm' # 'rowlength' # 'spectral' # 'wbm' # '1wd'
                             'petsc_preconditioner' : 'kaczmarz', # 'gamg' # 'ilu' # 'jacobi' # 'kaczmarz' # 'lu' # 'sor'
                             'petsc_reorderfornonzerodiagonal' : False,
                             'petsc_reuse' : False,
                             'petsc_shift_amount' : None, # use None to turn off
                             'petsc_shift_type' : 'inblocks', # 'positive_definite' # None # 'nonzero'
                             'petsc_zero_diagonal' : False # define the zeros on diagonal explicitly
                             }
    
    output = c_network.solve_network(x_init=x_init,
                                     solver=solver,
                                     solver_parameters=solver_parameters,
                                     lin_solver=lin_solver,
                                     lin_solver_parameters=lin_solver_parameters,
                                     post_processing=True)
    
    print("Solution = ", output[0])
    print("Iterations = ", output[1])
    print("Residual = ", output[2])
    print("p = ", output[3])
    print("q = ", output[4])
    print("delta = ", output[6])
    print("V = ", output[7])
    print("S = ", output[8][0])
    print("q_c = ", output[19])
    print("P_c = ", output[20])