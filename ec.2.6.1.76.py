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
	print header, ",", seq[3637], seq[3639], seq[3641], seq[3642], seq[3736], seq[3808], seq[3811], seq[3821], seq[3826], seq[3828], seq[3829], seq[3833],seq[3837], seq[3838], seq[3839], seq[3840], seq[3841], seq[3842], seq[3857], seq[3861], seq[3865], seq[3870], seq[3874], seq[3875], seq[3883], seq[3890], seq[3891], seq[3917], seq[3918], seq[3919], seq[3920], seq[3922], seq[3924], seq[3925], seq[3927], seq[3929], seq[3962], seq[3963], seq[3969], seq[3970], seq[3977], seq[3978], seq[3983], seq[3984], seq[3987], seq[3989], seq[3992], seq[3994], seq[4034], seq[4038], seq[4042], seq[4141], seq[4142], seq[4147], seq[4150], seq[4151], seq[4152], seq[4153], seq[4154], seq[4155], seq[4157], seq[4159], seq[4179], seq[4198], seq[4199], seq[4200], seq[4201], seq[4203], seq[4204], seq[4205], seq[4206], seq[4207], seq[4208], seq[4211], seq[4212], seq[4213], seq[4214], seq[4219], seq[4226], seq[4227], seq[4232], seq[4233], seq[4234], seq[4237], seq[4239], seq[4242], seq[4247], seq[4262], seq[4264], seq[4266], seq[4267], seq[4280], seq[4281], seq[4282], seq[4283], seq[4284], seq[4285], seq[4286], seq[4291], seq[4294], seq[4302], seq[5217], seq[5218], seq[5219], seq[5223], seq[6627], seq[6815], seq[6897], seq[6915], seq[6923], seq[6924], seq[6926], seq[7091]

