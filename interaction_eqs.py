#!/usr/bin/env python
import sys
sys.path.append('/Users/cordond/tools')
import numpy as np
import itertools
import pandas as pd
from vector_utils import *

# return the minimum of two opposing forces
def literature_def(Fa,Fb,Fg):
    '''
    Used by:
    '''
    if np.sign(Fa) != np.sign(Fb):
        Fi = min(abs(Fa),abs(Fb))
    else:
        Fi = 0
    return Fi

def minFsinTheta(Fa,Fb):
    '''
    Defined by us
    '''
    # get the angle between the two force vectors:
    theta = angle_between(Fa,Fb)
    Fa_magnitude = np.linalg.norm(Fa)
    Fb_magnitude = np.linalg.norm(Fb)
    if min(Fa_magnitude, Fb_magnitude) == Fa_magnitude:
        Fi = Fa*np.sin(theta/2)
    else:
        Fi = Fb*np.sin(theta/2)
    # Fi = min(Fa_magnitude, Fb_magnitude)*np.sin(theta/2)
    return Fi

def perpendicular_projection_bisection(Fa,Fb):
    '''
    Returns the perpendicular projection of the smaller force onto the bisector of the two vectors
        (similar to min(Fa,Fb)*sin(theta/2))
    '''
    bisecting_vector = get_bisector(Fa,Fb)
    Fa_magnitude = get_magnitude(Fa)
    Fb_magnitude = get_magnitude(Fb)

    # Find the smaller vector
    if Fa_magnitude < Fb_magnitude:
        Fi = get_perpendicular_component(Fa,bisecting_vector)
    else:
        Fi = get_perpendicular_component(Fb,bisecting_vector)
    return Fi

def perpendicular_projection_net(Fa,Fb):
    '''
    Returns the perpendicular projection of the smaller force onto the net force
    '''
    F_net = Fa + Fb
    Fa_magnitude = get_magnitude(Fa)
    Fb_magnitude = get_magnitude(Fb)

    # Find the smaller vector
    if Fa_magnitude < Fb_magnitude:
        Fi = get_perpendicular_component(Fa,F_net)
    else:
        Fi = get_perpendicular_component(Fb,F_net)
    return Fi



def literature_def_alpha(Fa,Fb,Fg,alpha):
    Fi = (1-alpha)*Fa + alpha*Fb
    return Fi

def Fa_is_leader(Fa,Fb,Fg):
    alpha = 1
    Fi = np.abs(literature_def_alpha(Fa,Fb,Fg,alpha))
    return Fi

def Fb_is_leader(Fa,Fb,Fg):
    alpha = 0
    Fi = np.abs(literature_def_alpha(Fa,Fb,Fg,alpha))
    return Fi

# return the minimum of two opposing forces after removing gravity from it's opposing force
def spencers(Fa,Fb,Fg):
    '''
    Used by:
    '''
    if np.sign(Fa) != np.sign(Fb):
        if np.sign(Fa) != np.sign(Fg):
            Fa = Fa + Fg
        else:
             Fb = Fb + Fg
             
    if np.sign(Fa) != np.sign(Fb):
        Fi = min(abs(Fa),abs(Fb))
    else:
        Fi = 0
    return Fi

# return the minimum of two opposing forces after removing gravity from it's matching force
def inv_spencers(Fa,Fb,Fg):
    if np.sign(Fa) != np.sign(Fb):
        if np.sign(Fa) == np.sign(Fg):
            Fa = Fa + Fg
        else:
             Fb = Fb + Fg
        Fi = min(abs(Fa),abs(Fb))
    else:
        Fi = 0
    return Fi

# return the minimum of two opposing forces after adding gravity to the leaders force
def leader_follower(Fa,Fb,Fg):
    Fa = Fa + Fg
    
    if np.sign(Fa) != np.sign(Fb):
        Fi = min(abs(Fa),abs(Fb))
    else:
        Fi = 0
    return Fi


# return the minimum of two opposing forces after adding gravity to both participants
def leader_leader(Fa,Fb,Fg):
    Fa = Fa + Fg
    Fb = Fb + Fg
    
    if np.sign(Fa) != np.sign(Fb):
        Fi = min(abs(Fa),abs(Fb))
    else:
        Fi = 0
    return Fi

# return the minimum between your force and all forces opposing you
def isolation(Fa,Fb,Fg):
    '''
    Used by:

    Failures: 
        when Fg=0 and |Fb|<|Fa|
    '''
    acc = Fa+Fb+Fg # assuming a mass of 1
    
    if np.sign(Fa) != np.sign(acc):
        ex = acc - Fa
        Fi = min(abs(Fa),abs(ex))
    else:
        Fi = 0
    return Fi
def isolation2(Fa,Fb,Fg):
    '''
    Used by:

    Failures: 
        when Fg=0 and |Fb|<|Fa|
    '''
    acc = Fa+Fb+Fg # assuming a mass of 1
    
    if np.sign(Fa) != np.sign(acc):
        ex = acc - Fa
        Fi = min(abs(Fa),abs(ex))
    elif np.sign(Fb) != np.sign(acc):
        ex = acc - Fb
        Fi = min(abs(Fb),abs(ex))
    else:
        Fi = 0
    return Fi

# return the minimum between your force and all forces opposing you with accounting for mass
def isolation_mass(Fa,Fb,Fg,m):
    acc_m = Fa+Fb+Fg # assuming a mass of 1
    acc_p = Fa/m
    if np.sign(acc_m) != np.sign(acc_p):
        ex = acc_m - acc_p
        Fi = min(abs(Fa),abs(ex))
    else:
        Fi = 0
    return Fi

# return the minimum between your force and all forces opposing you with accounting for mass
def isolation_mass(Fa,Fb,Fg,m):
    acc_m = Fa+Fb+Fg # assuming a mass of 1
    acc_p = Fa/m
    if np.sign(acc_m) != np.sign(acc_p):
        ex = acc_m - acc_p
        Fi = min(abs(Fa),abs(ex))
    else:
        Fi = 0
    return Fi

# return the active and passive components of Fa and Fb 
def multiple(Fa,Fb,Fg,ma):
    pass

def vis_F(F):
    if np.sign(F) > 0:
        vis ='-'* abs(F) + '>'
    else:
        vis = '<' + '-'* abs(F)
    if F == 0:
        vis = 'x'
    return vis
