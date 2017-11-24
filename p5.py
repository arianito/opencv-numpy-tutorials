# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# Find center of dark objects in screen
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
	window.suptitle('Find center of dark objects in screen')
	plot_left.set_title('Original Image')
	plot_right.set_title('Centers')



	# load image into memory
	source = cv2.imread('coins.jpg', cv2.IMREAD_COLOR);

	# show original image on left plot
	plot_left.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB), interpolation='bicubic')

	# create a new black and white image
	gray_img = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

	# view it on right plot



	ret, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

	kernel = np.ones((3, 3), np.uint8)
	opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

	# sure background area
	sure_bg = cv2.dilate(opening, kernel, iterations=3)

	# Finding sure foreground area
	dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
	ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

	# Finding unknown region
	sure_fg = np.uint8(sure_fg)
	ploted_image = plot_right.imshow(sure_fg, cmap='gray', interpolation='bicubic')

	# done!

	plt.show()

