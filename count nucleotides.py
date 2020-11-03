# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Problem
#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

#Given: A DNA string s of length at most 1000 nt.

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def countNucleotides(DNAstrand):
    """Given a string, DNAstrand, count the respective number of A's, C's, G's, and T's present in the string."""
    Nucleotides = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in DNAstrand:
        Nucleotides[nuc] += 1
    return Nucleotides


DNAStrand = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result = countNucleotides(DNAStrand)

print(' '.join([str(val) for key, val in result.items()]))

#Expected output: 20 12 17 21
