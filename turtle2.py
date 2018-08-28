#####################################
# This is a simple program 			#
# experiment with the turtle		#
# library							#
# Class			: Arch 7210			#
# Instructor	: Alireza Karduni	#
# Stuent		: Jarrod Norris		#
#####################################

import turtle
# Sets a screen for the app to run in
w = turtle.Screen()
# Sets the colormode for working with rgb
w.colormode(255)
#Sets background color
w.bgcolor("#808080")
# Creates a turtle
t = turtle.Turtle()
t.speed(0)
# Number of iterations
x = 73
# Radius of circle
s = 365
# For use with alternative coloring
i = 0
#Pen and fill colors
r = 0
g = 255
b = 255
h = 255
j = 40
k = 40
# Alternative coloring schema
pre = "#"
post = "ffff"
color = ["#ffffff", "#e6ffff", "#ccffff", "#b3ffff", "#99ffff", "#80ffff",
         "#66ffff", "#4dffff", "#33ffff", "#1affff", "#00ffff", "#00e6e6",
		 "#00cccc", "#00b3b3", "#009999", "#008080", "#006666", "#004d4d",
		 "#003333", "#001a1a", "#000000"]
		 
#t.pencolor("red")

# Loop to create multiple circles and adjust size and color
while x > 0 :
	t.pencolor(h,j,k)
	t.fillcolor(r,g,b)
	t.begin_fill()
	t.circle(s)	
	t.right(5)
	s=s-5
	x=x-1
	i=i+1
	g=g-3
	b=b-3
	h=h-1
	j=j+1
	k=k+1
	t.end_fill()
# Raises pen to move 
t.penup()
#Color schema for second image
r = 51
g = 204
b = 51
t.pencolor("orange")
# Moves the beginning point and lowers pen to canvas
t.goto(-300, 0)
t.pendown()
# Number of iterations and size of beginning circle
x = 20
s=10
# Loop to create multiple circles and adjust size and color
while x > 0 :
	t.fillcolor(r,g,b)
	t.begin_fill()
	t.circle(s)
	t.left(10)
	s=s+5
	x=x-1
	r=r-2
	g=g-5
	b=b-2
	t.end_fill()
# Ends the program an leaves window open	
turtle.done()
