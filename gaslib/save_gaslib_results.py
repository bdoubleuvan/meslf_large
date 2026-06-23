import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'code'))

import copy
import numpy as np
import re

from meslf.networks.gaslib_network import GasLibNetwork

network_names = ['GasLib-11', 'GasLib-24', 'GasLib-40', 'GasLib-135', 'GasLib-582', 'GasLib-2607', 'GasLib-4197']

# network options
flow = 'average' # 'min' # 'max'
pressure = 'max' # 'min' # 'average'
gas_type = 'hydrogen' # 'natural'

# pipe settings
link_settings = {'friction' : 'friction_weymouth',
                 'link_type' : 'pipe_high',
                 'link_equation_formulation' : 'dp_of_q'}

# initial guess
initial_guess = 'standard'
# initial_guess = 'linear_dp'
# initial_guess = 'linear_dp_satisfy_conservation_of_mass'
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
lin_solver = 'lu'
lin_solver_parameters = {'diag_pivot_thresh' : 0.1,
                         'drop_tol' : 1e-4,
                         'drop_rule' : ['basic', 'area'],
                         'fill_factor': 5,
                         'idr_s' : 4,
                         'max_iterations': 100,
                         'reorderfornonzerodiagonal' : False, # also affects ordering for petsc
                         'options' : {'Equil' : True},
                         'permc_spec': 'colamd',
                         'preconditioner': 'two-level',
                         'preconditioners_for_blocks': [],
                         'preconditioners_for_two_level': [],
                         'rcm' : False,
                         'residuals_filename' : None,
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

iterations_per_network = np.zeros(len(network_names), 'object, float')
slack_value_per_network = np.zeros(len(network_names), 'object, float')

for i, network_name in enumerate(network_names):
    print(50*"-" + "\n" + network_name + "\n" + 50*"-")
    
    if 'linear' in initial_guess:
        link_settings_linear = copy.deepcopy(link_settings)
        link_settings_linear['friction'] = 'friction_pole'
        link_settings_linear['link_type'] = 'pipe_low'
        
        solver_parameters_linear = copy.deepcopy(solver_parameters)
        
        if initial_guess == 'linear_dp_satisfy_conservation_of_mass':
            solver_parameters_linear['residual_q'] = True
    elif 'simplify_resistor' in initial_guess:
        link_settings_linear = copy.deepcopy(link_settings)
        
        solver_parameters_linear = copy.deepcopy(solver_parameters)
        
        if initial_guess == 'simplify_resistor_satisfy_conservation_of_mass':
                solver_parameters_linear['residual_q'] = True
    
    final_error = []

    gaslib_network = GasLibNetwork(network_name=network_name)
    network, node_data, link_data = gaslib_network.create_network(gas_type=gas_type,
                                                                  flow=flow,
                                                                  pressure=pressure,
                                                                  link_settings=link_settings,
                                                                  resistor=resistor,
                                                                  scale_var=scale_var)
    network.initialize()
    
    # network topology
    # print(50 * "-")
    # print(node_data.bc_type.value_counts(), end="\n" + 50 * "-" + "\n")
    # print(link_data.link_type.value_counts(), end="\n" + 50 * "-" + "\n")
    
    # start solving
    lin_solver_parameters['block_size'] = (len(network.links) + len(network.nodes)) // 10
    
    # Computing per unit scaling parameters
    q_init = 0.1 * np.ones(len(network.links))
    if scale_var is None:
        qbase = gaslib_network.convert_to_kg_per_second(value=node_data['q_max_value'].max(), \
                                                        rho=node_data['normDensity_value'].max(), \
                                                        unit=node_data['q_max_unit'][node_data['q_max_value'].argmax()])
        q_init *= qbase

    # initial pressure deviates from 5% to 10% of the reference pressure

    p_init = np.linspace(0.95, 0.9, network.number_of_unknown_p)
    if scale_var is None:
        pbase = gaslib_network.convert_to_pa(value=node_data['pressureMax_value'].max(), \
                                             unit=node_data['pressureMax_unit'][node_data['pressureMax_value'].argmax()])
        p_init *= pbase
    
    # initial guess
    x_init = np.concatenate([q_init, p_init])
    
    # if network_name == 'GasLib-4197':
    #     x_init = np.loadtxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results", "solution", "{}.txt".format(network_name)))
    
    if initial_guess not in ['standard']:
        if 'linear' in initial_guess:
            network_altered, node_data_altered, link_data_altered = gaslib_network.create_network(flow=flow,
                                                                                                  pressure=pressure,
                                                                                                  gas_type=gas_type, 
                                                                                                  link_settings=link_settings_linear,
                                                                                                  resistor=resistor,
                                                                                                  scale_var=scale_var)
        else:
            network_altered, node_data_altered, link_data_altered = gaslib_network.create_network(flow=flow,
                                                                                                  pressure=pressure,
                                                                                                  gas_type=gas_type, 
                                                                                                  link_settings=link_settings_linear,
                                                                                                  resistor=False,
                                                                                                  scale_var=scale_var)
        network_altered.initialize()
        
        # solve linear
        output = network_altered.solve_network(x_init=x_init,
                                               solver=solver,
                                               solver_parameters=solver_parameters_linear,
                                               lin_solver=lin_solver,
                                               lin_solver_parameters=lin_solver_parameters,
                                               post_processing=False)
        
        if initial_guess in ['linear_dp', 'linear_dp_satisfy_conservation_of_mass']:
            x_init[:len(q_init)] = output[0][:len(q_init)]
        else:
            x_init = output[0]
                        
    # solve original
    output = network.solve_network(x_init=x_init,
                                   solver=solver,
                                   solver_parameters=solver_parameters,
                                   lin_solver=lin_solver,
                                   lin_solver_parameters=lin_solver_parameters,
                                   post_processing=True)
        
    final_error.append(network.solver.errors[-1])
    
    np.savetxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results", "residuals", "{}.txt".format(network_name)), output[2])
    np.savetxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results", "solution", "{}.txt".format(network_name)), output[0])
    iterations_per_network[i][0] = network_name
    slack_value_per_network[i][0] = network_name
    iterations_per_network[i][1] = output[1]
    slack_value_per_network[i][1] = output[-1][0]
    
    # print some convergence results
    if initial_guess == 'standard':
        print("Number of iterations = {}".format(network.solver.iterations))
    else:
        print("Number of iterations = {} + {}".format(network_altered.solver.iterations, network.solver.iterations))
    print("Final error = {:.4e}".format(final_error[-1]))
    if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
        print("Average F time in seconds = {:.4e}".format(np.average(network.solver.F_times)))
        print("Average J time in seconds = {:.4e}".format(np.average(network.solver.J_times)))
        print("Average linear solve time in seconds = {:.4e}".format(np.average(network.solver.linear_solve_times)))
    print("Average non-linear solve time in seconds = {:.4e}".format(np.average(network.solver.nonlinear_solve_times)))
    print("Total time in seconds = {:.4e}".format(network.solver.total_time))
    
    print()
    print("{:21s}{:14.3f} Pa".format("Min. pressure = ", np.min(output[-3])))
    print("{:21s}{:14.3f} Pa".format("Max. pressure = ", np.max(output[-3])))
    print("{:21s}{:14.3f} Pa".format("Reference pressure = ", output[-3][0]))
    
    print()
    print("Slack mass flow = {:17.3f} kg / s".format(output[-1][0]))
    print("Slack mass flow = {:17.3f} 1000m^3 / hour".format(3.6 * output[-1][0] / node_data.at[0, 'normDensity_value']))
    print("Sum injected mass flow = {:10.3e} kg / s".format(np.sum(output[-1])))
    
np.savetxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results",  "iterations.txt"), iterations_per_network, fmt=['%s', '%d'])
np.savetxt(os.path.join(os.path.abspath('.'), "code", "gaslib", "results", "slack_value.txt"), slack_value_per_network, fmt=['%s', '%.18e'])