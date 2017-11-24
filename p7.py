# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# Create rgb historgram from image
# visit https://github.com/ary4n/opencv-numpy-tutorialss
#

# importing essential libraries just like before.
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.widgets as widget


if __name__ == '__main__':
	# create two plot side by side by setting columns to one
	window, ploting_context = plt.subplots(2, 1, sharey='row', figsize=(12, 8))


	plot_hist = ploting_context[0]
	plot_image = ploting_context[1]

	# set titles
	window.canvas.set_window_title('Figure')
	window.suptitle('Create rgb historgram from image')


	# load image into memory
	source = cv2.imread('coins.jpg', cv2.IMREAD_COLOR)


	plot_image.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB), interpolation='bicubic')


	color = ('b', 'g', 'r')
	for i, col in enumerate(color):
		hist = cv2.calcHist([source], [i], None, [1000], [0, 256])
		plot_hist.plot(hist, color=col, alpha=0.5)



	# done!

	plt.show()

