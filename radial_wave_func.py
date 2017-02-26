# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 00:03:15 2017

@author: Kyra
"""

def l00(x):
    return 1
def l10(x):
    return 1
def l20(x):
    return 2
def l30(x):
    return 6
def l01(x):
    return 1 - x
def l11(x):
    return 4 - 2*x
def l21(x):
    return -6*x + 18
def l31(x):
    return 96 - 24*x
def l02(x):
    return x**2 - 4*x + 2
def l12(x):
    return 3*x**2 - 18*x + 18
def l22(x):
    return 12*x**2 - 96*x + 144
def l32(x):
    return 60*x**2 - 600*x + 1200
def l03(x):
    return -1*x**3 + 9*x**2 - 18*x + 6
def l13(x):
    return -4*x**3 + 48*x**2 - 144*x + 96
def l23(x):
    return -20*x**3 + 300*x**2 - 1200*x + 1200
def l33(x):
    return -120*x**3 + 2160*x**2 - 10800*x + 14400



def assoc_laguerre(p,qmp):
    if p==0:
        if qmp==0:
            return l00
        elif qmp==1:
            return l01
        elif qmp==2:
            return l02
        elif qmp==3:
            return l03
    elif p==1:
        if qmp==0:
            return l10
        if qmp==1:
            return l11
        if qmp==2:
            return l12
        if qmp==3:
            return l13
    elif p==2:
        if qmp==0:
            return l20
        if qmp==1:
            return l21
        if qmp==2:
            return l22
        if qmp==3:
            return l23
    elif p==3:
        if qmp==0:
            return l30
        if qmp==1:
            return l31
        if qmp==2:
            return l32
        if qmp==3:
            return l33

import scipy.constants as c
import numpy as np 
a=c.physical_constants['Bohr radius'][0]

def radial_wave_func(n,l,r):
    p = 2.0*l + 1.0
    qmp = n - l - 1.0
    L = assoc_laguerre(p,qmp)
    Lx = np.float64(L((2.0*r)/(n*a)))
    fac1 = np.float64(np.math.factorial(n - l - 1.0))
    fac2 = np.float64(np.math.factorial(n + l))
    exp = np.float64(np.exp(-(r/(n*a))))
    sqrt = np.sqrt(((2.0 / (n * a))**3.0) * (fac1/((2.0*n)*((fac2)**3.0))))
    radialSolution = (sqrt * (exp) * ((2.0 * r) / (n * a))**l * (Lx)) / a**(- 3.0/2.0)
    return np.round(radialSolution,5)
