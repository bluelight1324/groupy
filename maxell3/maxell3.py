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
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the electric field
line1, = ax.plot(x, E[0, :], label='Electric Field (E)', color='blue')

# Plot the magnetic field
line2, = ax.plot(x, B[0, :], label='Magnetic Field (B)', color='red')

# Set titles and labels
ax.set_title('Electromagnetic Wave Propagation')
ax.set_xlabel('Position (m)')
ax.set_ylabel('Field Strength')
ax.legend()
ax.grid(True)

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

