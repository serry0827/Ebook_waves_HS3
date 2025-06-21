import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
frames = 90
x = np.linspace(-10, 10, 1000)
k = 2 * np.pi / 2       # Wave number (spatial frequency)
w = 2 * np.pi / 2       # Angular frequency (temporal frequency)
v = 1                   # Wave speed
alpha = 0.1             # Controls width of the wave packet envelope

# Create figure and axis
fig, ax = plt.subplots(figsize=(9, 3))
plt.tight_layout()
ax.set_xlim(-10, 10)
ax.set_ylim(-2, 2)
ax.set_title("Destructive Interference of Opposing Wave Packets")
ax.set_yticks([])

# Initialize wave lines
wave1_line, = ax.plot([], [], 'b--', label='Wave 1 →')        # Moving right
wave2_line, = ax.plot([], [], 'orange', linestyle='--', label='Wave 2 ←')  # Moving left
total_line, = ax.plot([], [], 'k-', linewidth=2, label='Resulting Wave')

ax.legend(loc='upper right')

# Initialization function
def init():
    wave1_line.set_data([], [])
    wave2_line.set_data([], [])
    total_line.set_data([], [])
    return wave1_line, wave2_line, total_line

# Animation function
def animate(i):
    t = (i-45) * 0.2  # Time step
    # Two opposing wave packets with Gaussian envelopes
    wave1 = np.sin(k * (x - v * t)) * np.exp(-alpha * (x - v * t)**2)
    wave2 = -np.sin(k * (x + v * t)) * np.exp(-alpha * (x + v * t)**2)  # Phase-inverted (destructive)
    total = wave1 + wave2

    wave1_line.set_data(x, wave1)
    wave2_line.set_data(x, wave2)
    total_line.set_data(x, total)
    return wave1_line, wave2_line, total_line

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=frames, interval=50, blit=True)

# Save as GIF
ani.save("packet_destruction.gif", writer='pillow')
