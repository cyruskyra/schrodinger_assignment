# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 00:39:34 2017

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
        
print 'f=assoc_laguerre(0,0)'
print 'f(1)'
f=assoc_laguerre(0,0)
ans=f(1)
print ans
print 'f=assoc_laguerre(1,1)'
print 'f(1)'
f=assoc_laguerre(1,1)
ans=f(1)
print ans
print 'f=assoc_laguerre(2,2)'
print 'f(1)'
f=assoc_laguerre(2,2)
ans=f(1)
print ans
print 'f=assoc_laguerre(2,2)'
print 'f(0)'
f=assoc_laguerre(2,2)
ans=f(0)
print ans