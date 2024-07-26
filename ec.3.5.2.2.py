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
        print (header,"," , seq[59], seq[61], seq[150], seq[155], seq[183], seq[239], seq[289], seq[316], seq[337])
