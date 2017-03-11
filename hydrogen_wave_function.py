#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:13:04 2017

@author: hoonqt
"""
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

def hydrogen_wave_func(n,l,m,roa,nx,ny,nz):
    def density(roa,theta,phi):
        r = roa*a
        nonsquare = angular_wave_func(m,l,theta,phi)*radial_wave_func(n,l,r)
        squared = np.absolute(nonsquare)**2
        return np.round(squared,5)
    vec_density = np.vectorize(density)
    vec_cart = np.vectorize(cartesian_to_spherical)
    x = []
    x.append(np.linspace(-roa, roa, nx))
    y = []
    y.append(np.linspace(-roa,roa,ny))
    z = []
    z.append(np.linspace(-roa,roa,nz))
    xx, yy, zz = np.meshgrid(x,y,z)
    rr, tt, pp = vec_cart(xx,yy,zz)
    mag = vec_density(rr, tt, pp)
    xx, yy, zz = np.round((xx,yy,zz), 5)
    return (xx, yy, zz, mag)




    
        