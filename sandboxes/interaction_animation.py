import sys
sys.path.append('..')  # Add the parent directory to the Python path
import numpy as np
from interaction_eqs import *
from tools.vector_utils import *
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')  # Set aspect ratio to be equal

# Create a quiver arrow
Fa = ax.quiver(0, 0, 2, 0, color='red', scale=1, scale_units='xy', angles='xy', label='Fa')
Fb = ax.quiver(0, 0, 1, 0, color='blue', scale=1, scale_units='xy', angles='xy', label='Fb')
Fnet = ax.quiver(0, 0, 0, 0, color='black', scale=1, scale_units='xy', angles='xy', label='Fnet')
Fi = ax.quiver(0, 0, 0, 0, color='green', scale=1, scale_units='xy', angles='xy', label='Fi')

def init():
    return [Fa, Fb, Fnet, Fi]

def animate(frame_number):
    # Rotate the arrow
    angle = np.radians(frame_number)
    Fb.set_UVC(np.cos(angle), np.sin(angle))

    # Update the net force
    sum_x = Fa.U + Fb.U
    sum_y = Fa.V + Fb.V
    Fnet.set_UVC(sum_x, sum_y)

    # Update the interaction force
    Fa_vector = np.array([Fa.U[0], Fa.V[0]])
    Fb_vector = np.array([Fb.U[0], Fb.V[0]])
    Fi_vector = perpendicular_projection_bisection(Fa_vector, Fb_vector)
    Fi.set_UVC(Fi_vector[0], Fi_vector[1])

    return [Fa,Fb,Fnet,Fi]

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
plt.legend()

# # uncomment below to turn the animation into a gif (takes a while to run):
# path = '/Users/cordond/Desktop/test.gif'
# anim.save(path, writer='imagemagick', fps=30)

plt.show()
