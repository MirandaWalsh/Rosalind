# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 02:02:24 2020

@author: walsh
"""

k = 2
m = 2
n = 2

population = k + m + n

prob = (k/population) + (m/population*((k/(population-1)) + (0.75*(m-1)/(population-1) + (0.5*(n/(population-1))))) + (n/population*((k/(population-1)) + (0.5*(m/(population-1))))))                      
print(prob)