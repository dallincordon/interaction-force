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
# Fc = ax.quiver(0, 0, 0, 0, color='purple', scale=1, scale_units='xy', angles='xy', label='Fc', linestyle='dotted')
Fnet = ax.quiver(0, 0, 0, 0, color='black', scale=1, scale_units='xy', angles='xy', label='Fnet')

# Create bisecting line
bisect_line, = ax.plot([], [], linestyle='dotted', color='black', label='Bisecting Line')

# Create interaction forces
Fi_bisection = ax.quiver(0, 0, 0, 0, color='green', scale=1, scale_units='xy', angles='xy', label='Fi')
Fi_bisection_greater = ax.quiver(0, 0, 0, 0, color='gray', scale=1, scale_units='xy', angles='xy', label='Fi_greater')
Fi_counteract = ax.quiver(0, 0, 0, 0, color='green', scale=1, scale_units='xy', angles='xy', label='Fi_counteract')

# Create forces without Fi (bisection)
Fa_minus_Fi_bisection = ax.quiver(Fa.X[0], Fa.Y[0], 0, 0, color='lightcoral', scale=1, scale_units='xy', angles='xy', label='Fa - Fi (bisection)')
Fb_minus_Fi_bisection = ax.quiver(Fb.X[0], Fb.Y[0], 0, 0, color='deepskyblue', scale=1, scale_units='xy', angles='xy', label='Fb - Fi (bisection)')
forces_no_fi_combined = ax.quiver(0, 0, 0, 0, color='purple', scale=1, scale_units='xy', angles='xy', label='(Fa - Fi) + (Fb - Fi)')

# Create forces without Fi (counteract)
Fa_minus_Fi_counteract = ax.quiver(0, 0, 0, 0, color='lightcoral', scale=1, scale_units='xy', angles='xy', label='Fa - Fi (counteract)')
Fb_minus_Fi_counteract = ax.quiver(0, 0, 0, 0, color='deepskyblue', scale=1, scale_units='xy', angles='xy', label='Fb - Fi (counteract)')

# Create orthogonal component of Fa projected onto Fnet
Fa_on_net_ortho     = ax.quiver(0, 0, 0, 0, ec='red', fc='none', linewidth=1, scale=1, scale_units='xy', angles='xy', label='⊥ of Fa on net')
Fb_on_net_ortho     = ax.quiver(0, 0, 0, 0, ec='blue', fc='none', linewidth=1, scale=1, scale_units='xy', angles='xy', label='⊥ of Fb on net')
Fa_on_net_parallel  = ax.quiver(0, 0, 0, 0, ec='red', fc='none', linewidth=1, scale=1, scale_units='xy', angles='xy', label='∥ of Fa on net', linestyle='dashed')
Fb_on_net_parallel  = ax.quiver(0, 0, 0, 0, ec='blue', fc='none', linewidth=1, scale=1, scale_units='xy', angles='xy', label='∥ of Fb on net', linestyle='dashed')

# Create lines to trace the arrow tip
trace_Fa,          = ax.plot([], [], linestyle=':', color='red',            label='Tip Trace Fa')
trace_Fb,          = ax.plot([], [], linestyle=':', color='blue',           label='Tip Trace Fb')
trace_Fnet,        = ax.plot([], [], linestyle=':', color='black',          label='Tip Trace Fnet')
trace_Fi_bisection,          = ax.plot([], [], linestyle=':', color='green',label='Tip Trace Fi')
trace_Fi_bisection_greater,  = ax.plot([], [], linestyle=':', color='gray', label='Tip Trace Fi greater')
trace_Fi_counteract,         = ax.plot([], [], linestyle=':', color='green',label='Tip Trace Fi counteract')
trace_Fa_minus_Fi_bisection, = ax.plot([], [], linestyle=':', color='lightcoral',     label='Tip Trace Fa - Fi (bisection)')
trace_Fb_minus_Fi_bisection, = ax.plot([], [], linestyle=':', color='deepskyblue',    label='Tip Trace Fb - Fi (bisection)')
trace_Fa_minus_Fi_counteract,= ax.plot([], [], linestyle=':', color='lightcoral',     label='Tip Trace Fa - Fi (counteract)')
trace_Fb_minus_Fi_counteract,= ax.plot([], [], linestyle=':', color='deepskyblue',    label='Tip Trace Fb - Fi (counteract)')
trace_Fa_on_net_ortho,   = ax.plot([], [], linestyle=':', color='darkred',  label='⊥ of Fa on net traced')
trace_Fb_on_net_ortho,   = ax.plot([], [], linestyle=':', color='darkblue', label='⊥ of Fb on net traced')
trace_Fa_on_net_parallel, = ax.plot([], [], linestyle=':', color='darkred', label='Fa - Fa_on_net_ortho traced')
trace_Fb_on_net_parallel, = ax.plot([], [], linestyle=':', color='darkblue',label='Fb - Fb_on_net_ortho traced')
# ==============================================================================

## MAIN EDITS GO HERE:
# ==============================================================================
# Group items for easy management
all_items = [Fa,      trace_Fa, 
             Fb,      trace_Fb,
             Fnet,    trace_Fnet,
             Fi_bisection,  trace_Fi_bisection,
             Fi_counteract, trace_Fi_counteract,
             bisect_line,
             Fa_minus_Fi_counteract, trace_Fa_minus_Fi_counteract,
             Fb_minus_Fi_counteract, trace_Fb_minus_Fi_counteract,
             Fa_minus_Fi_bisection, trace_Fa_minus_Fi_bisection,
             Fb_minus_Fi_bisection, trace_Fb_minus_Fi_bisection,
             forces_no_fi_combined, 
             Fi_bisection_greater, trace_Fi_bisection_greater,
             Fa_on_net_ortho,   trace_Fa_on_net_ortho,
             Fb_on_net_ortho,   trace_Fb_on_net_ortho,
             Fa_on_net_parallel, trace_Fa_on_net_parallel,
             Fb_on_net_parallel, trace_Fb_on_net_parallel
            ]

# Items that will plot and appear on the legend
show_items = [Fa, Fb, Fnet, Fi_counteract, trace_Fi_counteract]
toggle_vectors(all_items, show_items)

# Which items to trace (be sure all show up in the show_items list to appear on the legend):
trace_lines = {Fi_counteract: trace_Fi_counteract}#{Fnet: trace_Fnet}#{Fb_on_net_ortho: trace_Fb_on_net_ortho, Fa_on_net_ortho: trace_Fa_on_net_ortho}
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

    # Update the interaction force using the counteracting method
    Fi_counteract_vector = counteract_net(Fa_vector, Fb_vector)
    Fi_counteract.set_UVC(Fi_counteract_vector[0], Fi_counteract_vector[1])

    # Update the forces without Fi counteract
    Fa_minus_Fi_counteract_vector = Fa_vector - (Fi_counteract_vector * -1)
    Fb_minus_Fi_counteract_vector = Fb_vector - Fi_counteract_vector
    Fa_minus_Fi_counteract.set_UVC(Fa_minus_Fi_counteract_vector[0], Fa_minus_Fi_counteract_vector[1])
    Fb_minus_Fi_counteract.set_UVC(Fb_minus_Fi_counteract_vector[0], Fb_minus_Fi_counteract_vector[1])

    # Update the interaction force using the minimum orthogonal bisection method
    Fi_bisection_vector = perpendicular_projection_bisection(Fa_vector, Fb_vector)
    Fi_bisection.set_UVC(Fi_bisection_vector[0], Fi_bisection_vector[1])
    
    # Update the interaction force using the maximum orthogonal bisection method
    Fi_bisection_greater_vector = perpendicular_projection_bisection2(Fa_vector, Fb_vector)
    Fi_bisection_greater.set_UVC(Fi_bisection_greater_vector[0], Fi_bisection_greater_vector[1])

    # Update the forces without Fi bisection
    Fa_minus_Fi_bisection_vector = Fa_vector - (Fi_bisection_vector * -1)
    Fb_minus_Fi_bisection_vector = Fb_vector - Fi_bisection_vector
    Fa_minus_Fi_bisection.set_UVC(Fa_minus_Fi_bisection_vector[0], Fa_minus_Fi_bisection_vector[1])
    Fb_minus_Fi_bisection.set_UVC(Fb_minus_Fi_bisection_vector[0], Fb_minus_Fi_bisection_vector[1])

    # Update the combination of the forces without Fi bisection
    forces_no_fi_combined_vector = Fa_minus_Fi_bisection_vector + Fb_minus_Fi_bisection_vector
    forces_no_fi_combined.set_UVC(forces_no_fi_combined_vector[0], forces_no_fi_combined_vector[1])

    # Update the orthogonal component of Fa projected onto Fnet
    centered = True
    Fa_on_net_ortho_vector = get_perpendicular_component(Fa_vector, Fnet_vector)
    Fb_on_net_ortho_vector = get_perpendicular_component(Fb_vector, Fnet_vector)
    Fa_on_net_parallel.set_UVC(Fa_vector[0] - Fa_on_net_ortho_vector[0], Fa_vector[1] - Fa_on_net_ortho_vector[1])
    Fb_on_net_parallel.set_UVC(Fb_vector[0] - Fb_on_net_ortho_vector[0], Fb_vector[1] - Fb_on_net_ortho_vector[1])
    if centered:
        Fa_on_net_ortho.set_UVC(Fa_on_net_ortho_vector[0], Fa_on_net_ortho_vector[1])
        Fb_on_net_ortho.set_UVC(Fb_on_net_ortho_vector[0], Fb_on_net_ortho_vector[1])
    else:
        Fa_on_net_ortho_base = get_parallel_component(Fa_vector, Fnet_vector)
        Fa_on_net_ortho.set_UVC(Fa_on_net_ortho_vector[0], Fa_on_net_ortho_vector[1])
        Fa_on_net_ortho.set_offsets([Fa_on_net_ortho_base[0], Fa_on_net_ortho_base[1]])

        Fb_on_net_ortho_base = get_parallel_component(Fb_vector, Fnet_vector)
        Fb_on_net_ortho.set_UVC(Fb_on_net_ortho_vector[0], Fb_on_net_ortho_vector[1])
        Fb_on_net_ortho.set_offsets([Fb_on_net_ortho_base[0], Fb_on_net_ortho_base[1]])

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
plt.legend(fontsize='x-small', loc='upper right')

# # uncomment below to turn the animation into a gif (takes a while to run):
# path = '/Users/cordond/Desktop/counteract_trace.gif'
# anim.save(path, writer='imagemagick', fps=30)

plt.show()
