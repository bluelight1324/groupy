import numpy as np
import matplotlib.pyplot as plt

# Constants
sigma = 5.67e-8  # Stefan-Boltzmann constant in W m^-2 K^-4
radius = 1.0  # Radius of the sphere in meters

# Surface area of the sphere
A = 4 * np.pi * radius**2

# Temperature range (in Kelvin)
T = np.linspace(100, 1000, 100)  # from 100K to 1000K

# Power radiated
P = sigma * A * T**4

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(T, P, label=f'Radius = {radius} m')
plt.xlabel('Temperature (K)')
plt.ylabel('Power Radiated (W)')
plt.title('Power Radiated by a Sphere as a Function of Temperature')
plt.legend()
plt.grid(True)
plt.show()
