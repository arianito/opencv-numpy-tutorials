# Image Processing - Fall 2017 - IAUD
# Written by Aryan Alikhani
#
# Introduction how to use Matplotlib And Numpy
# visit https://github.com/ary4n/opencv-numpy-tutorials
#

# numpy is a common way to build and manipulate matrix operations in a simples posible way, just as awesome as matlab is.
import numpy as np
# cv library, it is not used here, just for making sure that it has been installed successfully, were gonna use it in future!
import cv2
# matplotlib is also a common library mostly used for visualizing data just like matlab ploting library, powerfull and handy.
from matplotlib import pyplot as plt
# matplotlib widgets library, the amazing Slider that we have used in this example
import matplotlib.widgets as widget



# defining sinc(t) function for testing some matplotlib functionalities.
# ampl parameter is defined as global function and used in sinc(t) function, actually we could do such a thing because we
# are writung in python and python is very high level language which automaticaly free and release memory at runtime,
# so dont be worry about this.
ampl = 1
def sinc(t):
	# t is a sequence array user for interpolating time
	# we used numpy math to create out sinc function! just like this.
	return ampl * (np.sin(np.pi * t) / (np.pi * t))


# now create a time steps array, given this to function as x(input), will interpolate y(output)
time_steps = np.arange(-10.0, 10.0, 0.02)


# make sure that we are running on console
if __name__ == '__main__':
	# create a ploting view first argument is number of rows and second is number of columns, we just need one ploting view so ..
	window, ploting_context = plt.subplots(1, 1, sharey='row', figsize=(9, 6))

	# set some titles
	window.canvas.set_window_title('Figure')
	window.suptitle('Introduction how to use Matplotlib And Numpy')
	# adjust ploting margins, for better viewing i guess?
	window.subplots_adjust(left=0.25, bottom=0.25)



	# enable grids
	ploting_context.grid()


	# now that we have created our ploting context, now we could add a plot, the first parameter is a array of numbers which it represents
	# a timing steps, and second argument is going to be out sinc(t) function that get timing steps as input to create our desired output.
	plot1, = ploting_context.plot(time_steps, sinc(time_steps), 'k')


	# so! now that we have ploted our sinc(t) function lets add some cool Sliders to change and manipulate our graph in realtime
	#  >> actualy it's cool to see how matplotlib works in realtime! with this functionality we could have more interaction with our
	# image proccessing proccess in future.


	# now we first create two axes, axes are containers in matplotlib, we use them to put our sliders in every each of them.
	# second slider for amplitude, your gonna like it.
	# and next is reset button ..
	axe_time = window.add_axes([0.25, 0.1, 0.65, 0.03], facecolor='gray')
	axe_ampl = window.add_axes([0.25, 0.15, 0.65, 0.03], facecolor='gray')
	axe_reset = window.add_axes([0.03, 0.15, 0.1, 0.03], facecolor='gray')

	# now the sliders take and axe as input and we tell slider ranges, name
	slider_time = widget.Slider(axe_time, 'Time Scale', 0., 40., 10.)
	slider_ampl = widget.Slider(axe_ampl, 'Amplitude', 0., 4., 1.)

	button_reset = widget.Button(axe_reset, 'Reset', hovercolor='0.9')

	# after every user interaction with slider, this function will get called, we assign it to change event on slider next.
	def on_ampl_changed(val):
		# first load amplitude variable from global context, global things works like this in python
		global ampl, time_steps
		# set the amplitude..
		ampl = val
		# now we have to reset our plot's data

		plot1.set_data(time_steps, sinc(time_steps))

		window.canvas.draw_idle()
		pass

	def on_time_change(val):
		# load time_steps from global just like before
		global time_steps
		# re-intitialize it with new range
		time_steps = np.arange(-val, val, 0.02)
		# reset ..
		plot1.set_data(time_steps, sinc(time_steps))

		# request ploting view to recalculate the max and mins and fit the graph on screen
		ploting_context.relim()
		ploting_context.autoscale_view()
		window.canvas.draw_idle()
		pass

	# reset everything!
	def on_reset_clicked(val):
		global time_steps,ampl
		ampl = 1
		time_steps = np.arange(-10.0, 10.0, 0.02)
		plot1.set_data(time_steps, sinc(time_steps))

		ploting_context.relim()
		ploting_context.autoscale_view()
		window.canvas.draw_idle()
		pass

	# done!!!
	# now lets set these functions to our sliders so when they get changed, update methods get called.
	slider_ampl.on_changed(on_ampl_changed)
	slider_time.on_changed(on_time_change)

	# and for button ...
	button_reset.on_clicked(on_reset_clicked)

	# view every thing
	plt.show()




	# i hope you enjoy this tutorial, and thanks to my teacher vahid khoramshahi.