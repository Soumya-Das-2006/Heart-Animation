import math
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("black")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed
pen.color("red")

# Function to define the heart shape
def heart(t):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

# Draw the heart pattern
pen.penup()
for i in range(10):  # Reduce the number of layers for faster rendering
    pen.goto(0, 0)  # Reset position
    pen.pendown()
    for t in range(0, 100, 2):  # Increase the step size to reduce points
        x, y = heart(t / 10)
        pen.goto(x * i, y * i)
    pen.penup()

# Hide the turtle and keep the window open
pen.hideturtle()
turtle.done()