'''Creates boxplot of fragment length statistics. Data should be a single column of integers with no header. Usage: python makeBoxplot.py *.len -- second argument is string indicating the pattern to match when searching for files
'''

import matplotlib.pyplot as plt
import sys
import glob

dataToPlot = []
fileList = glob.glob('*len*')
#print(fileList)


for fileName in fileList:
	lines = [line.rstrip('\n') for line in open(fileName)]
	converted = [int(i) for i in lines]
	dataToPlot.append(converted)


#print(dataToPlot)

fig = plt.figure(1, figsize=(10,10))
ax = fig.add_subplot(111)
bp = ax.boxplot(dataToPlot, sym='', showfliers=False)
#with outliers
#bp = ax.boxplot(dataToPlot)

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.set_ylim([0, 200])
xnames = [i.replace('*len*', '') for i in fileList]
ax.set_xticklabels(xnames, fontsize=10)
plt.xticks(rotation=90)

fig.savefig('lenbp.png', bbox_inches='tight')
fig.savefig('lenbp.pdf', format='pdf', bbox_inches='tight')
fig.savefig('lenbp.svg', format='svg', bbox_inches='tight')

#with outliers
#fig.savefig('lenbp_outliers.png', bbox_inches='tight')
#fig.savefig('lenbp_outliers.pdf', format='pdf', bbox_inches='tight')
