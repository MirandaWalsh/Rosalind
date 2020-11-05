# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:40:42 2020

@author: walsh
"""

from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('B5ZC00') 
record = SwissProt.read(handle)
list = record.keywords
print(list)

