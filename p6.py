# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# Reconstruct image from most-significant bits to lowest
# visit https://github.com/ary4n/opencv-numpy-tutorialss
#

# importing essential libraries just like before.
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.widgets as widget


if __name__ == '__main__':
	# create two plot side by side by setting columns to one
	window, ploting_context = plt.subplots(4, 2, sharey='row', figsize=(12, 8))

	# set titles
	window.canvas.set_window_title('Figure')
	window.suptitle('Reconstruct image from most-significant bits to lowest')



	# load image into memory
	source = cv2.imread('dollar.png', cv2.IMREAD_COLOR);
	gray_img = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

	height, width = gshape = gray_img.shape

	blank_image = np.zeros((height, width), dtype=np.uint8)

	for i in range(4):
		for j in range(2):
			index = (i*2+j)
			plot = ploting_context[i][j]
			plot.set_title('Without Bit %i' % index)

			for px in range(width):
				for py in range(height):
					blank_image[py, px] = gray_img[py, px] & (0b11111111 >> index)


			plot.imshow(blank_image, cmap='gray', interpolation='bicubic')



	# done!

	plt.show()

