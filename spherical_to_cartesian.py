# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 03:39:13 2017

@author: Kira
"""

import numpy as np

def spherical_to_cartesian(r,theta,phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return (round(x,5),round(y,5),round(z,5))

def cartesian_to_spherical(x,y,z):
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    if z != 0:
        theta = np.arctan((np.sqrt(x ** 2 + y ** 2) / z))
    elif x != 0  or y != 0:
        theta = np.arccos(z / (np.sqrt(x ** 2 + y ** 2 + z ** 2)))
    else:
        theta = 0
    if x != 0:
        phi = np.arctan(y / x)
    elif y != 0:
        phi = np.arccos(x / (np.sqrt(x ** 2 + y ** 2)))
    else:
        phi = 0
    if y < 0:
        phi = phi * -1
    if z < 0:
        theta = theta * -1
    return (round(r,5),round(theta,5),round(phi,5))


ans=spherical_to_cartesian(3,0,np.pi)
print ans

ans=spherical_to_cartesian(3,np.pi/2.0,np.pi/2.0)
print ans

ans=spherical_to_cartesian (3,np.pi ,0)
print ans

ans=cartesian_to_spherical(3,0,0)
print ans

ans=cartesian_to_spherical(0,3,0)
print ans

ans=cartesian_to_spherical(0,0,3)
print ans

ans=cartesian_to_spherical(0,-3,0)
print ans