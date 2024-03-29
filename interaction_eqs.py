#!/usr/bin/env python
import sys
sys.path.append('/Users/cordond/tools')
import numpy as np
from tools.vector_utils import *

# return the minimum of two opposing forces
def literature_def(Fa,Fb):
    '''
    Used by:
    Issues:
        - only accounts for 1D situations (doesn't account for partial opposition)
        - doesn't account for more than two agents
    '''
    if np.sign(Fa) != np.sign(Fb):
        Fi = min(abs(Fa),abs(Fb))
    else:
        Fi = 0
    return Fi

def minFsinTheta(Fa,Fb):
    '''
    Proposed by us as a proper mapping between zero (forces aligned) and the minimum of the two forces (forces opposing)
    Issues:
        - gives a correct looking magnitude but not the correct direction (simply scales the smaller force by sin(theta/2))
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

def perpendicular_projection_bisection2(Fa,Fb):
    '''
    Returns the perpendicular projection of the larger force onto the bisector of the two vectors
        (similar to min(Fa,Fb)*sin(theta/2))
    '''
    bisecting_vector = get_bisector(Fa,Fb)
    Fa_magnitude = get_magnitude(Fa)
    Fb_magnitude = get_magnitude(Fb)

    # Find the bigger vector
    if Fa_magnitude < Fb_magnitude:
        Fi = get_perpendicular_component(Fb,bisecting_vector)
    else:
        Fi = get_perpendicular_component(Fa,bisecting_vector)
    return Fi

def perpendicular_projection_net(Fa,Fb):
    '''
    Returns the perpendicular projection of the smaller force onto the net force
    Issues:
        - when Fa and Fb are equal and opposite, Fi = 0
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

def counteract_net(Fa,Fb):
    F_net = Fa + Fb
    if get_magnitude(Fa) < get_magnitude(Fb):
        F_min = Fa
    else:
        F_min = Fb
    theta = angle_between(F_min, F_net)
    if theta > np.pi/2:
        Fi = F_min
    else:
        Fi = get_perpendicular_component(F_min,F_net)
    return Fi


def literature_def_alpha(Fa,Fb,Fg,alpha):
    '''
    Referenced by Noohi et al.
    Issues:
        - doesn't account for more than two agents
        - assumes some measure of how much each agent contributes to the interaction force (alpha)
    '''
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
    Used by Spencer
    Issues:
        - doesn't account for more than two agents
        - doesn't account for partial opposition
        - adding gravity causes some weird behaviors (specify)
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
    '''
    Issues:
        - doesn't account for more than two agents
        - doesn't account for partial opposition
    '''
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
    '''
    Issues:
        - doesn't account for more than two agents
        - doesn't account for partial opposition
    '''
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
