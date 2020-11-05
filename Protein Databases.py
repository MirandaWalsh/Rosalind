# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:40:42 2020

@author: walsh
"""
#Problem
#The UniProt Knowledgebase can be found here.

#You can see a complete description of a protein by entering its UniProt access ID into the site's query field. Equivalently, you may simply insert its ID (uniprot_id) directly into a UniProt hyperlink as follows:

#http://www.uniprot.org/uniprot/uniprot_id
#For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

#Swiss-Prot holds protein data as a structured .txt file. You can obtain it by simply adding .txt to the link:

#http://www.uniprot.org/uniprot/uniprot_id.txt
#Given: The UniProt ID of a protein.

#Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).

from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('B5ZC00') 
record = SwissProt.read(handle)
list = record.keywords
print(list)

#Expected output:
#['Aminoacyl-tRNA synthetase', 'ATP-binding', 'Cytoplasm', 'Ligase', 'Nucleotide-binding', 'Protein biosynthesis']

