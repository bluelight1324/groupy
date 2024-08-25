
# Import necessary libraries
import sympy as sp
from sympy import Function, Eq

# Define the variables and function
x = sp.symbols('x')
y = Function('y')(x)

# Define the differential equation
# Example: y'' + y = 0
differential_eq = Eq(y.diff(x, x) + y.diff(x), 0)

# Define the infinitesimal generators
xi = sp.Function('xi')(x, y)
eta = sp.Function('eta')(x, y)

# Compute the prolongation
prolongation = sp.diff(eta, x) + (sp.diff(eta, y) - sp.diff(xi, x)) * y.diff(x) - sp.diff(xi, y) * y.diff(x)**2

# Solve the determining equations
det_eqs = sp.simplify(prolongation - sp.diff(y.diff(x, x), x) - y)

# Find the symmetries
symmetries = sp.solve(det_eqs, (xi, eta))

# Output the symmetries
print("The symmetries of the differential equation are:")
print(symmetries)
