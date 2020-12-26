# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:51:07 2020

@author: walsh
"""





file = open("C:/Users/walsh/downloads//rosalind_orf.txt", 'r') 
record = file.read().replace('\n', '')
file.close()  

Codon_Table = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def reverseComplement(DNAstrand):
    """Given a string, DNAstrand, reverse the string and convert every A to T, T to A, C to G, and G to C."""
    x = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return''.join([x[nuc] for nuc in DNAstrand])[::-1]
    
ProteinSet = set()
for sequence in [record, reverseComplement(record)]:
    for x in range((len(sequence))-2):
        if sequence[x:x+3] == "ATG":
            y = x
            protein = ""
            while (y+3) in range((len(sequence))-1):
                if Codon_Table[sequence[y:y+3]] == "Stop":
                    ProteinSet.add(protein)
                    break
                else:
                        protein += Codon_Table[sequence[y:y+3]]
                y += 3
print("\n".join(ProteinSet))
            
