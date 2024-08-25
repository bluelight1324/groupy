
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
c = 3e8  # Speed of light in vacuum (m/s)
epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (H/m)
omega = 2 * np.pi * 1e8  # Angular frequency (rad/s)
k = omega / c  # Wave number (1/m)

# Time and space arrays
t = np.linspace(0, 2 * np.pi / omega, 100)
x = np.linspace(0, 2 * np.pi / k, 100)

# Create meshgrid for space and time
X, T = np.meshgrid(x, t)

# Electric field as a function of space and time
E = np.sin(k * X - omega * T)

# Magnetic field as a function of space and time
B = (1 / c) * np.sin(k * X - omega * T)

# Set up the figure and axis
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Plot the electric field
ax[0].set_title('Electric Field (E)')
ax[0].set_xlabel('Position (m)')
ax[0].set_ylabel('Electric Field (V/m)')
line1, = ax[0].plot(x, E[0, :], label='E')
ax[0].legend()
ax[0].grid(True)

# Plot the magnetic field
ax[1].set_title('Magnetic Field (B)')
ax[1].set_xlabel('Position (m)')
ax[1].set_ylabel('Magnetic Field (T)')
line2, = ax[1].plot(x, B[0, :], label='B', color='red')
ax[1].legend()
ax[1].grid(True)

# Animation function
def animate(i):
    line1.set_ydata(E[i, :])
    line2.set_ydata(B[i, :])
    return line1, line2

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)

# Show the plot
plt.tight_layout()
plt.show()
