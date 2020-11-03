# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:54:35 2020

@author: walsh
"""
#Problem
#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

#Return: The Hamming distance dH(s,t).


def hammingDist(seq1, seq2):
    """Given two strings of equal length, seq1 and seq2, count the number of positions where the two strings have values that are not identical."""
    pointMut = 0
    x = len(seq1)
    for nuc in range (x):
        if seq1[nuc] != seq2[nuc]:
            pointMut += 1
    return(pointMut)
    
        
        
        
        
        
        
        
        
result = hammingDist("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
print(result)

#Expected output: 7
    
