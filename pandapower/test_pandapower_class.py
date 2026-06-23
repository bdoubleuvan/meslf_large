import numpy as np
import os
import re
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'code'))

from meslf.networks.pandapower_network import *

network_names = [
                 'case4gs',
                 'case5',
                 'case6ww',
                 'case9',
                 'case14',
                 'case24_ieee_rts',
                 'GBreducednetwork',
                 'case30',
                 'case_ieee30',
                 'case33bw',
                 'case39',
                 'case57',
                 'case89pegase',
                 'case118',
                 'case145',
                 'iceland',
                 'case_illinois200',
                 'case300',
                 'case1354pegase',
                 'case1888rte',
                 'GBnetwork',
                 'case2848rte',
                 'case2869pegase',
                 'case3120sp',
                 'case6470rte',
                 'case6495rte',
                 'case6515rte',
                 'case9241pegase'
                 ]
 
for network_name in network_names[-2:-1]:    
    formulation = 'complex_power'
    
    scale_var = 'per_unit'
    
    solver = 'nr'
    solver_parameters = {'m' : 3, # Anderson acceleration
                         'max_iterations' : 20,
                         'optimal_multiplier' : False,
                         'residual_q' : False,
                         'tol' : 1e-6}

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
                             'petsc_nzdiag' : 1e-6,
                             'petsc_ord_type' : 'qmd', # 'natural' # 'nd' # 'qmd' # 'rcm' # 'rowlength' # 'spectral' # 'wbm' # '1wd'
                             'petsc_preconditioner' : 'ilu', # 'gamg' # 'ilu' # 'jacobi' # 'kaczmarz' # 'lu' # 'sor'
                             'petsc_reorderfornonzerodiagonal' : False,
                             'petsc_reuse' : False,
                             'petsc_shift_amount' : None, # use None to turn off
                             'petsc_shift_type' : 'inblocks', # 'positive_definite' # None # 'nonzero'
                             'petsc_zero_diagonal' : False # define the zeros on diagonal explicitly
                            }

    pandapower_network = PandapowerNetwork(network_name=network_name)
    network, data = pandapower_network.create_network(ignore_nodes=[],
                                                      formulation=formulation,
                                                      scale_var=scale_var,
                                                      change_first_slack=False)
    
    network.initialize()

    delta_init = np.zeros(len(network.unknown_delta_nodes)) # flat start 0
    V_init = np.ones(len(network.unknown_V_nodes)) # flat start 1
    x_init = np.concatenate([delta_init, V_init])
    
    x_sol, iterations, errors, delta_sol, V_sol, S_inj, P_link, Q_link = network.solve_network(x_init=x_init,
                                                                                               solver=solver,
                                                                                               solver_parameters=solver_parameters,
                                                                                               lin_solver=lin_solver,
                                                                                               lin_solver_parameters=lin_solver_parameters,
                                                                                               post_processing=True)

    print(50*"-" + "\n" + network_name + "\n" + 50*"-")
    
    if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
        print("Average F time in seconds = {:.4e}".format(np.average(network.solver.F_times)))
        print("Average J time in seconds = {:.4e}".format(np.average(network.solver.J_times)))
        print("Average linear solve time in seconds = {:.4e}".format(np.average(network.solver.linear_solve_times)))
    print("Average non-linear solve time in seconds = {:.4e}".format(np.average(network.solver.nonlinear_solve_times)))
    print("Total time in seconds = {:.4e}".format(network.solver.total_time))
    
    print("Iterations = {:d}".format(iterations))
    print("Final error = {:.3e}".format(errors[-1]))