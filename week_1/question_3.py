"""
Name: question_3.py

Description:

Draw squares.

Author:

Date:

Note: Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name

"""

from turtle import *

speed(0)


# Function to draw a square

def draw_square(side_length):
    
    for _ in range(4):
        fd(side_length)
        lt(90)


# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw square
draw_square(50)

# Square 2
penup()
setpos(-220, 0)
pendown()
pencolor("blue")
draw_square(80)

# Square 3
penup()
setpos(-110, 0)
pendown()
pencolor("green")
draw_square(110)

# Square 4
penup()
setpos(30, 0)
pendown()
pencolor("red")
draw_square(130)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
