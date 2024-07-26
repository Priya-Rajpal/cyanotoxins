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
	print header, ",", seq[3020], seq[3023], seq[3030], seq[3077], seq[3078], seq[3084], seq[3085], seq[3087], seq[3137], seq[3142], seq[3145], seq[3177], seq[3179], seq[3198], seq[3260], seq[3262], seq[3263], seq[3266], seq[3267], seq[3269], seq[3270], seq[3271], seq[3272], seq[3276], seq[3277], seq[3278], seq[3298], seq[3299], seq[3300], seq[3310], seq[3312], seq[3313], seq[3315], seq[3316], seq[3317], seq[3318], seq[3319], seq[3320], seq[3321], seq[3322],seq[3323], seq[3324], seq[3325], seq[3326], seq[3327], seq[3329], seq[3330], seq[3331], seq[3332], seq[3333], seq[3334], seq[3348], seq[3351], seq[3352], seq[3354], seq[3355], seq[3356], seq[3373], seq[3374], seq[3377], seq[3386], seq[3387], seq[3388], seq[3389], seq[3390], seq[3391], seq[3392], seq[3393], seq[3394], seq[3395], seq[3396], seq[3397], seq[3398], seq[3399], seq[3403], seq[3404], seq[3406], seq[3410], seq[3474], seq[3483], seq[3485], seq[3487], seq[3488], seq[3489], seq[3490], seq[3541], seq[3542], seq[3544], seq[3545], seq[3546], seq[3547], seq[3548], seq[3549], seq[3550], seq[3551], seq[3552], seq[3553], seq[3554], seq[3555], seq[3556], seq[3557], seq[3559], seq[3560], seq[3562], seq[3565], seq[3587], seq[3590], seq[3600], seq[3602], seq[3603], seq[3607], seq[3629], seq[3633], seq[3635], seq[3642], seq[3643], seq[3644], seq[3645], seq[3647], seq[3649], seq[3650], seq[3651], seq[3652], seq[3653], seq[3659], seq[3704], seq[3709], seq[3711], seq[3712], seq[3745], seq[3746], seq[3749],seq[3752], seq[3753], seq[3776], seq[3777], seq[3778], seq[3780], seq[3782], seq[3784], seq[3787], seq[3788], seq[3789], seq[3790], seq[3791], seq[3795], seq[3796], seq[3798], seq[3799], seq[3800], seq[3801], seq[3802], seq[3803], seq[3804], seq[3805], seq[3806], seq[3812], seq[3827], seq[3833], seq[3835], seq[3837], seq[3838], seq[3839], seq[3840], seq[3843], seq[3844], seq[3847], seq[3848], seq[3849], seq[3850], seq[3851], seq[3852], seq[3853], seq[3855], seq[3856], seq[3857], seq[3858], seq[3859], seq[3860], seq[3861], seq[3862], seq[3863], seq[3864], seq[3865], seq[3869], seq[3871], seq[3872], seq[3876], seq[3878], seq[3879], seq[3883], seq[3885], seq[3887], seq[3891], seq[3892], seq[3893], seq[3894], seq[3944], seq[3955], seq[3966], seq[4020], seq[4022], seq[4028], seq[4030], seq[4035], seq[4045], seq[4070], seq[4073], seq[4074], seq[4075], seq[4077], seq[4079], seq[4110], seq[4114], seq[4116], seq[4117], seq[4123], seq[4124], seq[4125], seq[4158], seq[4159], seq[4161], seq[4163], seq[4184], seq[4187], seq[4198], seq[4199], seq[4201], seq[4202], seq[4206], seq[4261] 
