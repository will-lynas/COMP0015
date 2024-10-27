"""
Name: question_2.py

Description:

Draw a square.

Author:

Date:

Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name

"""

from turtle import *

speed(0)


# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw the smallest square

for counter in range(4):   # repeat 4 times
    forward(50)
    left(90)

# Square 2
penup()
setpos(-220, 0)
pendown()

pencolor("blue")

for counter in range(4):
    forward(80)
    left(90)

# Square 3
penup()
setpos(-110, 0)
pendown()

pencolor("green")

for counter in range(4):
    forward(110)
    left(90)

# Square 4
penup()
setpos(30, 0)
pendown()

pencolor("red")

for counter in range(4):
    forward(130)
    left(90)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()
