# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:49:19 2020

@author: walsh
"""
#Problem

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

from Bio.SeqUtils import GC






a = GC("CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG")
b = GC("CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC")
c = GC("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")


seqDict = {a: 'Rosalind_6404', b: 'Rosalind_5959', c: 'Rosalind_0808'}


list = [a, b, c]
x = (max(list))
print(x)
print(seqDict.get(x))


#Expected Output: 
#Rosalind_0808
#60.919540
