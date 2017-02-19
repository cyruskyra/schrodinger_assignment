# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:53:20 2017

@author: Wang Gan
"""
import numpy as np

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

print 'f=assoc_legendre (0,0)'
print 'f(1)'
f=assoc_legendre (0,0)
ans=f(1)
print ans
print 'f=assoc_legendre (1,1)'
print 'f(1)'
f=assoc_legendre (1,1)
ans=f(1)
print ans
print 'f=assoc_legendre (2,3)'
print 'f(1)'
f=assoc_legendre (2,3)
ans=f(1)
print ans
print 'f=assoc_legendre (2,3)'
print 'f(0)'
f=assoc_legendre (2,3)
ans=f(0)
print ans