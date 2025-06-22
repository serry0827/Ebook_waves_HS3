import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(9, 3))
ax.set_xlim(0, 9)
ax.set_ylim(0, 3)
ax.axis('off')

# Interface line
interface_y = 1.5
ax.plot([0, 9], [interface_y, interface_y], 'k', lw=2)

# Section titles
ax.text(1, 2.7, 'Reflection', fontsize=14, color='navy')
ax.text(4, 2.7, 'Refraction', fontsize=14, color='navy')
ax.text(7, 2.7, 'Diffraction', fontsize=14, color='navy')

# Plot elements
reflect_ray, = ax.plot([], [], 'r-', lw=2)
refract_ray, = ax.plot([], [], 'r-', lw=2)
diff_incident_ray, = ax.plot([], [], 'r-', lw=2)
diff_rays = [ax.plot([], [], 'r-', lw=2)[0] for _ in range(3)]

n_points = 60

# Reflection
x_reflect_in = np.linspace(1, 2, n_points)
y_reflect_in = 1.5 + (2 - x_reflect_in)
x_reflect_out = np.linspace(2, 3, n_points)
y_reflect_out = 1.5 + (x_reflect_out - 2)

# Refraction
x_refract_in = np.linspace(3.5, 5, n_points)
y_refract_in = 1.5 + (5 - x_refract_in)
x_refract_out = np.linspace(5, 6, n_points)
y_refract_out = 1.5 - 3 * (x_refract_out - 5)

# Diffraction
x_diff_in = np.linspace(6.5, 8, n_points)
y_diff_in = 1.5 + (8 - x_diff_in)
x_diff_out = np.linspace(8, 9, n_points)
angles = [-0.6, 0, 0.6]
y_diff_out = [1.5 + (x_diff_out - 8) * angle for angle in angles]

def init():
    reflect_ray.set_data([], [])
    refract_ray.set_data([], [])
    diff_incident_ray.set_data([], [])
    for ray in diff_rays:
        ray.set_data([], [])
    return reflect_ray, refract_ray, diff_incident_ray, *diff_rays

def animate(i):
    if i < n_points:
        reflect_ray.set_data(x_reflect_in[:i], y_reflect_in[:i])
        refract_ray.set_data(x_refract_in[:i], y_refract_in[:i])
        diff_incident_ray.set_data(x_diff_in[:i], y_diff_in[:i])
    else:
        i2 = i - n_points
        reflect_ray.set_data(np.concatenate([x_reflect_in, x_reflect_out[:i2]]),
                             np.concatenate([y_reflect_in, y_reflect_out[:i2]]))
        refract_ray.set_data(np.concatenate([x_refract_in, x_refract_out[:i2]]),
                             np.concatenate([y_refract_in, y_refract_out[:i2]]))
        diff_incident_ray.set_data(x_diff_in, y_diff_in)
        for j, ray in enumerate(diff_rays):
            ray.set_data(x_diff_out[:i2], y_diff_out[j][:i2])
    return reflect_ray, refract_ray, diff_incident_ray, *diff_rays

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=n_points * 2, interval=20, blit=True)

ani.save("final_light_behaviors.gif", writer='pillow')
