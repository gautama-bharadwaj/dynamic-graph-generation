#Program to plot graphs on data present in text file T2.txt

#Importing libraries for plotting graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#Styling the displayed graph
style.use('fivethirtyeight')

#Defining the plot
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#Function to read text file and plot the graph
def animate(i):
	#Opens text file named T2.txt and reads the values
	graph_data = open('T2.txt', 'r').read()
	#lines stores different lines separated by newline
	lines = graph_data.split('\n')
	#Defining variables xs and ys that will act as the axes for the graph
	xs = []
	ys = []
	#Defining variable time which will be the x-axis
	time = 1
	#Looping till the number of lines in T2.txt
	for line in lines:
		if len(line) > 1:
			#Find if + or - is present in the line
			char = line.find('+')
			#If + is present, then execute this code block
			if char == 6:
				#Splice the line with +
				x, y = line.split('+')
				#Remove left blank space
				y.lstrip()
				#Splice again to get the number only
				y1, x1 = y.split('.')
				#Remove left blank space
				y1.lstrip()
				#Convert string to integer
				y1 = int(y1)
				#Append time (x-axis) and y1 (y-axis) to xs and ys
				xs.append(time)
				ys.append(y1)
				#Increment time
				time = time+1
			#Same loop as above but if - character is present in the line
			else:
				#Splice the line with -
				x, y = line.split('-')
				#Splice again to get the number only
				y1, x1 = y.split('.')
				#Remove left blank space
				y1.lstrip()
				#Convert string to integer
				y1 = int(y1)
				#Append time (x-axis) and y1 (y-axis) to xs and ys
				xs.append(time)
				ys.append(y1)
				#Increment time
				time = time+1
	#Clear the plot everytime the function is called
	ax1.clear()
	ax1.plot(xs, ys)
#Runs the function animate(i) at intervals of 1000ms
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()




