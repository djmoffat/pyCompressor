''' Written By Dave Moffat 30/10/2020'''
'''Copyright 2020'''

import numpy as np
import math


yL_prev = 0

def gain_computer(sample, threshold=-20, ratio=3, attack=100, release=200, makeupGain=None, kneeWidth=2.5, samplerate=44100):
    global yL_prev
    if makeupGain is None:
        makeupGain = (1*ratio-1) * threshold * 0.5
    
    
    alphaAttack = math.exp(-1/(0.001 * samplerate * attack))
    alphaRelease= math.exp(-1/(0.001 * samplerate * release))
    
    # Level detection- estimate level using peak detector
    if (abs(sample) < 0.000001):
        x_g =-120
    else:
        x_g = 20*math.log10(abs(sample))
    
    # Apply second order interpolation soft knee
    if ((2* abs(x_g-threshold)) <= kneeWidth):
    # Quadratic Interpolation
        # y_g = x_g + (1*ratio -1) * ((x_g-threshold+kneeWidth)*(x_g-threshold+kneeWidth)) / (4*kneeWidth)
    # Linear Interpolation
        y_g = threshold - kneeWidth*0.5 + (x_g-threshold+kneeWidth*0.5)*(1+ratio)*0.5
    elif ((2*(x_g-threshold)) > kneeWidth):
        y_g = threshold + (x_g - threshold) * ratio
    else:
        y_g = x_g
    
    x_l = x_g - y_g
    
    # Ballistics- smoothing of the gain
    if (x_l > yL_prev):
        y_l = alphaAttack * yL_prev + (1 - alphaAttack ) * x_l
    else:
        y_l = alphaRelease * yL_prev + (1 - alphaRelease) * x_l
    
    c = math.pow(10,(makeupGain - y_l)*0.05)
    yL_prev = y_l
    
    return c