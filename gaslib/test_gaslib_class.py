import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'code'))

from meslf.networks.gaslib_network import GasLibNetwork

# network_names = ['GasLib-11', 'GasLib-24', 'GasLib-40', 'GasLib-135', 'GasLib-582', 'GasLib-2607', 'GasLib-4197']
network_names = ['GasLib-11', 'GasLib-24', 'GasLib-40', 'GasLib-135', 'GasLib-582', 'GasLib-4197']
network_names = network_names[:]

# gas type
gas_type = 'hydrogen'

# pipe settings
link_settings = {'friction' : 'friction_weymouth',
                 'link_type' : 'pipe_high',
                 'link_equation_formulation' : 'dp_of_q'}

# initial guess
# initial_guess = 'standard'
# initial_guess = 'linear_dp'
initial_guess = 'linear_dp_satisfy_conservation_of_mass'
# initial_guess = 'simplify_resistor'
# initial_guess = 'simplify_resistor_satisfy_conservation_of_mass'

# Use same resistor parameters as seen in data
resistor = False # use the resistor parameters from data

# scaling type
scale_var = 'per_unit'

# non-linear solver settings
solver = 'nr'
solver_parameters = {'m' : 10, # Anderson acceleration
                     'max_iterations' : 20,
                     'optimal_multiplier' : False,
                     'residual_q' : False,
                     'tol' : 1e-6}

# linear solver settings
lin_solver = 'gmres'
lin_solver_parameters = {'diag_pivot_thresh' : 0.1,
                         'drop_tol' : 1e-4,
                         'drop_rule' : ['basic', 'area'],
                         'fill_factor': 5,
                         'idr_s' : 4,
                         'max_iterations': 100,
                         'reorderfornonzerodiagonal' : True, # also affects ordering for petsc
                         'options' : {'Equil' : True},
                         'permc_spec': 'colamd',
                         'preconditioner': 'two-level',
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

for network_name in network_names:
    gaslib_network = GasLibNetwork(network_name=network_name)
    gaslib_network.solve(gas_type=gas_type,
                         link_settings=link_settings,
                         initial_guess=initial_guess,
                         resistor=resistor,
                         solver=solver,
                         solver_parameters=solver_parameters,
                         lin_solver=lin_solver,
                         lin_solver_parameters=lin_solver_parameters,
                         scale_var=scale_var)