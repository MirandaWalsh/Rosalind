# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:20:48 2020

@author: walsh
"""
#Problem
#A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

#Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

#A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

seq1 = "ATCCAGCT"
seq2 = "GGGCAACT"
seq3 = "ATGGATCT"
seq4 = "AAGCAACC"
seq5 = "TTGGAACT"
seq6 = "ATGCCATT"
seq7 = "ATGGCACT"

sequences = [seq1, seq2, seq3, seq4, seq5, seq6, seq7]
position = 0
length = len(seq1)

A = [0]*length
C = [0]*length
G = [0]*length
T = [0]*length


while (position < length):
    for sequence in sequences:
        base = sequence[position]
        if (base == "A"):
            A[position] = A[position] + 1
        elif (base =="C"):
            C[position] = C[position] + 1
        elif (base =="G"):
            G[position] = G[position] + 1
        elif (base =="T"):
            T[position] = T[position] + 1
    position = position+1


aCount = 0
cCount = 0
gCount = 0
tCount = 0
maxCount = 0    
consensus = ""
position = 0
while(position < length):
    aCount = A[position]
    cCount = C[position]
    gCount = G[position]
    tCount = T[position]
    maxCount = max([aCount,cCount,gCount,tCount])
    
    if (maxCount == aCount):
        consensus = consensus + "A"
    elif (maxCount == cCount):
        consensus = consensus + "C"
    elif (maxCount == gCount):
        consensus = consensus + "G"
    elif (maxCount == tCount):
        consensus = consensus + "T"
    position = position + 1    


print (consensus)
print("A: " + ' '.join(map(str,A)))
print("C: " +' '.join(map(str,C)))
print("G: " +' '.join(map(str,G)))
print("T: " +' '.join(map(str,T)))

#Expected Output:

#ATGCAACT
#A: 5 1 0 0 5 5 0 0
#C: 0 0 1 4 2 0 6 1
#G: 1 1 6 3 0 1 0 0
#T: 1 5 0 0 0 1 1 6
