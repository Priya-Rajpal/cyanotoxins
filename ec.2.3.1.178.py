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
	print header, ",", seq[155], seq[156], seq[158], seq[159], seq[161], seq[195], seq[346], seq[433], seq[435], seq[436], seq[629], seq[634], seq[844], seq[898]
