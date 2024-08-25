
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space
N = 100  # Number of turns in the coil
A = 1.0  # Area of the coil (m^2)
B0 = 1.0  # Initial magnetic field strength (T)
omega = 2 * np.pi  # Angular frequency of the magnetic field (rad/s)

# Time array
t = np.linspace(0, 2 * np.pi, 1000)

# Magnetic field as a function of time
B_t = B0 * np.sin(omega * t)

# Induced EMF as a function of time (Faraday's Law: EMF = -N * d?/dt)
EMF_t = -N * A * omega * B0 * np.cos(omega * t)

# Set up the figure and axis
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Plot the magnetic field
ax[0].plot(t, B_t, label='Magnetic Field (B)')
ax[0].set_ylabel('Magnetic Field (T)')
ax[0].set_title('Magnetic Field and Induced EMF')
ax[0].legend()
ax[0].grid(True)

# Plot the induced EMF
ax[1].plot(t, EMF_t, label='Induced EMF (?)', color='red')
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Induced EMF (V)')
ax[1].legend()
ax[1].grid(True)

# Animation function
def animate(i):
    ax[0].cla()
    ax[1].cla()
    
    # Update magnetic field plot
    ax[0].plot(t[:i], B_t[:i], label='Magnetic Field (B)')
    ax[0].set_ylabel('Magnetic Field (T)')
    ax[0].set_title('Magnetic Field and Induced EMF')
    ax[0].legend()
    ax[0].grid(True)
    
    # Update induced EMF plot
    ax[1].plot(t[:i], EMF_t[:i], label='Induced EMF (?)', color='red')
    ax[1].set_xlabel('Time (s)')
    ax[1].set_ylabel('Induced EMF (V)')
    ax[1].legend()
    ax[1].grid(True)

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, repeat=False)

# Show the plot
plt.tight_layout()
plt.show()
