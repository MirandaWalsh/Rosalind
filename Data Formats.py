# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:58:41 2020

@author: walsh
"""

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "walsh_miranda@yahoo.ca"
handle = Entrez.efetch(db="nucleotide", id=["JF927163, NM_001015511, NM_002037, JX472277, NM_002124, JN698988, JX428803, GU292427, JX295575, JX205496"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta")) 
records.sort(key=len)
#print(records)
print(records[0])
