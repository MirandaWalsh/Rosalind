# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:05:56 2020

@author: walsh
"""
#Problem
#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

#Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

from Bio.Seq import Seq


DNAstrand = ("ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG")


splice_DNAstrand = (DNAstrand.replace("ATCGGTCGAA", ""))
splice_DNAstrand2 = Seq(splice_DNAstrand.replace("ATCGGTCGAGCGTGT", ""))

Protein = splice_DNAstrand2.translate()
print(Protein)

#Expected Output:  MVYIADKQHVASREAYGHMFKVCA
