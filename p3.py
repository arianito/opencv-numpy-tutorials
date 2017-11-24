# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# Loading image into opencv and view it by matplotlib
#

# importing essential libraries just like before.
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.widgets as widget


if __name__ == '__main__':
	# first load our desired image
	first_image = cv2.imread('cameraman.jpg');

	# crearing context like before
	fig, ploting_context = plt.subplots(1, 1, sharey='row', figsize=(9, 6))

	# set some titles
	fig.canvas.set_window_title('Figure')
	fig.suptitle('Loading image into opencv')

	# show image in figure
	ploting_context.imshow(first_image, interpolation='bicubic')


	plt.show()

