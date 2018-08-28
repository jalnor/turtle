#####################################
# This is a simple program 			#
# experiment with the turtle		#
# library							#
# Class			: Arch 7210			#
# Instructor	: Alireza Karduni	#
# Stuent		: Jarrod Norris		#
#####################################

import turtle
from structure import Structure
from background import Background
# Sets a screen for the app to run in
turtle.setup(width = 1900, height=1060, startx = 0, starty = 0)
w = turtle.Screen()

w.title("Fort Norris")
# Sets the colormode for working with rgb
w.colormode(255)
#Sets background color
b1 = Background(w.window_width(),(w.window_height()-660),"#80e5ff",-950,530)
b1.drawSquare()
b2 = Background(w.window_width(),(w.window_height()-400),"#008000",-950,130)
b2.drawSquare()


nw = Structure(-475, 255, "nw")
nw.drawRoof()
nw.drawTower()

ne = Structure(475, 255, "ne")
ne.drawRoof()
ne.drawTower()

sw = Structure(-375, -200, "sw")
sw.drawRoof()
sw.drawTower()

se = Structure(575, -200, "se")
se.drawRoof()
se.drawTower()




 

turtle.done()