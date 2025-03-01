
"""
Lie Group Analysis of Differential Equations

This module implements Lie group methods for solving differential equations.
It uses Lie symmetry analysis to find symmetry groups of differential equations,
which can then be used to construct solutions or reduce the order of the equations.

Key concepts:
- Infinitesimal generators: Vector fields that generate one-parameter groups of transformations
- Prolongation: Extension of group action to derivative spaces
- Determining equations: System of equations whose solutions give the symmetries

References:
- Olver, P.J. "Applications of Lie Groups to Differential Equations"
- Bluman, G.W. and Kumei, S. "Symmetries and Differential Equations"
"""

import sympy as sp
from sympy import Function, Eq

# Define the independent variable x and dependent variable y(x)
x = sp.symbols('x')
y = Function('y')(x)

# Define the second-order differential equation
# Here we use the example y'' + y' = 0 (damped oscillator equation)
# This can be modified for other differential equations
differential_eq = Eq(y.diff(x, x) + y.diff(x), 0)

# Define the infinitesimal generators of the symmetry group
# xi: coefficient of ∂/∂x
# eta: coefficient of ∂/∂y
xi = sp.Function('xi')(x, y)
eta = sp.Function('eta')(x, y)

# Compute the second prolongation of the infinitesimal generators
# This extends the group action to the second derivative
prolongation = sp.diff(eta, x) + (sp.diff(eta, y) - sp.diff(xi, x)) * y.diff(x) - sp.diff(xi, y) * y.diff(x)**2

# Set up and solve the determining equations
# These equations come from the invariance condition
det_eqs = sp.simplify(prolongation - sp.diff(y.diff(x, x), x) - y)

# Solve the system to find the Lie point symmetries
# These symmetries form a Lie algebra of the symmetry group
symmetries = sp.solve(det_eqs, (xi, eta))

# Output the found symmetry transformations
print("The Lie point symmetries of the differential equation are:")
print(symmetries)

# Note: These symmetries can be used to:
# 1. Reduce the order of the differential equation
# 2. Find invariant solutions
# 3. Generate new solutions from known ones
