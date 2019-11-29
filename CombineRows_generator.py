
def CombineRowsList(listToCompress, regions):
	import re
	# listToCompress=[[1,2,2,3],[1,2,2,23,4,6],[2,4,6,7,8], [1,2,3,4]]
	# regions = ['GeneA.g1.e', 'GeneB.g2.e', 'GeneA.g5.e', 'GeneC.g1.e']
	# Variables used for generating a splice list, indices of where the regions have been merged, used in the region plot figure to add black seperating lines. One for each line in the bed file
	splice_full = [] # contain the length of each list in the list to compress, hence the last position of every coverage depth value list. One per row in the bed file containing regions
	for line in listToCompress:
		splice_full.append(len(line))

	splice_temp = {} # Only contains a temporary splicing value
	splice = [] # Contain lists of all splice values one list per merged region

	current_region = [] # Current region name
	combine_temp = {} # Temporary list with lines to compress
	newList=[] # Contain the new merged list from listToCompress
	region_name=[]

	index=0 #-1 # Start at -1 that would be the previous element for the first element in the list, the -1 index is skipped and we move forward in the list
	# regions.append('end.extra') # add one extra element to the list as for each line the previous information is stored
	# listToCompress.append(['end.extra']) # add one extra elemtn to the list as for each line the previous information is stored
	for line in regions:
		current_region = re.split('\.|,|_',line)
		if (current_region[0] == 'iSNP' or current_region[0] == 'iIndel' or current_region[0] == 'MSI'):
			current_region[0] = "-".join([current_region[0],current_region[1],current_region[2]])
			current_region[1] = "-".join([current_region[0],current_region[1],current_region[2]])
			current_region[2] = "-".join([current_region[0],current_region[1],current_region[2]])
		current_region = current_region[0]

		if current_region in splice_temp.keys():
			splice_temp[current_region].append(splice_full[index])
			combine_temp[current_region]=combine_temp[current_region]+listToCompress[index]

		else:
			splice_temp[current_region]=[splice_full[index]]
			combine_temp[current_region]=listToCompress[index]
		index+=1
	splice = [v for v in splice_temp.values()]
	newList = [v for v in combine_temp.values()]
	region_name = [k for k in combine_temp.keys()]
	# Return the generated lists
	return region_name, newList, splice

	######################### Genrates new list of merged information rows for the validation table. The original region information list contains
	# the values chr start, stop and length. If the information comes from the same region name the values will be added horisontally
	# list to compress=[[chr 1', 'start', 'stop'], [chr 1', 'start', 'stop'], [chr 1', 'start', 'stop'], [chr 1', 'start', 'stop']]
	# regions = ['GeneA.g.1.e', 'GeneA.g.2.e', 'GeneB.g.1.e', 'GeneC.g.1.e']

def CombineRegionInfo(listToCompress, regions):
	import re

	current_region = []
	combine_temp = {}
	newList=[]
	index=0 # Since we compare with the previous start at -1 instead of 0 to jump one step and start with the first element as a previous value

	for line in regions:
		current_region = re.split('\.|,|_',line)
		if (current_region[0] == 'iSNP' or current_region[0] == 'iIndel' or current_region[0] == 'MSI'):
			current_region[0] = "-".join([current_region[0],current_region[1],current_region[2]])
			current_region[1] = "-".join([current_region[0],current_region[1],current_region[2]])
			current_region[2] = "-".join([current_region[0],current_region[1],current_region[2]])
		current_region = current_region[0]

		if current_region in combine_temp.keys():
			combine_temp[current_region]=combine_temp[current_region]+listToCompress[index]

		else:
			combine_temp[current_region]=listToCompress[index]
		index+=1

	newList = [v for v in combine_temp.values()]
	# region_name = [k for k in combine_temp.keys()]

	return newList
