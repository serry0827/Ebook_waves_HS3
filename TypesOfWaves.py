import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
frames = 60                         # Total number of animation frames
x = np.linspace(0, 4 * np.pi, 500)  # X values for transverse wave

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4))
plt.tight_layout(pad=2)

# Setup for transverse wave
trans_line, = ax1.plot([], [], lw=2, color='blue')
ax1.set_xlim(0, 4 * np.pi)
ax1.set_ylim(-1.5, 1.5)
ax1.set_title('Transverse Wave')
ax1.set_yticks([])

# Setup for longitudinal wave
long_dots, = ax2.plot([], [], 'ko', markersize=3)
ax2.set_xlim(0, 4 * np.pi)
ax2.set_ylim(-0.5, 0.5)
ax2.set_title('Longitudinal Wave')
ax2.set_yticks([])

# Particles for the longitudinal wave
num_particles = 60
x_particles = np.linspace(0, 4 * np.pi, num_particles)

# Initialize function (blank frames)
def init():
    trans_line.set_data([], [])
    long_dots.set_data([], [])
    return trans_line, long_dots

# Animation function (updates each frame)
def animate(i):
    phase = 2 * np.pi * i / frames  # Wave phase change over time

    # Transverse wave: y = sin(kx - ωt)
    y_trans = np.sin(x - phase)
    trans_line.set_data(x, y_trans)

    # Longitudinal wave: horizontal oscillation of particles
    x_disp = 0.3 * np.sin(x_particles - phase)
    long_dots.set_data(x_particles + x_disp, np.zeros_like(x_particles))

    return trans_line, long_dots

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=frames, interval=50, blit=True)

# Save as GIF
ani.save("transverse_longitudinal_wave.gif", writer='pillow')
