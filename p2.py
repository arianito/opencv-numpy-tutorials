# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# Loading image into opencv and view it by matplotlib
# visit https://github.com/ary4n/opencv-numpy-tutorialss
#

# importing essential libraries just like before.
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.widgets as widget


if __name__ == '__main__':
	# crearing context like before
	window, ploting_context = plt.subplots(1, 1, sharey='row', figsize=(6, 6))

	# set some titles
	window.canvas.set_window_title('Figure')
	window.suptitle('Loading image into opencv')
	ploting_context.set_title('Our favorite Camera man!')

	# loading image is so simple like:
	source = cv2.imread('cameraman.jpg');


	# and add it to ploting window
	# change opencv color mapping from BGR to RGB cause matplotlib only knows how to show RGB images
	ploting_context.imshow(cv2.cvtColor(source, cv2.COLOR_RGB2BGR), interpolation='bicubic')

	plt.show()

