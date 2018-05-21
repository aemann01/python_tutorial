import sys #library that allows you to communicate via command line
from Bio import AlignIO #load AlignIO (input/output) class from BioPython library

"""Problem: You have an alignment file of two 16S rRNA genes (fasta format) and want to calculate the percent identity between them
"""

#add fancy colors to the output of your screen (in this case green when the script is complete)
class colors:
	COMPLETE = '\033[92m'

#initialize our data/variables
align = AlignIO.read(sys.argv[1], "fasta")
first_seq = list(align[0])
next_seq = list(align[1])

def pid():
	matches = 0 #initialize values for loop 

	for nucleotide in range(0, len(first_seq)):
        	if first_seq[nucleotide] == next_seq[nucleotide]:
                	matches += 1

	perc_id = (matches*100)/float((len(first_seq)))

	print(colors.COMPLETE + ("Percent identity: %.2f" % perc_id))

pid()
