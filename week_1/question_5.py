"""
Name: question_5.py

Description:

Draw shapes.

Author: Rae Harbird

Date: August 2018

Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name
"""

from turtle import *

speed(0)

# Function to draw a polygon

def draw_n_gon(sides, side_length):
    for _ in range(sides):
        fd(side_length)
        lt(360/sides)
    
# Add your code here


# place the turtle on the left hand side of your canvas
penup()
setpos(-355,0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle
draw_n_gon(3, 30)

penup()
setpos(-300, 0)
pendown()
pencolor("blue")
draw_n_gon(4, 50)

penup()
setpos(-205, 0)
pendown()
pencolor("green")
draw_n_gon(5, 70)

penup()
setpos(-45, 0)
pendown()
pencolor("red")
draw_n_gon(6, 90)

penup()
setpos(170, 0)
pendown()
pencolor("pink")
draw_n_gon(8, 105)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()
