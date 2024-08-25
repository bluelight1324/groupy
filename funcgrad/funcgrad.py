
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variables in polar coordinates
r, theta = sp.symbols('r theta')

# Define the function in polar coordinates
f = r**2 * sp.cos(theta)

# Compute the partial derivatives (gradient components)
f_r = sp.diff(f, r)
f_theta = sp.diff(f, theta)

# Convert the gradient components to lambda functions for numerical evaluation
f_r_func = sp.lambdify((r, theta), f_r, 'numpy')
f_theta_func = sp.lambdify((r, theta), f_theta, 'numpy')

# Generate a grid of points in polar coordinates
r_vals = np.linspace(0, 2, 100)
theta_vals = np.linspace(0, 2 * np.pi, 100)
R, Theta = np.meshgrid(r_vals, theta_vals)

# Evaluate the gradient components at each point
F_r = f_r_func(R, Theta)
F_theta = f_theta_func(R, Theta)

# Convert polar coordinates to Cartesian coordinates for plotting
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Convert the gradient components to Cartesian coordinates
F_x = F_r * np.cos(Theta) - F_theta * np.sin(Theta) / R
F_y = F_r * np.sin(Theta) + F_theta * np.cos(Theta) / R

# Plot the gradient field
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, F_x, F_y, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gradient Field of f(r, θ) = r^2 cos(θ) in Polar Coordinates')
plt.grid(True)
plt.axis('equal')
plt.show()
