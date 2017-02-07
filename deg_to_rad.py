# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 03:25:27 2017

@author: Kira
"""

import math

def deg_to_rad(deg):
    rad = deg * (math.pi / 180)
    return round(rad,5)

def rad_to_deg(rad):
    deg = (rad / math.pi) * 180
    return round(deg,5)

print 'deg_to_rad(90)'
ans=deg_to_rad(90)
print ans
print 'deg_to_rad(180)'
ans=deg_to_rad(180)
print ans
print 'deg_to_rad(270)'
ans=deg_to_rad(270)
print ans
print 'rad_to_deg(3.14)'
ans=rad_to_deg (3.14)
print ans
print 'rad_to_deg(3.14/2.0)'
ans=rad_to_deg (3.14/2.0)
print ans
print 'rad_to_deg(3.14*3/4)'
ans=rad_to_deg (3.14*3/4)
print ans