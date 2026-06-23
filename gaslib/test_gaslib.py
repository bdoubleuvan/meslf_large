import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'code'))

import copy
import numpy as np
import re

from meslf.networks.gaslib_network import GasLibNetwork
from meslf.load_flow.system_of_equations import NonLinearSystem, NonLinearSystemGas, NonLinearSystemElectrical, NonLinearSystemHeterogeneous

# %% Settings

# network_names = ['GasLib-11', 'GasLib-24', 'GasLib-40', 'GasLib-135', 'GasLib-582', 'GasLib-2607', 'GasLib-4197']
network_names = ['GasLib-11', 'GasLib-24', 'GasLib-40', 'GasLib-135', 'GasLib-582', 'GasLib-4197']
network_names = network_names[-1:]

slack_positions = [11] # [11, 17, 18, 19, 20] # position of slack node
number_of_clones_list = [1, 2, 4, 8, 16, 32]
number_of_merges = 16
directory = os.path.join(os.path.abspath('.'), 
                         "code", 
                         "gaslib", 
                         "results_merges_junction_{}".format(number_of_merges))

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
                     'max_iterations' : 30,
                     'optimal_multiplier' : False,
                     'residual_q' : False,
                     'tol' : 1e-6}

# linear solver settings
lin_solver = 'lu'
lin_solver_parameters = {'diag_pivot_thresh' : 1,
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


# %% Run simulations

save_number_of_clones = []
dofs = []
final_error = []
iteration = []
slack_position_list = []
slack_value = []

F_time = []
J_time = []
linear_solve_time = []
nonlinear_solve_time = []
total_time = []

for slack_position in slack_positions:
    directory = os.path.join(directory, "slack_position_{}".format(slack_position))
    for number_of_clones in number_of_clones_list:
        for network_name in network_names:
            print(50*"-" + "\n" + network_name + "\n" + 50*"-")
            
            os.makedirs(name=os.path.join(directory, "clone_{}".format(number_of_clones), "solutions"), exist_ok=True)
            os.makedirs(name=os.path.join(directory, "clone_{}".format(number_of_clones), "residuals"), exist_ok=True)
            
            # initialise network
            gaslib_network = GasLibNetwork(network_name=network_name)
            network, node_data, link_data, \
            save_node, save_merge_q_node_even, save_merge_q_node_odd = gaslib_network.create_network(gas_type=gas_type,
                                                                                                     flow=flow,
                                                                                                     pressure=pressure,
                                                                                                     link_settings=link_settings,
                                                                                                     resistor=resistor,
                                                                                                     scale_var=scale_var,
                                                                                                     slack_position=slack_position,
                                                                                                     number_of_clones=number_of_clones,
                                                                                                     number_of_merges=number_of_merges)
            network.initialize()

            # network topology
            # print(50 * "-")
            # print(node_data.bc_type.value_counts(), end="\n" + 50 * "-" + "\n")
            # print(link_data.link_type.value_counts(), end="\n" + 50 * "-" + "\n")

            # start solving
            lin_solver_parameters['block_size'] = (len(network.links) + len(network.nodes)) // 10

            # Computing per unit scaling parameters
            q_init = 0.1 * np.ones(len(network.link_unknown_q) + len(network.dummy_link_unknown_q))
            if scale_var is None:
                qbase = gaslib_network.convert_to_kg_per_second(value=node_data['q_max_value'].max(), \
                                                                rho=node_data['normDensity_value'].max(), \
                                                                unit=node_data['q_max_unit'][node_data['q_max_value'].argmax()])
                q_init *= qbase

            # initial pressure deviates from 5% to 10% of the reference pressure
            p_original = np.linspace(0.95, 0.9, len(save_node.keys()))
            p_init_even = p_original[~np.isin(range(len(p_original)), list(save_merge_q_node_odd.values()))]
            p_init_odd = p_original[~np.isin(range(len(p_original)), list(save_merge_q_node_even.values()))]
            p_init = np.linspace(0.95, 0.9, len(save_node.keys()))
            for i in range(1, number_of_clones):
                if (i % 2) == 0:
                    p_init = np.concatenate([p_init, p_init_even])
                else:
                    p_init = np.concatenate([p_init, p_init_odd])
                    
            print(len(p_init), network.number_of_unknown_p)

            if scale_var is None:
                pbase = gaslib_network.convert_to_pa(value=node_data['pressureMax_value'].max(), \
                                                     unit=node_data['pressureMax_unit'][node_data['pressureMax_value'].argmax()])
                p_init *= pbase

            # initial guess
            x_init = np.concatenate([q_init, p_init])
            print("DoFs = {}".format(x_init.shape[0]))

            if initial_guess not in ['standard']:
                if 'linear' in initial_guess:
                    network_altered, node_data_altered, link_data_altered, \
                    _, _, _  = gaslib_network.create_network(flow=flow,
                                                             pressure=pressure,
                                                             gas_type=gas_type, 
                                                             link_settings=link_settings_linear,
                                                             resistor=resistor,
                                                             scale_var=scale_var,
                                                             slack_position=slack_position,
                                                             number_of_clones=number_of_clones,
                                                             number_of_merges=number_of_merges)
                else:
                    network_altered, node_data_altered, link_data_altered, \
                    _, _, _ = gaslib_network.create_network(flow=flow,
                                                            pressure=pressure,
                                                            gas_type=gas_type, 
                                                            link_settings=link_settings_linear,
                                                            resistor=False,
                                                            scale_var=scale_var,
                                                            slack_position=slack_position,
                                                            number_of_clones=number_of_clones,
                                                            number_of_merges=number_of_merges)
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
                                           post_processing=False)

            # save output            
            np.savetxt(os.path.join(directory, "clone_{}".format(number_of_clones), 'solutions', '{}.txt'.format(network_name)), output[0])
            np.savetxt(os.path.join(directory, "clone_{}".format(number_of_clones), 'residuals', '{}.txt'.format(network_name)), output[2])

            # collect output
            save_number_of_clones.append(number_of_clones)
            dofs.append(len(network.x_entries))
            final_error.append(network.solver.errors[-1])
            iteration.append(network.solver.iterations)
            slack_position_list.append(slack_position)

            F_time.append(np.average(network.solver.F_times))
            J_time.append(np.average(network.solver.J_times))
            linear_solve_time.append(np.average(network.solver.linear_solve_times))
            nonlinear_solve_time.append(np.average(network.solver.nonlinear_solve_times))
            total_time.append(network.solver.total_time)

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
            for node in network.nodes:
                if 'q' not in node.bc_type:
                    slack_q = node.half_links[0].q
                    break
            print("Slack mass flow = {:11.9f} kg / s".format(slack_q))
            print("Slack mass flow = {:11.9f} 1000m^3 / hour".format(3.6 * slack_q / node_data.at[slack_position, 'normDensity_value']))
            print("Sum injected mass flow = {:10.3e} kg / s".format(np.sum(output[-1])))
            slack_value.append(slack_q)
    

# save output
np.savetxt(os.path.join(directory, "overview.txt"), np.column_stack([save_number_of_clones, 
                                                                     dofs,
                                                                     slack_position_list,
                                                                     slack_value,
                                                                     iteration, 
                                                                     final_error,
                                                                     F_time,
                                                                     J_time,
                                                                     linear_solve_time,
                                                                     nonlinear_solve_time,
                                                                     total_time]))