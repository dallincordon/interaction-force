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
Fi_ab_bi = perpendicular_projection_bisection(Fa,Fb)
Fi_ab_net = perpendicular_projection_net(Fa,Fb)
equivalency = np.array_equal(Fi_ab_bi,Fi_ab_net)

combine = get_magnitude(Fnet + Fi_ab_bi*2)

colors = ['r','b','k','m','c']
vectors = np.array([Fa,Fb,Fnet,Fi_ab_bi,Fi_ab_net])

plot_vectors(vectors, colors)
print(f"|Fa| = {np.linalg.norm(Fa)}")
print(f"|Fb| = {np.linalg.norm(Fb)}")
print(f"|F_net| = {np.linalg.norm(Fnet)}")
print(f"Bisection = Net?: {equivalency}")
print(f"|Fi_ab_bi| = {np.linalg.norm(Fi_ab_bi)}")
print(f"|Fi_ab_net| = {np.linalg.norm(Fi_ab_net)}")
print(f"|F_net + Fi*2| = {combine}")

#==============================================================================

#%% 
## Two agents pull 90 degrees apart with different forces
Fa = polar_to_cartesian(3, np.pi/4)
Fb = polar_to_cartesian(1, 3*np.pi/4)

Fnet = Fa + Fb
Fi_ab_bi = perpendicular_projection_bisection(Fa,Fb)
Fi_ab_net = perpendicular_projection_net(Fa,Fb)
equivalency = np.array_equal(Fi_ab_bi,Fi_ab_net)

combine_bi = get_magnitude(Fnet + Fi_ab_bi*2)
combine_net = get_magnitude(Fnet + Fi_ab_net*2)

colors = ['r','b','k','m','c']
vectors = np.array([Fa,Fb,Fnet,Fi_ab_bi,Fi_ab_net])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"Bisection = Net?: {equivalency}")
print(f"|Fi_ab_bi| = {get_magnitude(Fi_ab_bi)}")
print(f"|Fi_ab_net| = {get_magnitude(Fi_ab_net)}")
print(f"|F_net + Fi_ab_bi*2| = {combine_bi}")
print(f"|F_net + Fi_ab_net*2| = {combine_net}")

#==============================================================================
#%%
# Two agents pull 180 degrees apart with same force
Fa = np.array([3,0])
Fb = polar_to_cartesian(2, np.pi-0.001)

Fnet = Fa + Fb
Fi_ab_bi = perpendicular_projection_bisection(Fa,Fb)
Fi_ab_net = perpendicular_projection_net(Fa,Fb)
equivalency = np.array_equal(Fi_ab_bi,Fi_ab_net)

combine_bi = get_magnitude(Fnet + Fi_ab_bi*2)
combine_net = get_magnitude(Fnet + Fi_ab_net*2)

colors = ['r','b','k','m','c']
vectors = np.array([Fa,Fb,Fnet,Fi_ab_bi,Fi_ab_net])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"Bisection = Net?: {equivalency}")
print(f"|Fi_ab_bi| = {get_magnitude(Fi_ab_bi)}")
print(f"|Fi_ab_net| = {get_magnitude(Fi_ab_net)}")
print(f"|F_net + Fi_ab_bi*2| = {combine_bi}")
print(f"|F_net + Fi_ab_net*2| = {combine_net}")

#==============================================================================
# %%
# Two agents pull together degrees apart with same force
Fa = np.array([2,0])
Fb = np.array([2,0])

Fnet = Fa + Fb
Fi_ab_bi = perpendicular_projection_bisection(Fa,Fb)
Fi_ab_net = perpendicular_projection_net(Fa,Fb)
equivalency = np.array_equal(Fi_ab_bi,Fi_ab_net)

combine_bi = get_magnitude(Fnet + Fi_ab_bi*2)
combine_net = get_magnitude(Fnet + Fi_ab_net*2)

colors = ['r','b','k','m','c']
vectors = np.array([Fa,Fb,Fnet,Fi_ab_bi,Fi_ab_net])

plot_vectors(vectors, colors)
print(f"|Fa| = {get_magnitude(Fa)}")
print(f"|Fb| = {get_magnitude(Fb)}")
print(f"|F_net| = {get_magnitude(Fnet)}")
print(f"Bisection = Net?: {equivalency}")
print(f"|Fi_ab_bi| = {get_magnitude(Fi_ab_bi)}")
print(f"|Fi_ab_net| = {get_magnitude(Fi_ab_net)}")
print(f"|F_net + Fi_ab_bi*2| = {combine_bi}")
print(f"|F_net + Fi_ab_net*2| = {combine_net}")

# %%
