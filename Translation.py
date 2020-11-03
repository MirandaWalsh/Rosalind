# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:20:48 2020

@author: walsh
"""
from Bio.Seq import Seq


DNAstrand = Seq("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
Protein = DNAstrand.translate()
print(Protein)