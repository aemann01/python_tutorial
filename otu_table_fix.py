import sys #library that allows you to communicate via command line
import pandas as pd #load and set up alias for pandas library

"""PROBLEM: you have a tab delimited OTU table called filtered_otu_table_L6.txt with redundant taxa strings that need to be collapsed
"""

data = pd.read_csv(sys.argv[1], sep="\t", skiprows=1)

def fixOTU():
	fixed_data = data.groupby("#OTU ID").sum()

	#how many duplicate records were in the file?

	duplicates = data.shape[0] - fixed_data.shape[0]
	print("Number of duplicate rows to be collapsed: %i" %duplicates)

	#now write your fixed OTU table to file

	with open("collapsed_otu_table.txt", "w") as outfile:
		fixed_data.to_csv(outfile, sep="\t")

	outfile.close() #you're done writing to file, close it (not necessary but good practice)

	print("Complete, collapsed OTU table written to: collapsed_otu_table.txt") #tell the user that it's done!

fixOTU()
