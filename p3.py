# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# B/W Image using opencv
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
	window.suptitle('Create B/W Image')
	plot_left.set_title('Original Image')
	plot_right.set_title('Grayscale Image')


	# load image into memory
	source = cv2.imread('lena.jpg', cv2.IMREAD_COLOR);

	# show original image on left plot
	plot_left.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB), interpolation='bicubic')

	# create a new black and white image
	gray_img = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

	# view it on right plot
	plot_right.imshow(gray_img, cmap='gray', interpolation='bicubic')

	# done!

	plt.show()

