#%% Imports
import sys
sys.path.append('..')  # Add the parent directory to the Python path
import numpy as np
from interaction_eqs import *
from tools.vector_utils import *

#==============================================================================
#%%
## Two agents pull 90 degrees apart with same force
Fa = polar_to_cartesian(1, np.pi/4)
Fb = polar_to_cartesian(1, 3*np.pi/4)

Fnet = Fa + Fb
Fi_ab = perpendicular_projection_bisection(Fa,Fb)

combine = get_magnitude(Fnet + Fi_ab*2)

colors = ['r','b','k','g']
vectors = np.array([Fa,Fb,Fnet,Fi_ab])

plot_vectors(vectors, colors)
print(f"|Fa| = {np.linalg.norm(Fa)}")
print(f"|Fb| = {np.linalg.norm(Fb)}")
print(f"|F_net| = {np.linalg.norm(Fnet)}")
print(f"|Fi_ab| = {np.linalg.norm(Fi_ab)}")
print(f"|F_net + Fi*2| = {combine}")

#==============================================================================

#%% 
## Two agents pull 90 degrees apart with different forces
## (Increase Fa)
Fa = polar_to_cartesian(2, np.pi/4)
Fb = polar_to_cartesian(1, 3*np.pi/4)

Fnet = Fa + Fb
Fi_ab = perpendicular_projection_bisection(Fa,Fb)

combine_bi = get_magnitude(Fnet + Fi_ab*2)

colors = ['r','b','k','g']
vectors = np.array([Fa,Fb,Fnet,Fi_ab])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"|Fi_ab| = {get_magnitude(Fi_ab)}")
print(f"|F_net + Fi_ab*2| = {combine_bi}")

#%% 
## Two agents pull 90 degrees apart with different forces
## (Decrease Fb)
Fa = polar_to_cartesian(2, np.pi/4)
Fb = polar_to_cartesian(0.5, 3*np.pi/4)

Fnet = Fa + Fb
Fi_ab = perpendicular_projection_bisection(Fa,Fb)

combine_bi = get_magnitude(Fnet + Fi_ab*2)

colors = ['r','b','k','g']
vectors = np.array([Fa,Fb,Fnet,Fi_ab])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"|Fi_ab| = {get_magnitude(Fi_ab)}")
print(f"|F_net + Fi_ab*2| = {combine_bi}")

#==============================================================================
#%%
# Two agents pull 180 degrees apart with same force
Fa = np.array([3,0])
Fb = polar_to_cartesian(2, np.pi-0.001)

Fnet = Fa + Fb
Fi_ab = perpendicular_projection_bisection(Fa,Fb)

combine_bi = get_magnitude(Fnet + Fi_ab*2)

colors = ['r','b','k','g']
vectors = np.array([Fa,Fb,Fnet,Fi_ab])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"|Fi_ab| = {get_magnitude(Fi_ab)}")
print(f"|F_net + Fi_ab*2| = {combine_bi}")

#==============================================================================
# %%
# Two agents pull together degrees apart with same force
Fa = np.array([2,0])
Fb = np.array([2,0])

Fnet = Fa + Fb
Fi_ab = perpendicular_projection_bisection(Fa,Fb)

combine_bi = get_magnitude(Fnet + Fi_ab*2)

colors = ['r','b','k','g']
vectors = np.array([Fa,Fb,Fnet,Fi_ab])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"|Fi_ab| = {get_magnitude(Fi_ab)}")
print(f"|F_net + Fi_ab*2| = {combine_bi}")

# %%
# Two agents pull 90 degrees apart with different force
Fa = np.array([3,0])
Fb = np.array([0,2])

Fnet = Fa + Fb
Fi_ba = perpendicular_projection_bisection(Fa,Fb)
Fi_ab = perpendicular_projection_bisection2(Fa,Fb)

combine_bi = get_magnitude(Fnet) + get_magnitude(Fi_ba)*2

colors = ['r','b','k','g']
vectors = np.array([Fa,Fb,Fnet,Fi_ba])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"|Fa|+|Fb|-|Fnet| = {get_magnitude(Fa)+get_magnitude(Fb)-get_magnitude(Fnet)}")
print(f"|Fi_ba| = {get_magnitude(Fi_ba)}")
print(f"|Fi_ab| = {get_magnitude(Fi_ab)}")
print(f"|Fi_ab+Fi_ba| = {get_magnitude(Fi_ab+Fi_ba)}")
print(f"|F_net| + |Fi_ab|*2 = {combine_bi}")

# %%
