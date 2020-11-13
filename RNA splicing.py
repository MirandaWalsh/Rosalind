# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:05:56 2020

@author: walsh
"""

from Bio.Seq import Seq


DNAstrand = ("ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG")


splice_DNAstrand = (DNAstrand.replace("ATCGGTCGAA", ""))
splice_DNAstrand2 = Seq(splice_DNAstrand.replace("ATCGGTCGAGCGTGT", ""))

Protein = splice_DNAstrand2.translate()
print(Protein)
