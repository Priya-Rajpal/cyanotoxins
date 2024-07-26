#!/usr/bin/env python

import sys 

# parse fasta into dict
with open(sys.argv[1], 'r') as fasta:
	fasta_dict = {}
	for line in fasta:
		if line.startswith(">"):
			header = line.rstrip("\n").replace(">", "")
			fasta_dict[header] = '' # make key equal to header and value equal to empty string
		else:
			fasta_dict[header] += line.rstrip("\n") # add line to empty string

# iterate over key value pairs and print header and amino acid positions of interest (accounting for zero-based indexing)
for header, seq in fasta_dict.items():
	print header, ",", seq[133],seq[135], seq[137], seq[152], seq[156], seq[169], seq[172], seq[174], seq[176], seq[181], seq[191], seq[199], seq[202], seq[204], seq[210], seq[225], seq[227], seq[229], seq[256], seq[258], seq[282], seq[286], seq[288]
