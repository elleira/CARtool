# Generate region positions with over or under threshold values in a figure

def Region_generator_plot(det_list_row, Regions, Xcov, index, fig, splice, hotspot):
	import matplotlib
	matplotlib.use('Agg')
	import matplotlib.pyplot as plt
	from matplotlib.collections import PatchCollection
	import matplotlib.patches as mpatches
	import tkinter
	import matplotlib._color_data as mcd
	import matplotlib.lines as lines
	import matplotlib.text as text
	import matplotlib.gridspec as gridspec

	ax = fig.add_subplot(2,2,index)
	count=0
	count_element = 1
	count_hotspot = 1
	patches=[]
	Sq_under = []
	Sq_over = []
	hight = len(det_list_row)*1.1
	bredth = len(det_list_row)*0.01
	arrow_bredth=int(len(det_list_row))*0.4

	# If hotspots is activated and contains a value on the last base in the region figure insert it one step to make sure it is printed
	if not(hotspot==[]) and int(hotspot[-1])==int(len(det_list_row)):
		hotspot[-1]=int(len(det_list_row))-1

	if splice:
		splice_element_index=0
		splice_site = splice[0]

	line_temp = []
	arrow=[]

	#Check the values in the list, if bellow threshold add a yellow square to the image else a blue.
	for element in det_list_row:


		if int(element) < int(Xcov):
			Sq_under = mpatches.Rectangle([count*10,0], 10, hight, color= 'orange', capstyle = 'butt', joinstyle='miter')
			patches.append(Sq_under)


		if int(element) >= int(Xcov):
			Sq_over = mpatches.Rectangle([count*10,0], 10, hight, color= 'blue', capstyle = 'butt', joinstyle='miter')
			patches.append(Sq_over)

		# If the region figure comes from multiple rows in the bed file, distinguise the new line with a dark line.
		if splice:
			if not(len(splice)==1) and int(splice_element_index) < int(len(splice)-1):
				if int(count_element) == int(splice_site):
					line_temp = mpatches.Rectangle([count*10,-0.5*hight], bredth, 0.49*hight, color= 'black')
					patches.append(line_temp)
					splice_element_index+=1
					splice_site += int(splice[splice_element_index])

		# Add an arrow if there is a hotspot on this location

		if int(count_element-1) in hotspot:
			arrow = mpatches.Arrow(count*10,hight*1.8, 0, -0.8*hight, width=(int(arrow_bredth)))
			patches.append(arrow)

		Sq_over = []
		Sq_under = []
		count+=1
		count_element+=1

	# Add to figure and return the image
	collection = PatchCollection(patches, match_original=True)
	ax.add_collection(collection)
	plt.axis('equal')
	plt.axis('off')
	ax.set_title(str(Regions))
	return fig
