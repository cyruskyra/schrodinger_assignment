# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 02:40:13 2017

@author: Kira
"""

import scipy.constants as c

def energy_n(n):
    ans = - c.value("Rydberg constant times hc in eV") / n ** 2
    return round(ans,5)

print 'n = 1'
ans= energy_n(1)
print ans
print 'n = 2'
ans= energy_n(2)
print ans
print 'n = 3'
ans= energy_n(3)
print ans