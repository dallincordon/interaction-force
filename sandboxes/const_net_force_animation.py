import sys
sys.path.append('..')  # Add the parent directory to the Python path
import numpy as np
from interaction_eqs import *
from tools.vector_utils import *
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

num_frames = 100

def get_Fa_Fb(alpha, beta, Fnet):
    theta = angle_between(Fnet, (1,0))
    R = np.array([[np.cos(theta + alpha), np.cos(theta + beta)],
                  [np.sin(theta + alpha), np.sin(theta + beta)]])
    AB_magnitudes = np.linalg.inv(R) @ (Fnet)
    Fa_length = AB_magnitudes[0]
    Fb_length = AB_magnitudes[1]
    Fa_return = polar_to_cartesian(Fa_length, theta + alpha)
    Fb_return = polar_to_cartesian(Fb_length, theta + beta)
    return Fa_return, Fb_return

increment_alpha = 0
increment_beta = 0

fig, ax = plt.subplots()
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-4.5, 4.5)
ax.set_aspect('equal')  # Set aspect ratio to be equal

Fnet_angle = np.pi/16
Fnet_init = polar_to_cartesian(3, Fnet_angle)
alpha_init = np.deg2rad(80)
beta_init = np.deg2rad(-60)
Fa_init, Fb_init = get_Fa_Fb(alpha_init, beta_init, Fnet_init)

Fa_magnitude = get_magnitude(Fa_init)
Fb_magnitude = get_magnitude(Fb_init)


# Create a quiver arrow
Fa = ax.quiver(0, 0, Fa_init[0], Fa_init[1], color='red', scale=1, scale_units='xy', angles='xy', label='Fa')
Fb = ax.quiver(0, 0, Fb_init[0], Fb_init[1], color='blue', scale=1, scale_units='xy', angles='xy', label='Fb')
Fnet = ax.quiver(0, 0, Fnet_init[0], Fnet_init[1], color='black', scale=1, scale_units='xy', angles='xy', label='Fnet')
# Fi = ax.quiver(0, 0, 0, 0, color='green', scale=1, scale_units='xy', angles='xy', label='Fi')

# Create a line to trace the arrow tip
line_Fa, = ax.plot([], [], color='red', label='Fa Tip Trace', linestyle=':')
line_Fb, = ax.plot([], [], color='blue', label='Fb Tip Trace', linestyle=':')

def init():
    return [Fa, Fb, Fnet, line_Fa, line_Fb]

def animate(frame_number):
    global increment_alpha
    global increment_beta

    Fa_vector = np.array([Fa.U[0], Fa.V[0]])
    Fb_vector = np.array([Fb.U[0], Fb.V[0]])
    Fnet_vector = np.array([Fnet.U[0], Fnet.V[0]])

    if frame_number == 0:
        increment_alpha = angle_between(Fa_vector, Fnet_vector)/num_frames
        increment_beta = angle_between(Fb_vector, Fnet_vector)/num_frames
        if Fa_vector[1] < Fnet_vector[1]:
            increment_alpha *= -1
        if Fb_vector[1] < Fnet_vector[1]:
            increment_beta *= -1
    
    # FIXME Issue might be here:
    alpha = angle_between(Fa_vector, Fnet_vector)
    beta = angle_between(Fb_vector, Fnet_vector)

    if is_vector_endpoint_above_vector_slope(Fa_vector, Fnet_vector) == False:
        alpha *= -1
    if is_vector_endpoint_above_vector_slope(Fb_vector, Fnet_vector) == False:
        beta *= -1

    alpha -= increment_alpha
    beta -= increment_beta

    Fa_new, Fb_new = get_Fa_Fb(alpha, beta, Fnet_vector)
    Fa_length = get_magnitude(Fa_new)
    Fb_length = get_magnitude(Fb_new)

    Fa.set_UVC(Fa_new[0], Fa_new[1])
    Fb.set_UVC(Fb_new[0], Fb_new[1])

    # print(f"Alpha: {np.rad2deg(alpha)}")
    # print(f"Beta: {np.rad2deg(beta)}")

    # # Update the interaction force
    # Fi_vector = perpendicular_projection_bisection(Fa_vector, Fb_vector)
    # Fi.set_UVC(Fi_vector[0], Fi_vector[1])

    # Update the line to trace the arrow tip
    for line, force in zip([line_Fa, line_Fb], [Fa, Fb]):
        x, y = line.get_data()
        x = np.append(x, force.U)
        y = np.append(y, force.V)
        line.set_data(x, y)

    if frame_number == num_frames - 1:
        increment_alpha = 0
        increment_beta = 0

    return [Fa,Fb,Fnet,line_Fa,line_Fb]

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=20, blit=True)
plt.legend()

# uncomment below to turn the animation into a gif (takes a while to run):
path = '/Users/cordond/Desktop/test.gif'
anim.save(path, writer='imagemagick', fps=30)

plt.show()
