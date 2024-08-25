
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
alpha = 0.01  # Thermal diffusivity
L = 1.0      # Length of the rod
T = 10.5      # Total time
nx = 5000000      # Number of spatial points
nt = 100000000     # Number of time points

# Discretize the spatial and time domains
x = np.linspace(0, L, nx)
t = np.linspace(0, T, nt)
dx = x[1] - x[0]
dt = t[1] - t[0]

# Initial condition: u(x, 0) = sin(pi * x / L)
u0 = np.sin(np.pi * x / L)

# Boundary conditions: u(0, t) = u(L, t) = 0
def boundary_conditions(u):
    u[0] = 0
    u[-1] = 0
    return u

# Define the heat equation as a system of ODEs
def heat_equation(t, u):
    dudt = np.zeros_like(u)
    dudt[1:-1] = alpha * (u[2:] - 2 * u[1:-1] + u[:-2]) / dx**2
    return dudt

# Solve the PDE using solve_ivp
sol = solve_ivp(heat_equation, [0, T], u0, t_eval=t, method='RK45')

# Plot the result
X, T = np.meshgrid(x, t)
U = sol.y.T

plt.figure(figsize=(10, 6))
plt.contourf(X, T, U, 20, cmap='hot')
plt.colorbar(label='Temperature')
plt.xlabel('Position (x)')
plt.ylabel('Time (t)')
plt.title('Heat Equation Solution')
plt.show()
