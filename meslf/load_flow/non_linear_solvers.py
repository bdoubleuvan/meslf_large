"""
Class to solve non-linear system of equations arising from steady-state
load flow problems
"""

import abc
import os

# import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.optimize as spo
import time

from meslf.load_flow.system_of_equations import NonLinearSystem, NonLinearSystemGas, NonLinearSystemElectrical, NonLinearSystemHeterogeneous
from meslf.load_flow.idrs import idrs
# from petsc4py import PETSc

# %% counter for iterative solver

class callback(object):
    def __init__(self, iteration_nr, directory):
        self.iteration_nr = iteration_nr
        self.filename = os.path.join(directory, "{:d}.txt".format(self.iteration_nr))

    def __call__(self, iteration_outer, iteration_inner, residual, relative_residual):
        f = open(self.filename, 'a')
        line = "{:5d} {:5d} {:23.16e} {:23.16e} \n".format(iteration_outer, 
                                                           iteration_inner, 
                                                           residual, 
                                                           relative_residual)
        f.write(line)
        f.close()

# %% Abstract class

class Solver(metaclass=abc.ABCMeta):
    """
    Abstract base class for non-linear solver.
    """

    @abc.abstractmethod
    def solve(self, nlsys, x_init):
        """
        Abstract (instance) method to solve nlsys.F(x)=0, starting at x_init

        Parameters
        ----------
        nlsys : NonLinearSystem
                Non-linear system to be solved.
        x_init : np array
                 Initial guess.
        """


# %% Newton-Raphson

class NR(Solver):
    """
    Class for using basic Newton-Raphson with analytical Jacobian.

    Attributes
    ----------
    errors : list
        list with error per iteration
    iterations : int
        iteration number
    tol : float
        Tolerance :math:`\varepsilon` of NR. Default is :math:`\varepsilon = 10^{-6}`

    Returns
    -------
    x : np array
        the latest vector x
    """
    # %% constructor

    def __init__(self, tol=1e-6):
        self.x = None
        
        self.tol = tol
        
        self.errors = []
        self.iterations = 0

        self.linear_solve_times = []
        self.nonlinear_solve_times = []
        self.total_time = 0
        
        self.F_times = []
        self.J_times = []
        
        self.sv = [[], [], []]

    # %% condition number

    def get_condition_number(self, J, s, s_min, s_max, condition_number):
        # We compute all singular values, because sp.linalg.svds does not converge for small GasLib-582 and larger
        if type(J) is np.ndarray:
            s.append(sp.linalg.svdvals(J))
        else:
            s.append(sp.linalg.svdvals(J.todense()))

        s_min.append(s[-1][-1])
        s_max.append(s[-1][0])

        if s_min[-1] > 0:
            condition_number.append(s_max[-1] / s_min[-1])
        else:
            condition_number.append(np.inf)

    # %% determinant

    def get_determinant(self):
        self.determinant.append(np.linalg.det(self.J.todense()))

    # %% eigenvalue

    def get_eigenvalue(self, J, eigenvalue):
        if type(J) is np.ndarray:
            eigenvalue.append(sp.linalg.eigvals(J))
        else:
            eigenvalue.append(sp.linalg.eigvals(J.todense()))
            
    def get_eigen(self):
        self.eigenvalue_initial, self.eigenvector = sp.linalg.eig(self.J.todense())

    # %% symmetric

    def get_symmetric(self):
        symmetric = np.sqrt(np.sum(abs(self.J - self.J.T) ** 2)) / np.sqrt(np.sum(abs(self.J) ** 2)) < 1e-10
        self.symmetric.append(symmetric)

    # %% svd

    def get_svd(self, check_condition_number):
        self.U, self.s_initial, self.Vh = sp.linalg.svd(self.J.todense())

    # %% rank

    def get_rank(self):
        rank_J = np.linalg.matrix_rank(self.J.todense())
        print("Information of initial Jacobian obtained with SVD")
        print("Rank = {}".format(rank_J))
        print("Dimension = {}".format(self.J.shape))
        if self.J.shape[0] - rank_J > 0:
            print("Number of zero rows of initial Jacobian = ", \
                  np.sum(np.isclose(np.sum(abs(self.J), dtype=np.float64, axis=1), 0)))
            print("Number of zero columns of initial Jacobian = ", \
                  np.sum(np.isclose(np.sum(abs(self.J), dtype=np.float64, axis=0), 0)))

    # %% Jacobi preconditioner

    def jacobi(self, A, b, block=False):
        if block is False:
            A_diagonal = A.diagonal()
            # A_diagonal[A_diagonal == 0] = 1
            return b / A_diagonal
        else:
            A_diagonal = A
            return sp.sparse.linalg.spsolve(A=A_diagonal, b=b, permc_spec='natural', use_umfpack=False)
        

    # %% Gauss-Seidel preconditioner

    def gauss(self, A, b):
        A_tril = sp.sparse.tril(A, k=0, format='csr')
        # A_diagonal = A.diagonal()
        # A_diagonal[A.diagonal() == 0] = 1
        # A_diagonal[A.diagonal() != 0] = 0
        # A_tril = A_tril + sp.sparse.diags(A_diagonal)

        # return sp.sparse.linalg.spsolve(A=A_tril, b=b, permc_spec='natural', use_umfpack=False)
        return sp.sparse.linalg.spsolve_triangular(A=A_tril, b=b)

    # %% Incomplete LU factorisation

    def ilu(self, A, b, lin_solver_parameters, solve=True):
        # try:
        M_x = sp.sparse.linalg.spilu(A=A.tocsc(),
                                     diag_pivot_thresh=lin_solver_parameters['diag_pivot_thresh'],
                                     drop_rule=lin_solver_parameters['drop_rule'],
                                     drop_tol=lin_solver_parameters['drop_tol'], 
                                     fill_factor=lin_solver_parameters['fill_factor'], 
                                     permc_spec=lin_solver_parameters['permc_spec'],
                                     options=lin_solver_parameters['options'])
        # except: #shift, if breakdown
        #     print("Shifted matrix with {}".format(lin_solver_parameters['shift_value']))
        #     M_x = sp.sparse.linalg.spilu(A=A + lin_solver_parameters['shift_value']*sp.sparse.eye(A.shape[0]),
        #                                  drop_rule=lin_solver_parameters['drop_rule'],
        #                                  drop_tol=lin_solver_parameters['drop_tol'],
        #                                  fill_factor=lin_solver_parameters['fill_factor'],
        #                                  permc_spec=lin_solver_parameters['permc_spec'])

        # print(M_x.nnz, A.nnz)
        
        if solve:
            return M_x.solve(b)
        else:
            Pr = sp.sparse.csc_array((np.ones(M_x.shape[0]), (M_x.perm_r, np.arange(M_x.shape[0]))))
            Pc = sp.sparse.csc_array((np.ones(M_x.shape[0]), (np.arange(M_x.shape[0]), M_x.perm_c)))
            return Pr.T @ (M_x.L @ M_x.U) @ Pc.T
     
        
    # Block ILUTP
        
    def block_ilu(self, A, b, lin_solver_parameters):
        M_11 = sp.sparse.linalg.spilu(A=A[:lin_solver_parameters['block_size'], :lin_solver_parameters['block_size']].tocsc(),
                                      diag_pivot_thresh=lin_solver_parameters['diag_pivot_thresh'],
                                      drop_rule=lin_solver_parameters['drop_rule'],
                                      drop_tol=lin_solver_parameters['drop_tol'], 
                                      fill_factor=lin_solver_parameters['fill_factor_11'], 
                                      permc_spec=lin_solver_parameters['permc_spec'],
                                      options=lin_solver_parameters['options'])
        
        M_22 = sp.sparse.linalg.spilu(A=A[lin_solver_parameters['block_size']:, lin_solver_parameters['block_size']:].tocsc(),
                                      diag_pivot_thresh=lin_solver_parameters['diag_pivot_thresh'],
                                      drop_rule=lin_solver_parameters['drop_rule'],
                                      drop_tol=lin_solver_parameters['drop_tol'], 
                                      fill_factor=lin_solver_parameters['fill_factor_22'], 
                                      permc_spec=lin_solver_parameters['permc_spec'],
                                      options=lin_solver_parameters['options'])
        
        x = np.zeros(b.shape[0])
        
        x[:lin_solver_parameters['block_size']] = M_11.solve(b[:lin_solver_parameters['block_size']])
        x[lin_solver_parameters['block_size']:] = M_22.solve(b[lin_solver_parameters['block_size']:])
        
        print(M_11.nnz, M_22.nnz, A.nnz)
        
        return x
        
    # %% Kaczmarz

    def kaczmarz(self, A, b):
        return A.multiply(1 / A.multiply(A).sum(1) / A.shape[0]).transpose() @ b
    
    # %% set preconditioner for blocks, returns a method that returns the solution

    def set_preconditioner(self, preconditioner, lin_solver_parameters):
        if preconditioner == 'jacobi':
            def method(A, b): return self.jacobi(A=A, b=b, block=True)
        elif preconditioner == 'gauss':
            def method(A, b): return self.gauss(A=A, b=b)
        elif preconditioner == 'ilu':
            def method(A, b): return self.ilu(A=A, b=b, lin_solver_parameters=lin_solver_parameters)
        else:
            def method(A, b): return b

        return method

    # %% homogeneous block preconditioner

    def block_preconditioner(self, A, b, lin_solver_parameters):
        x = b.copy()

        method = self.set_preconditioner(lin_solver_parameters['preconditioner'], lin_solver_parameters)
  
        block_size = lin_solver_parameters['block_size']

        if A.shape[0] % block_size:
            number_of_blocks = (A.shape[0] // block_size) + 1
        else:
            number_of_blocks = A.shape[0] // block_size

        index_start = 0
        index_end = 0
        for i in range(number_of_blocks - 1):
            index_start = index_end
            index_end += block_size
            try:
                x[index_start:index_end] = method(A[index_start:index_end, index_start:index_end], b[index_start:index_end])
            except:
                pass

        try:
            x[index_end:] = method(A[index_end:, index_end:], b[index_end:])
        except:
            pass

        return x

    # %% heterogeneous block preconditioner

    def block_with_different_preconditioners(self, A, b, lin_solver_parameters):
        x = b.copy()

        index_start = 0
        index_end = 0
        for stride, preconditioner in zip(lin_solver_parameters['block_size'], lin_solver_parameters['preconditioners_for_blocks']):
            index_start = index_end
            index_end += stride
            try:
                method = self.set_preconditioner(preconditioner, lin_solver_parameters)
                x[index_start:index_end] = method(A[index_start:index_end, index_start:index_end], 
                                                  b[index_start:index_end])
            except:
                pass

        try:
            x[index_end:] = method(A[index_end:, index_end:], b[index_end:])
        except:
            pass

        return x
    
    # %% two-level preconditionr    
    
    def two_level(self, A, b, lin_solver_parameters):
        return self.jacobi(A, self.ilu(A, b, lin_solver_parameters), block=False)

    # %% construct preconditioner

    def construct_preconditioner(self, lin_solver_parameters, solve=True):   
        if lin_solver_parameters['preconditioner'] == 'jacobi':
            self.M_x = lambda b: self.jacobi(A=self.J, b=b, block=False)
        elif lin_solver_parameters['preconditioner'] == 'gauss':
            self.M_x = lambda b: self.gauss(A=self.J, b=b)
        elif lin_solver_parameters['preconditioner'] == 'ilu':
            self.M_x = lambda b: self.ilu(A=self.J, b=b, lin_solver_parameters=lin_solver_parameters, solve=solve)
        elif lin_solver_parameters['preconditioner'] == 'ilu_constant':
            self.M_x = lambda b: self.ilu(A=self.J_init, b=b, lin_solver_parameters=lin_solver_parameters)
        elif lin_solver_parameters['preconditioner'] == 'block_ilu':
            self.M_x = lambda b:  self.block_ilu(A=self.J, b=b, lin_solver_parameters=lin_solver_parameters)
        elif lin_solver_parameters['preconditioner'] == 'kaczmarz':
            self.M_x = lambda b: self.kaczmarz(A=self.J, b=b)
        elif lin_solver_parameters['preconditioner'] == 'block':
            self.M_x = lambda b: self.block_preconditioner(A=self.J,
                                                           b=b,
                                                           lin_solver_parameters=lin_solver_parameters)
        elif lin_solver_parameters['preconditioner'] == 'block_with_different_preconditioners':
            self.M_x = lambda b: self.block_with_different_preconditioners(A=self.J, 
                                                                           b=b, 
                                                                           lin_solver_parameters=lin_solver_parameters)
        elif lin_solver_parameters['preconditioner'] == 'two-level':
            self.M_x = lambda b: self.two_level(A=self.J,
                                                b=b,
                                                lin_solver_parameters=lin_solver_parameters)
        else:
            if lin_solver_parameters['preconditioner'] is not None:
                print("Not implemented or invalid input. Default to no preconditioner.")
            self.M_x = None

        if self.M_x is None:
            self.M = None
        else:
            self.M = sp.sparse.linalg.LinearOperator(self.J.shape, self.M_x)

    # %% objective function for optimal multiplier

    def objective_function(self, mu, x, dx, nlsys=None, T_F=None, T_F_len=None, T_x_inv=None, T_x_len=None):
        if T_F_len and T_x_len:
            return np.linalg.norm(T_F.dot(nlsys.F(T_x_inv.dot(x - mu * dx))))
        else:
            return np.linalg.norm(nlsys.F(x - mu * dx))

    # %% derivative of objective function for optimal multiplier

    def der_objective_function(self, mu, x, dx, nlsys=None, T_F=None, T_F_len=None, T_x_inv=None, T_x_len=None):
        if T_F_len and T_x_len:
            return T_F.dot(nlsys.F(T_x_inv.dot(x - mu * dx))).dot(T_F.dot(nlsys.J(x - mu * dx)).dot(T_x_inv.dot(dx)))
        else:
            return nlsys.F(x - mu * dx).dot(nlsys.J(x - mu * dx).dot(dx))

    # %% optimal multiplier method

    def optimal_multiplier_method(self, optimal_multiplier, x, dx, nlsys, T_F, T_F_len, T_x_inv, T_x_len):
        cost = self.objective_function(mu=1, 
                                       x=x, 
                                       dx=0*dx, 
                                       nlsys=nlsys, 
                                       T_F=T_F, 
                                       T_F_len=T_F_len, 
                                       T_x_inv=T_x_inv, 
                                       T_x_len=T_x_len)

        if optimal_multiplier is True:
            mu = sp.optimize.minimize(lambda mu: self.objective_function(mu, x=x, dx=dx, nlsys=nlsys, T_F=T_F, T_F_len=T_F_len, T_x_inv=T_x_inv, T_x_len=T_x_len),
                                      x0=1,
                                      method='L-BFGS-B',
                                      bounds=((0, 1),),
                                      tol=1e-12)

            mu = mu.x[0]

            if abs(mu) > 1e-10: # close to 0
                cost_mu = self.objective_function(mu=mu, x=x, dx=dx, nlsys=nlsys, T_F=T_F, T_F_len=T_F_len, T_x_inv=T_x_inv, T_x_len=T_x_len)
        elif optimal_multiplier == 'Damped':
            mu = 0.95

            cost_mu = self.objective_function(mu=mu, x=x, dx=dx, nlsys=nlsys, T_F=T_F, T_F_len=T_F_len, T_x_inv=T_x_inv, T_x_len=T_x_len)

            i = 1
            while (cost_mu >= cost) and (i < 100):
                mu *= 0.95
                cost_mu = self.objective_function(mu=mu, x=x, dx=dx, nlsys=nlsys, T_F=T_F, T_F_len=T_F_len, T_x_inv=T_x_inv, T_x_len=T_x_len)
                i += 1

        if cost_mu < cost: # if objective function has decreased
            dx = mu * dx

        return dx

    # %% solver

    def solve(self, network, nlsys, x_init, *args, \
              solver_parameters={}, lin_solver='lu', lin_solver_parameters={}, \
              post_processing=True, bounded=False, **kwargs):
        """
        The Newton-Raphson method. Iterations are stopped if the error is
        smaller than the specified tolerance, if the iteration number is
        larger than the specified maximum number of iterations.

        Parameters
        ----------
        network : Network
            Network to be solved.
        nlsys : NonLinearSystem
            Non-linear system to be solved.
        x_init : numpy array
            Initial guess.
        solver_parameters : dict
            Contains essential parameters for the solver.
        lin_solver : str
            Selecting method to solve linear system. Default is 'lu', which use an LU factorisation. 
            Other options are iterative methods:
            'bicgstab',
            'gmres',
            'idr',
            'lsqr'.
        lin_solver_parameters : dict
            Contains essential parameters for the solver.
        post_processing : bool
            Adjusts the solution after the last solution. For gas networks, 
            pressure at nodes connected with only high pressure elements are changed to positive pressures.
            
        Warns
        ------
        UserWarning
            If the linear solver did not reach convergence at some NR iteration.

        Raises
        ------
        TypeError
            If nlsys is not an instance of NonLinearSystem.
        ValueError
            If an incompatible or invalid linear solver is provided.
        """
        start_time = time.perf_counter()

        if not isinstance(nlsys, NonLinearSystem):
            raise TypeError("nlsys has to be an instance of NonLinearSystem")

        # Initial guess
        self.x = x_init
        
        if post_processing:
            # Post processing new iterate
            if type(nlsys) in [NonLinearSystemElectrical]:
                self.x = nlsys.delta_check(self.x)  # keep voltage angles within 0 <= delta < 2*pi        
        
        network.update(x=self.x)
        
        # Construct right-hand-side
        start_F_time = time.perf_counter()
        self.F = nlsys.F(self.x)
        self.F_times.append(time.perf_counter() - start_F_time)

        self.errors.append(np.linalg.norm(self.F)) # residual
        
        if lin_solver_parameters['get_initial']:
            self.J_init = nlsys.J(self.x)
            if lin_solver in {'direct', 'lu'}:
                self.lu_init = sp.sparse.linalg.splu(self.J_init, permc_spec=lin_solver_parameters['permc_spec'])
            else:
                if lin_solver_parameters['preconditioner'] in {'ilu'}:
                    self.lu_init = sp.sparse.linalg.spilu(A=self.J_init.tocsc(),
                                                          diag_pivot_thresh=lin_solver_parameters['diag_pivot_thresh'],
                                                          drop_rule=lin_solver_parameters['drop_rule'],
                                                          drop_tol=lin_solver_parameters['drop_tol'], 
                                                          fill_factor=lin_solver_parameters['fill_factor'], 
                                                          permc_spec=lin_solver_parameters['permc_spec'],
                                                          options=lin_solver_parameters['options'])
            
        
        # print(["iterations = {}, q_c = {}, P_c = {}".format(self.iterations, self.x[-2], self.x[-1])])
        # Start Newton-Raphson
        print("Iteration = {:3d} | Residual = {:.3e}".format(self.iterations, self.errors[-1]))
        while (self.errors[-1] > self.tol) and (self.iterations < solver_parameters['max_iterations']):
            self.iterations += 1
            
            # Construct Jacobian
            start_J_time = time.perf_counter()
            self.J = nlsys.J(self.x)
            self.J_times.append(time.perf_counter() - start_J_time)
            
            if lin_solver_parameters['get_condition_number']:
                print("Computing singular values")
                self.sv[0].append(sp.sparse.linalg.svds(self.J, return_singular_vectors=False, k=1, which='SM', 
                                                        solver='lobpcg', tol=10**-6, maxiter=2*10**4)[0])
                print("Smallest singular value = {:.3e}".format(self.sv[0][-1]))
                
                self.sv[1].append(sp.sparse.linalg.svds(self.J, return_singular_vectors=False, k=1, which='LM', 
                                                        solver='lobpcg', tol=10**-6, maxiter=2*10**4)[0])
                print("Largest singular value = {:.3e}".format(self.sv[1][-1]))
                
                self.sv[2].append(self.sv[1][-1] / self.sv[0][-1])
                print("Condition number = {:.3e}".format(self.sv[2][-1]))

            linear_solve_start_time = time.perf_counter()
            
            if lin_solver_parameters['rcm']:
                index_rcm = sp.sparse.csgraph.reverse_cuthill_mckee(self.J)
                self.J = self.J[index_rcm, :][:, index_rcm]
                self.F = self.F[index_rcm]

            if lin_solver_parameters['reorderfornonzerodiagonal']:
                index_nz_diag = sp.sparse.csgraph.min_weight_full_bipartite_matching(self.J != 0, maximize=True)[1]
                self.J = self.J[:, index_nz_diag]

            try:
                if lin_solver == 'lu':
                        dx = sp.sparse.linalg.spsolve(self.J, 
                                                      self.F,
                                                      permc_spec=lin_solver_parameters['permc_spec'], 
                                                      use_umfpack=False)
                elif lin_solver in ['bicgstab', 'gmres', 'idr', 'lsqr']:
                    if (self.iterations == 1) and (lin_solver_parameters['preconditioner'] == 'ilu_constant'):
                        print("Copied Jacobian in iteration ", self.iterations)
                        self.J_init = self.J.copy()
                    
                    # Construct a linear operator that computes M^-1 @ x = y.
                    self.construct_preconditioner(lin_solver_parameters=lin_solver_parameters)
     
                    if lin_solver == 'bicgstab':
                        dx, info = sp.sparse.linalg.bicgstab(A=self.J,
                                                             b=self.F,
                                                             x0=np.zeros(self.x.shape[0]),
                                                             maxiter=lin_solver_parameters['max_iterations'],
                                                             rtol=lin_solver_parameters['tol'],
                                                             atol=lin_solver_parameters['tol'] * self.errors[-1],
                                                             M=self.M,
                                                             callback=None)
                                                             #  callback=callback(A=self.J,
                                                             #                    b=self.F,
                                                             #                    M=self.M,
                                                             #                    filename=lin_solver_parameters['filename']))
                    elif lin_solver == 'gmres':
                        if lin_solver_parameters['residuals_directory'] is not None:
                            dx, info = sp.sparse.linalg.gmres(A=self.J,
                                                              b=self.F,
                                                              x0=np.zeros(self.x.shape[0]),
                                                              maxiter=lin_solver_parameters['max_iterations'],
                                                              rtol=lin_solver_parameters['tol'],
                                                              atol=lin_solver_parameters['tol'] * self.errors[-1],
                                                              M=self.M,
                                                              restart=lin_solver_parameters['gmres_restart'],
                                                              callback=callback(self.iterations, lin_solver_parameters['residuals_directory']),
                                                              callback_type='custom')
                        else:
                            dx, info = sp.sparse.linalg.gmres(A=self.J,
                                                              b=self.F,
                                                              x0=np.zeros(self.x.shape[0]),
                                                              maxiter=lin_solver_parameters['max_iterations'],
                                                              rtol=lin_solver_parameters['tol'],
                                                              atol=lin_solver_parameters['tol'] * self.errors[-1],
                                                              M=self.M,
                                                              restart=lin_solver_parameters['gmres_restart'])
                    elif lin_solver == 'idr':
                        dx, info = idrs(A=self.J,
                                        b=self.F,
                                        x0=np.zeros(self.x.shape[0]),
                                        maxiter=lin_solver_parameters['max_iterations'],
                                        tol=lin_solver_parameters['tol'], #relative residual
                                        M=self.M,
                                        s=lin_solver_parameters['idr_s'],
                                        callback=None)
                                        # callback=callback(A=self.J,
                                        #                   b=self.F,
                                        #                   M=self.M,
                                        #                   filename=lin_solver_parameters['filename']))
                    elif lin_solver == 'lsqr':
                        dx, info, _, _, _, _, _, _, _, _ = sp.sparse.linalg.lsqr(A=self.J,
                                                                                 b=self.F,
                                                                                 x0=None,
                                                                                 iter_lim=lin_solver_parameters['max_iterations'],
                                                                                 btol=lin_solver_parameters['tol'],
                                                                                 atol=lin_solver_parameters['tol'])   
                elif lin_solver == 'petsc':
                    J_petsc = PETSc.Mat().createAIJ(size=self.J.shape, 
                                                    csr=(self.J.indptr, self.J.indices, self.J.data),
                                                    comm=PETSc.COMM_WORLD)
                    if lin_solver_parameters['petsc_zero_diagonal']:
                        J_petsc = J_petsc + PETSc.Mat().createDiagonal(PETSc.Vec().createWithArray(np.zeros(self.J.shape[0])))       
                    J_petsc.assemble()

                    if lin_solver_parameters['petsc_reorderfornonzerodiagonal']:
                        row, col = J_petsc.getOrdering(lin_solver_parameters['petsc_ord_type'])
                        J_petsc.reorderForNonzeroDiagonal(row, col)

                    ksp = PETSc.KSP()
                    ksp.create(comm=J_petsc.getComm())

                    if lin_solver_parameters['petsc_lin_solver'] == 'lu':
                        ksp.setType('preonly')
                        ksp.getPC().setType('lu')
                        ksp.getPC().setFactorOrdering(ord_type=lin_solver_parameters['petsc_ord_type'], 
                                                      nzdiag=lin_solver_parameters['petsc_nzdiag'], 
                                                      reuse=lin_solver_parameters['petsc_reuse'])
                        if lin_solver_parameters['petsc_shift_amount'] is not None:
                            ksp.getPC().setFactorShift(shift_type=lin_solver_parameters['petsc_shift_type'], amount=lin_solver_parameters['petsc_shift_amount'])
                    else:
                        ksp.setType(lin_solver_parameters['petsc_lin_solver'])

                        if lin_solver_parameters['petsc_lin_solver'] == 'gmres':
                            ksp.setGMRESRestart(restart=lin_solver_parameters['petsc_gmres_restart'])

                        if lin_solver_parameters['petsc_preconditioner'] is not None:
                            ksp.getPC().setType(lin_solver_parameters['petsc_preconditioner'])

                        ksp.setNormType(1) # 2-norm
                        ksp.setTolerances(rtol=self.tol * 10**-2,
                                          atol=self.tol * self.errors[-1] * 10**-2,
                                          max_it=lin_solver_parameters['petsc_max_iterations'])

                        if lin_solver_parameters['petsc_preconditioner'] == 'ilu':
                            ksp.getPC().setFactorLevels(lin_solver_parameters['petsc_fill-in'])
                            ksp.getPC().setFactorOrdering(ord_type=lin_solver_parameters['petsc_ord_type'], 
                                                          nzdiag=lin_solver_parameters['petsc_nzdiag'], 
                                                          reuse=lin_solver_parameters['petsc_reuse'])
                            if lin_solver_parameters['petsc_shift_amount'] is not None:
                                ksp.getPC().setFactorShift(shift_type=lin_solver_parameters['petsc_shift_type'], amount=lin_solver_parameters['petsc_shift_amount'])
                        elif lin_solver_parameters['petsc_preconditioner'] == 'gamg':
                            if lin_solver_parameters['petsc_gamglevels'] is not None:
                                ksp.getPC().setGAMGLevels(lin_solver_parameters['petsc_gamglevels'])
                            if lin_solver_parameters['petsc_gamglevels'] is not None:
                                ksp.getPC().setGAMGSmooths(lin_solver_parameters['petsc_gamgsmooths'])
                            ksp.getPC().setGAMGType(lin_solver_parameters['petsc_gamgtype'])

                    ksp.setOperators(J_petsc)
                    ksp.setFromOptions()

                    dx, b = J_petsc.createVecs()
                    b.setArray(self.F)

                    ksp.solve(b, dx)

                    dx = dx.getArray()
                else:
                    raise ValueError("Enter a valid value for lin_solver", UserWarning)
            except Exception as e:
                print(e)
                return self.x
            
            self.linear_solve_times.append(time.perf_counter() - linear_solve_start_time)

            # Optimal multiplier
            if solver_parameters['optimal_multiplier']:
                dx = self.optimal_multiplier_method(optimal_multiplier=solver_parameters['optimal_multiplier'],
                                                    x=self.x,
                                                    dx=dx,
                                                    nlsys=nlsys)

            # Reorder update
            if lin_solver_parameters['reorderfornonzerodiagonal']:
                dx = dx[np.argsort(index_nz_diag)]

            if lin_solver_parameters['rcm']:
                dx = dx[np.argsort(index_rcm)]
             
            # Update iterate
            self.x = self.x - dx
            # print(["iterations = {}, q_c = {}, P_c = {}".format(self.iterations, self.x[-2], self.x[-1])])
            if bounded:
                self.x = nlsys.coupling_bounds_check(x=self.x)
                # print(["iterations = {}, q_c = {}, P_c = {}".format(self.iterations, self.x[-2], self.x[-1])])
            
            if post_processing:
                # Post processing new iterate
                if type(nlsys) in [NonLinearSystemElectrical, NonLinearSystemHeterogeneous]:
                    self.x = nlsys.delta_check(self.x)  # keep voltage angles within 0 <= delta < 2*pi
            
            network.update(x=self.x)

            # Update F
            start_F_time = time.perf_counter()
            self.F = nlsys.F(self.x)
            self.F_times.append(time.perf_counter() - start_F_time)

            # Add error
            self.errors.append(np.linalg.norm(self.F)) # residual
            print("Iteration = {:3d} | Residual = {:.3e}".format(self.iterations, self.errors[-1]))
            
            # print(self.errors[-1], self.x[-6:])

            # Add nonlinear solve time
            if len(self.nonlinear_solve_times) == 0:
                self.nonlinear_solve_times.append(time.perf_counter() - start_time)
            else:
                self.nonlinear_solve_times.append(time.perf_counter() - nonlinear_solve_start_time)
            nonlinear_solve_start_time = time.perf_counter()
            
            if type(nlsys) in [NonLinearSystemGas]:
                if solver_parameters['residual_q']:
                    if np.linalg.norm(self.F[:nlsys.index_Fn[-1]]) < self.tol:
                        break

        if post_processing:
            # Post processing new iterate
            if type(nlsys) in [NonLinearSystemGas]: # [NonLinearSystemGas, NonLinearSystemHeterogeneous]:
                self.x = nlsys.p_check(self.x)  # change pressure value to absolute value

        # Total time spent in the non-linear solver
        self.total_time = time.perf_counter() - start_time
        
        return self.x
    
# %% Anderson Acceleration

class AA(Solver):
    """
    Class for using Anderson Acceleration (AA).

    Attributes
    ----------
    errors : list
        list with error per iteration
    iterations : int
        iteration number
    tol : float
        Tolerance :math:`\varepsilon` of AA. Default is :math:`\varepsilon = 10^{-6}`
          
    Returns
    -------
    x : np array
        the latest vector x
    """
    
    def __init__(self, tol=1e-6):
        self.tol = tol
        
        self.errors = []        
        self.iterations = 0
        
        self.nonlinear_solve_times = []

       
    def solve(self, network, nlsys, x_init, *args, \
              solver_parameters={}, post_processing=True, **kwargs):        
        total_start_time = time.perf_counter()

        if not isinstance(nlsys, NonLinearSystem):
            raise TypeError("nlsys has to be an instance of NonLinearSystem")
        
        def F(x):
            return x - nlsys.F(x)
                
        if post_processing:
            # Post processing new iterate
            if type(nlsys) in [NonLinearSystemElectrical]:
                x_init = nlsys.delta_check(x_init)  # keep voltage angles within 0 <= delta < 2*pi
                
        network.update(x=x_init) # update network
        
        self.x = F(x=x_init)
        
        if post_processing:
            # Post processing new iterate
            if type(nlsys) in [NonLinearSystemElectrical]:
                self.x = nlsys.delta_check(self.x)  # keep voltage angles within 0 <= delta < 2*pi
        
        network.update(x=self.x)
        
        x = [x_init, self.x] # list of approximations
        
        g = [x[1] - x[0], F(x[1]) - x[1]] # list of residuals
        G = np.array(g[1] - g[0]).reshape(len(x_init), 1) # list of residual differences
        X = np.array(x[1]- x[0]).reshape(len(x_init), 1) # list of approximation differences
    
        self.errors.append(np.linalg.norm(g[0]))
        self.errors.append(np.linalg.norm(g[1]))
        
        self.iterations = 2
        while (self.errors[-1] > self.tol) and (self.iterations < solver_parameters['max_iterations']):
            theta = sp.linalg.lstsq(G, g[1])[0]
            
            x[0] = x[1]
            g[0] = g[1]
            x[1] = x[0] + g[0] - (X + G) @ theta
            
            self.x = x[1]
            
            if post_processing:
                # Post processing new iterate
                if type(nlsys) in [NonLinearSystemElectrical]:
                    self.x = nlsys.delta_check(self.x)  # keep voltage angles within 0 <= delta < 2*pi
            
            network.update(x=self.x)
            
            g[1] = F(x[1]) - x[1]
            
            X = np.column_stack((X, x[1] - x[0]))
            G = np.column_stack((G, g[1] - g[0]))
            
            n = X.shape[1]
            if n > solver_parameters['m']:
                X = X[:, n-solver_parameters['m']:]
                G = G[:, n-solver_parameters['m']:]

            self.errors.append(np.linalg.norm(g[1]))
                        
            self.iterations += 1
                            
            if len(self.nonlinear_solve_times) == 0:
                self.nonlinear_solve_times.append(time.perf_counter() - total_start_time)
            else:
                self.nonlinear_solve_times.append(time.perf_counter() - nonlinear_solve_start_time)
            nonlinear_solve_start_time = time.perf_counter()
            
        if post_processing:
            if type(nlsys) in [NonLinearSystemGas]:
                self.x = nlsys.p_check(x=self.x)  # change pressure value to absolute value

        # Total time spent in the non-linear solver
        self.total_time = time.perf_counter() - total_start_time
        
        return self.x
    
# %% Fixed Point

class FP(Solver):
    """
    Class for using Fixed Point (FP).

    Attributes
    ----------
    errors : list
        list with error per iteration
    iterations : int
        iteration number
    tol : float
        Tolerance :math:`\varepsilon` of FP. Default is :math:`\varepsilon = 10^{-6}`
          
    Returns
    -------
    x : np array
        the latest vector x
    """
    
    def __init__(self, tol):
        self.tol = 1e-6
        
        self.errors = []
        self.iterations = 0
        
        self.nonlinear_solve_times = []
        
    def solve(self, network, nlsys, x_init, *args,
              solver_parameters={}, post_processing=True, **kwargs):
        
        total_start_time = time.perf_counter()

        if not isinstance(nlsys, NonLinearSystem):
            raise TypeError("nlsys has to be an instance of NonLinearSystem")
        
        def F(x):
            return x - nlsys.F(x)
                
        self.x = x_init
        
        if post_processing:
            # Post processing new iterate
            if type(nlsys) in [NonLinearSystemElectrical]:
                self.x = nlsys.delta_check(self.x)  # keep voltage angles within 0 <= delta < 2*pi
        
        network.update(x=self.x)
        
        self.errors.append(np.linalg.norm(nlsys.F(self.x)))
        
        while (self.errors[-1] > self.tol) and (self.iterations < solver_parameters['max_iterations']):
            self.iterations += 1
            
            self.x = F(self.x)
            
            if post_processing:
                # Post processing new iterate
                if type(nlsys) in [NonLinearSystemElectrical]:
                    self.x = nlsys.delta_check(self.x)  # keep voltage angles within 0 <= delta < 2*pi
            
            network.update(x=self.x)
            self.errors.append(np.linalg.norm(nlsys.F(self.x)))
               
            if len(self.nonlinear_solve_times) == 0:
                self.nonlinear_solve_times.append(time.perf_counter() - total_start_time)
            else:
                self.nonlinear_solve_times.append(time.perf_counter() - nonlinear_solve_start_time)
            nonlinear_solve_start_time = time.perf_counter()

        if post_processing:
            if type(nlsys) in [NonLinearSystemGas]:
                self.x = nlsys.p_check(self.x)  # change pressure value to absolute value

        # Total time spent in the non-linear solver
        self.total_time = time.perf_counter() - total_start_time
        
        return self.x
