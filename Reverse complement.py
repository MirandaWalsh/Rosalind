# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:23:11 2020

@author: walsh
"""
#Problem
#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

#Given: A DNA string s of length at most 1000 bp.

#Return: The reverse complement sc of s.

def reverseComplement(DNAstrand):
    """Given a string, DNAstrand, reverse the string and convert every A to T, T to A, C to G, and G to C."""
    x = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return''.join([x[nuc] for nuc in DNAstrand])[::-1]


print(reverseComplement("AAAACCCGGT"))

#Expected output: ACCGGGTTTT
