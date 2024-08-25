
import sympy as sp

# Define the variables
x, y, u = sp.symbols('x y u')
f = sp.Function('f')(x, y)

# Define the PDE (example: u_xx + u_yy = 0)
pde = sp.Eq(f.diff(x, x) + f.diff(y, y), 0)

# Display the PDE
print(f"PDE: {pde}")

# Define the infinitesimals
xi = sp.Function('xi')(x, y, u)
eta = sp.Function('eta')(x, y, u)

# Calculate the prolongation
u_x = f.diff(x)
u_y = f.diff(y)
prolongation = eta - xi.diff(x) * u_x - xi.diff(y) * u_y

# Display the prolongation
print(f"Prolongation: {prolongation}")

# Solve the determining equations
det_eq = sp.simplify(prolongation.diff(x, x) + prolongation.diff(y, y))
solutions = sp.solve(det_eq, (xi, eta))

# Display the solutions
print(f"Solutions: {solutions}")
