'mafft_with_seq' files contain the multiple sequence alignments for all the enzymes analyzed in our study, which are potentially involved in the production of 2,4-DAB or BMAA.
The 'active_site_position' files provided by Maria Mantas were updated to capture the amino acids at specified positions. 
The 'HD' files are Python scripts designed to calculate the Hamming distance between a new sequence and reference sequences. To run the script, use the following command in the Linux bash environment:

```bash
python hd_file.py WP Output
```

Here, `WP` and `Output` are the two required arguments: `WP` is the WP number of the new sequence, and `Output` is the output from the 'active_site_position' file. The script will use these inputs to compute the Hamming distance.
