import matplotlib.pyplot as plt

def generate_chart(total_files, occurrencies):
	# The slices will be ordered and plotted counter-clockwise.
	labels = 'With @Refactoring', 'Without @Refactoring'
	sizes = [total_files, occurrencies]
	colors = ['yellowgreen', 'gold',]
	explode = (0, 0.1) # only "explode" the 2nd slice (i.e. 'Hogs')

	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	        autopct='%1.1f%%', shadow=False, startangle=180)
	# Set aspect ratio to be equal so that pie is drawn as a circle.
	plt.axis('equal')
	plt.savefig('c:/Temp/lalala.png')
	plt.show()
