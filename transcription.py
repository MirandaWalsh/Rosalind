# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:08:08 2020

@author: walsh
"""
#Problem
#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

#Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

#Given: A DNA string t having length at most 1000 nt.

#Return: The transcribed RNA string of t.

def transcribe(DNAstrand):
     """Given a string, DNAstrand, convert every T to U."""
     return DNAstrand.replace("T", "U")


print(transcribe("GATGGAACTTGACTACGTAAATT"))

#Expected output: GAUGGAACUUGACUACGUAAAUU
