
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the variables
x, y, z = sp.symbols('x y z')

# Define the surface equation F(x, y, z) = 0
# Example: Ellipsoid x^2 + y^2 + z^2 - 1 = 0
F = x**3 + y**3 + z**3 - 1

# Compute the partial derivatives
Fx = sp.diff(F, x)
Fy = sp.diff(F, y)
Fz = sp.diff(F, z)

# Compute the second partial derivatives
Fxx = sp.diff(Fx, x)
Fyy = sp.diff(Fy, y)
Fzz = sp.diff(Fz, z)
Fxy = sp.diff(Fx, y)
Fxz = sp.diff(Fx, z)
Fyz = sp.diff(Fy, z)

# Define the Gaussian curvature formula
E = Fx**2 + Fy**2 + Fz**2
L = Fxx * Fx**2 + 2 * Fxy * Fx * Fy + Fyy * Fy**2 + 2 * Fxz * Fx * Fz + 2 * Fyz * Fy * Fz + Fzz * Fz**2
K = (L / E**2).simplify()

# Convert the Gaussian curvature to a lambda function for numerical evaluation
K_func = sp.lambdify((x, y, z), K, 'numpy')

# Generate points on the surface
u = np.linspace(-1, 1, 100)
v = np.linspace(-1, 1, 100)
U, V = np.meshgrid(u, v)
X = U
Y = V
Z = np.sqrt(1 - X**2 - Y**2)

# Compute the Gaussian curvature at each point
K_values = K_func(X, Y, Z)

# Plot the surface and color it according to the Gaussian curvature
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(K_values), rstride=1, cstride=1, linewidth=0, antialiased=False)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Gaussian Curvature of the Surface')
plt.show()
