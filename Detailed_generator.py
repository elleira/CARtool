def detail_samtools(Regions, Read_depth):

	# create a detailed list with all depth values from the same region in a sub list. From samtools depth calculations
	# samtools generates a depth file with: chr, position and coverage depth value
	# Regeions comes from the bed file with chr, start, stop, region name
	BaseCov_dict = {i[0]+"_"+i[1]:i[2] for i in Read_depth} #chrX_pos:coverge

	detailed = []

	for roi in Regions:
		BaseCov_Region_temp = []
		for pos in range(int(roi[1])+1,int(roi[2])+1,1): #Samtools 0 indexed
			keyvalue = roi[0]+"_"+str(pos)
			BaseCov_Region_temp.append(BaseCov_dict[keyvalue])
		detailed.append(BaseCov_Region_temp)





	# detailed =[]
	# list_temp=[]
	# previous_chr = Read_depth[0][0]
	# Region_row = 0
	# count=0
	# index = 0
	# size_list = len(Read_depth)
	#
	# for line in Read_depth:
	# 	Region_row = Regions[index]
	# 	if str(line[0]) == str(previous_chr) and (int(line[1])) <= int(Region_row[2]):
	# 		list_temp.append(line[2])
	#
	# 	else:
	# 		previous_chr=line[0]
	# 		detailed.append(list_temp)
	# 		list_temp=[]
	# 		list_temp.append(line[2])
	# 		index+=1
	#
	# 	count+=1
	# 	if count == size_list:
	# 		detailed.append(list_temp)

	return detailed


