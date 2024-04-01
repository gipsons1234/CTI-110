#Steven Gipson

#4-1-2024

#P4Lab1A

#This program has me using turtle graphics to draw a square and triagnle using loops




import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.left(90)

# Move the turtle to a new position for drawing the triangle
t.penup()
t.goto(-50, -50)
t.pendown()

# Draw a triangle
for _ in range(3):
    t.forward(100)
    t.left(120)

# Keep the window open until it's manually closed
turtle.done()
