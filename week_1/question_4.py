"""
Name: question_4.py

Description:

Draw shapes: triangle, square, pentagon, hexagon, octagon.

Author:

Date:

Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name

"""

from turtle import *

speed(0)


# Function to draw a square

def draw_square(side_length):
    
    for _ in range(4):
        fd(side_length)
        lt(90)

def draw_triangle(side_length):
    for _ in range(3):
        fd(side_length)
        lt(360/3)

def draw_pentagon(side_length):
    for _ in range(5):
        fd(side_length)
        lt(360/5)

def draw_hexagon(side_length):
    for _ in range(6):
        fd(side_length)
        lt(360/6)

def draw_octagon(side_length):
    for _ in range(8):
        fd(side_length)
        lt(360/8)


# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("blue")

# Draw square
draw_square(50)

penup()
setpos(-355, 0)
pendown()
pencolor("dark sea green")
draw_triangle(30)

penup()
setpos(-205, 0)
pendown()
pencolor("green")
draw_pentagon(70)

penup()
setpos(-45, 0)
pendown()
pencolor("red")
draw_hexagon(90)

penup()
setpos(170, 0)
pendown()
pencolor("pink")
draw_octagon(105)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
