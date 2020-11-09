# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 02:02:24 2020

@author: walsh
"""
#Problem
#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


k = 2
m = 2
n = 2

population = k + m + n

prob = (k/population) + (m/population*((k/(population-1)) + (0.75*(m-1)/(population-1) + (0.5*(n/(population-1))))) + (n/population*((k/(population-1)) + (0.5*(m/(population-1))))))                      
print(prob)

#Expected Output: 0.78333
