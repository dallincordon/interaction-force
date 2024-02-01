import sys
sys.path.append('..')  # Add the parent directory to the Python path
import numpy as np
from interaction_eqs import *
from tools.vector_utils import *
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

def show_vector(vector):
    vector.set_visible(True)
    vector.set_label(vector._label)

def hide_vector(vector):
    vector.set_visible(False)
    vector.set_label('')

def toggle_vectors(all_vectors, show_list):
    for vector in all_vectors:
        if vector in show_list:
            show_vector(vector)
        else:
            hide_vector(vector)

fig, ax = plt.subplots()
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')  # Set aspect ratio to be equal

# ==============================================================================
# Define magnitudes
Fa_magnitude = 2
Fb_magnitude = 1
# ==============================================================================

# ==============================================================================
# Initialize items to be animated

# Create agent forces:
Fa = ax.quiver(0, 0, Fa_magnitude, 0, color='red', scale=1, scale_units='xy', angles='xy', label='Fa')
Fb = ax.quiver(0, 0, Fb_magnitude, 0, color='blue', scale=1, scale_units='xy', angles='xy', label='Fb')
Fnet = ax.quiver(0, 0, 0, 0, color='black', scale=1, scale_units='xy', angles='xy', label='Fnet')

# Create bisecting line
bisect_line, = ax.plot([], [], linestyle='dotted', color='black', label='Bisecting Line')

# Create interaction forces
Fi = ax.quiver(0, 0, 0, 0, color='green', scale=1, scale_units='xy', angles='xy', label='Fi')
Fi_greater = ax.quiver(0, 0, 0, 0, color='gray', scale=1, scale_units='xy', angles='xy', label='Fi_greater')

# Create forces without Fi
Fa_minus_Fi = ax.quiver(Fa.X[0], Fa.Y[0], 0, 0, color='lightcoral', scale=1, scale_units='xy', angles='xy', label='Fa - Fi')
Fb_minus_Fi = ax.quiver(Fb.X[0], Fb.Y[0], 0, 0, color='deepskyblue', scale=1, scale_units='xy', angles='xy', label='Fb - Fi')
forces_no_fi_combined = ax.quiver(0, 0, 0, 0, color='purple', scale=1, scale_units='xy', angles='xy', label='(Fa - Fi) + (Fb - Fi)')

# Create orthogonal component of Fa projected onto Fnet
Fa_on_net = ax.quiver(0, 0, 0, 0, color='darkblue', scale=1, scale_units='xy', angles='xy', label='Fa on net')
Fb_on_net = ax.quiver(0, 0, 0, 0, color='darkred', scale=1, scale_units='xy', angles='xy', label='Fb on net')

# Create lines to trace the arrow tip
trace_Fa,          = ax.plot([], [], linestyle=':', color='red', label='Tip Trace Fa')
trace_Fb,          = ax.plot([], [], linestyle=':', color='blue', label='Tip Trace Fb')
trace_Fnet,        = ax.plot([], [], linestyle=':', color='black', label='Tip Trace Fnet')
trace_Fi,          = ax.plot([], [], linestyle=':', color='green', label='Tip Trace Fi')
trace_Fi_greater,  = ax.plot([], [], linestyle=':', color='gray', label='Tip Trace Fi greater')
trace_Fi_minus_Fa, = ax.plot([], [], linestyle=':', color='lightcoral', label='Tip Trace Fi - Fa')
trace_Fi_minus_Fb, = ax.plot([], [], linestyle=':', color='deepskyblue', label='Tip Trace Fi - Fb')
trace_Fa_on_net,   = ax.plot([], [], linestyle=':', color='darkblue', label='Tip Trace Fa on net')
trace_Fb_on_net,   = ax.plot([], [], linestyle=':', color='darkred', label='Tip Trace Fb on net')
# ==============================================================================

# ==============================================================================
# Group items for easy management
all_items = [Fa,      trace_Fa, 
             Fb,      trace_Fb,
             Fnet,    trace_Fnet,
             Fi,      trace_Fi,
             bisect_line,
             Fa_minus_Fi, trace_Fi_minus_Fa,
             Fb_minus_Fi, trace_Fi_minus_Fb,
             forces_no_fi_combined, 
             Fi_greater, trace_Fi_greater,
             Fa_on_net,  trace_Fa_on_net,
             Fb_on_net,  trace_Fb_on_net
            ]

# Items that will plot and appear on the legend
show_items = [Fa, Fb, Fnet, bisect_line, Fa_on_net, Fb_on_net, trace_Fa_on_net, trace_Fb_on_net]
toggle_vectors(all_items, show_items)

# Which items to trace (be sure all show up in the show_items list to appear on the legend):
trace_lines = {Fb_on_net: trace_Fb_on_net, Fa_on_net: trace_Fa_on_net}
# ==============================================================================

def init():
    return all_items

def animate(frame_number):
    # Update Fb angle
    angle = np.radians(frame_number)
    Fb.set_UVC(Fb_magnitude*np.cos(angle), Fb_magnitude*np.sin(angle))

    Fa_vector = np.array([Fa.U[0], Fa.V[0]])
    Fb_vector = np.array([Fb.U[0], Fb.V[0]])

    # Update the net force
    sum_x = Fa_vector[0] + Fb_vector[0]
    sum_y = Fa_vector[1] + Fb_vector[1]
    Fnet.set_UVC(sum_x, sum_y)
    Fnet_vector = np.array([Fnet.U[0], Fnet.V[0]])

    # Update the interaction force using the minimum orthogonal bisection method
    Fi_vector = perpendicular_projection_bisection(Fa_vector, Fb_vector)
    Fi.set_UVC(Fi_vector[0], Fi_vector[1])
    
    # Update the interaction force using the maximum orthogonal bisection method
    Fi_greater_vector = perpendicular_projection_bisection2(Fa_vector, Fb_vector)
    Fi_greater.set_UVC(Fi_greater_vector[0], Fi_greater_vector[1])

    # Update the forces without Fi
    Fa_minus_Fi_vector = Fa_vector - (Fi_vector * -1)
    Fb_minus_Fi_vector = Fb_vector - Fi_vector
    Fa_minus_Fi.set_UVC(Fa_minus_Fi_vector[0], Fa_minus_Fi_vector[1])
    Fb_minus_Fi.set_UVC(Fb_minus_Fi_vector[0], Fb_minus_Fi_vector[1])

    # Update the combination of the forces without Fi
    forces_no_fi_combined_vector = Fa_minus_Fi_vector + Fb_minus_Fi_vector
    forces_no_fi_combined.set_UVC(forces_no_fi_combined_vector[0], forces_no_fi_combined_vector[1])

    # Update the orthogonal component of Fa projected onto Fnet
    Fa_on_net_vector = get_perpendicular_component(Fa_vector, Fnet_vector)
    Fa_on_net.set_UVC(Fa_on_net_vector[0], Fa_on_net_vector[1])
    Fb_on_net_vector = get_perpendicular_component(Fb_vector, Fnet_vector)
    Fb_on_net.set_UVC(Fb_on_net_vector[0], Fb_on_net_vector[1])

    # Update the bisecting line
    bisecting_vector = get_bisector(Fa_vector, Fb_vector)
    bisect_line.set_data([0, bisecting_vector[0]*100], [0, bisecting_vector[1]*100])

    for force, trace_line in trace_lines.items():
        x, y = trace_line.get_data()
        x = np.append(x, force.U)
        y = np.append(y, force.V)
        trace_line.set_data(x, y)

    return all_items

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
plt.legend()
plt.show()
