#!/usr/local/bin/python

import sys #library that allows you to communicate via command line
from Bio import AlignIO #load AlignIO (input/output) class from BioPython library

"""Problem: You have an alignment file of two 16S rRNA genes (fasta format) and want to calculate the percent identity between them
"""

class colors:
	COMPLETE = '\033[92m'

align = AlignIO.read(sys.argv[1], "fasta")
first_seq = list(align[0])
next_seq = list(align[1])

matches = 0 #initialize values for loop 

for nucleotide in range(0, len(first_seq)):
        if first_seq[nucleotide] == next_seq[nucleotide]:
                matches += 1
	else:
		continue #you can also skip this else statement, will do the same thing

perc_id = (matches*100)/float((len(first_seq)))

print colors.COMPLETE + "Percent identity: %.2f" %perc_id

