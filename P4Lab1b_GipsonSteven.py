#Steven Gipson

#4-1-2024

#P4Lab1B

#This program has me using turtle graphics to draw my initials

import turtle

# Create a turtle object
t = turtle.Turtle()

# Set pen color and size
t.color("black")
t.pensize(2)


#Drawing an S
t.penup()
t.setpos(-150,100)
t.pendown()

t.forward(30)
t.backward(30)

t.circle(-90,-185)
t.circle(90,-250)

#Drawing a G
t.penup()
t.setpos(100,100)
t.right(270)
t.pendown()

t.circle(-80,-180)
t.right(90)
t.forward(50)

t.right(90)
t.forward(50)










