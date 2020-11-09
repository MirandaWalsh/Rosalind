# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:49:50 2020

@author: walsh
"""


DNAstrand = "GATATATGCATATACTT"
substring = "ATAT"

Motifs = []
position = 0
count = 0

while (count < len(DNAstrand)):
      position = DNAstrand.find(substring, count)
      if(position > 0):
          count = position + 1
          Motifs.append(position+1)
      else:
          count = count + 1

print(Motifs)


