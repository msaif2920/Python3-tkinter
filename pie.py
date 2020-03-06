import math
import turtle

probability={"a":0.3, "b":0.1, "c":0.2, "d":0.4}


l=turtle.Turtle()

l.circle(90)
l.left(90)
l.penup()
l.goto(45,45)
l.pendown()
for key in probability:

    angle=(360)*probability[key]
    l.right(angle)
    l.forward(45)
    l.back(45)


turtle.done()