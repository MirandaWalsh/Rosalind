# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:20:48 2020

@author: walsh
"""
#create dictionary
#use count method from finding motif to count a, t, c, g, print keys and values
#print max value for each position


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