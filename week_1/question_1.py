"""
Name: question_1.py

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
pencolor("dark sea green")

# Draw a square
forward(50)     # move forward 50 pixels
left(90)        # turn left 90 degrees
forward(50)
lt(90)          # an abbreviation for turn left
fd(50)          # an abbreviation for move forward
lt(90)
fd(50)
lt(90)

# Square 2
penup()
setpos(-220, 0)
pendown()

pencolor("blue")

forward(80)
left(90)
forward(80)
lt(90)
fd(80)
lt(90)
fd(80)
lt(90)

# Square 3
penup()
setpos(-110, 0)
pendown()

pencolor("green")

forward(110)
left(90)
forward(110)
lt(90)
fd(110)
lt(90)
fd(110)
lt(90)

# Square 4
penup()
setpos(30, 0)
pendown()

pencolor("red")

forward(130)
left(90)
forward(130)
lt(90)
fd(130)
lt(90)
fd(130)
lt(90)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()
