# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:36:48 2017

@author: Wang Gan
"""
import scipy.constants as c
import numpy as np
def fact(n):
    if n ==0:
        return 1
    else:
        return n*fact(n-1)
def p00(theta):
    return 1
def p01(theta):
    return np.cos(theta)
def p11(theta):
    return np.sin(theta)
def p02(theta):
    return 3/2.0*(np.cos(theta))**2-1/2.0
def p12(theta):
    return 3*np.cos(theta)*np.sin(theta)
def p22(theta):
    return 3*(np.sin(theta))**2
def p03(theta):
    return 1/2.0*(5*(np.cos(theta))**3-3*np.cos(theta))
def p13(theta):
    return np.sin(theta)*0.5*(15*(np.cos(theta)**2)-3)
def p23(theta):
    return 15*np.cos(theta)*np.sin(theta)**2
def p33(theta):
    return 15*np.sin(theta)**3
def assoc_legendre(m,l):
    if l == 0:
        return p00
    elif l == 1:
        if np.abs(m)==0:
            return p01
        else:
            return p11
    elif l == 2:
        if np.abs(m)==0:
            return p02
        elif np.abs(m)==1:
            return p12
        else:
            return p22
    elif l == 3:
        if np.abs(m)==0:
            return p03
        elif np.abs(m)==1:
            return p13
        elif np.abs(m)==2:
            return p23
        else:
            return p33

def angular_wave_func(m,l,theta,phi):
    pfunc=assoc_legendre(m,l)
    if m>0:
        return np.round((-1)**m*np.sqrt((2*l+1)*fact(l-np.abs(m))/(4*c.pi*fact((l+np.abs(m)))))*(np.cos(m*phi)+np.sin(m*phi)*1j)*pfunc(theta),5)
    else:
        return np.round(np.sqrt((2*l+1)*fact(l-np.abs(m))/(4*c.pi*fact((l+np.abs(m)))))*(np.cos(m*phi)+np.sin(m*phi)*1j)*pfunc(theta),5)

print 'angular_wave_func (0,0,0,0)'
ans= angular_wave_func (0,0,0,0)
print ans
print 'angular_wave_func (0,1,c.pi ,0)'
ans= angular_wave_func (0,1,c.pi ,0)
print ans
print 'angular_wave_func (1,1,c.pi/2,c.pi)'
ans= angular_wave_func (1,1,c.pi/2,c.pi)
print ans
print 'angular_wave_func (0,2,c.pi ,0)'
ans= angular_wave_func (0,2,c.pi ,0)
print ans