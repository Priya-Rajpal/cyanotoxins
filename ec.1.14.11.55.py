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
	print header, ",", seq[752], seq[865], seq[868], seq[942], seq[943], seq[944], seq[947], seq[978], seq[980], seq[981], seq[982], seq[990], seq[991], seq[992], seq[993], seq[1005], seq[1006], seq[1011], seq[1012], seq[1013], seq[1024], seq[1043], seq[1107], seq[1109], seq[1160], seq[1165], seq[1169], seq[1172], seq[1174], seq[1178], seq[1398], seq[1402], seq[1601], seq[1620]
