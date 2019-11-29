#subpart names
import re
def bar_names_generator(list_to_compress, regions):

#example input, regions = ['hej.g.1.e', 'hej.g.2.e', 'hej.g.1.e', 'h.g.1.e']
	regions_temp_bar = {}
	region_name=[]
	region_name_bar=[]
	list_of_lists=[]


	# compute region subpart name list
	for line in regions:
		l = re.split('\.|,|_', line)
		# l = line.split('.')
		# here the third element in the region name after a '.' is taken as the subpart name
		exomnr = re.findall(r'\d+',l[1])
		# import pdb; pdb.set_trace()
		list_of_lists.append([l[1][0]+''.join(exomnr)])
	region_name = [val for sublist in list_of_lists for val in sublist]
	# Add subpart names from the same combined region in a nested list
	# previous_region = []
	index=0 #-1
	# regions.append('end.extra')
	current_region = []
	formated_bar_temp={}
	detailed_list_formated_bar=[]


	for line in regions:
		# current_region = line.split('.')
		current_region =  re.split('\.|,|_', line)
		current_region = current_region[0]

		if current_region in regions_temp_bar.keys():
			regions_temp_bar[current_region].append(region_name[index])
			formated_bar_temp[current_region].append(list_to_compress[index])

		else:
			regions_temp_bar[current_region] = [region_name[index]]
			formated_bar_temp[current_region] = [list_to_compress[index]]
		index+=1

	detailed_list_formated_bar = [v for v in formated_bar_temp.values()]
	region_name_bar = [v for v in regions_temp_bar.values()]
	# 	if not(previous_region ==[]):
	# 		import pdb; pdb.set_trace()
	# 		if previous_region == current_region:
	# 			regions_temp_bar.append(region_name[index])
	# 			formated_bar_temp.append(list_to_compress[index])
	#
	# 		else:
	# 			regions_temp_bar.append(region_name[index])
	# 			region_name_bar.append(regions_temp_bar)
	# 			formated_bar_temp.append(list_to_compress[index])
	# 			detailed_list_formated_bar.append(formated_bar_temp)
	#
	# 			regions_temp_bar=[]
	# 			formated_bar_temp=[]
	#
	# 	index+=1
	# 	previous_region=current_region
	# regions.pop()

	return region_name_bar, detailed_list_formated_bar
