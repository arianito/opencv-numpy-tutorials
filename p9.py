# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# Sharpen Image
# visit https://github.com/ary4n/opencv-numpy-tutorialss
#

# importing essential libraries just like before.
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.widgets as widget


if __name__ == '__main__':
	# create two plot side by side by setting columns to one
	window, ploting_context = plt.subplots(1, 2, sharey='row', figsize=(13, 6))


	# load ploting views into new variables
	plot_left = ploting_context[0]
	plot_right = ploting_context[1]


	# set titles
	window.canvas.set_window_title('Figure')
	window.suptitle('Sharpening image')
	plot_left.set_title('Original Image')
	plot_right.set_title('Sharped Image')

	# set margins
	window.subplots_adjust(bottom=0.25)


	# load image into memory
	source = cv2.imread('skull.png', cv2.IMREAD_COLOR);

	# show original image on left plot
	plot_left.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB), interpolation='bicubic')


	# view it on right plot
	ploted_image = plot_right.imshow(source, cmap='gray', interpolation='bicubic')


	axe_level = window.add_axes([0.25, 0.1, 0.50, 0.03], facecolor='gray')

	slider_level = widget.Slider(axe_level, 'Level', 1.0, 20.0, 9.0)

	def on_change(val):
		global source

		kernel = np.array([[-1,-1,-1], [-1,val,-1], [-1,-1,-1]])

		sharped_image = cv2.filter2D(source, -2, kernel)


		median = cv2.medianBlur(sharped_image,  3)

		ploted_image.set_data(cv2.cvtColor(median, cv2.COLOR_BGR2RGB))

		window.canvas.draw_idle()

	on_change(9)

	slider_level.on_changed(on_change)

	# done!

	plt.show()

