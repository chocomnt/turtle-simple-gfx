from turtle import *
import colorsys

t = Turtle()
t.speed(0)
t.pensize(1)
n = 70
h = 0

bgcolor("black")

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, .8)
    h += 1/n
    t.color(c)
    t.left(1)
    t.forward(1)

    for i in range(2):
        t.left(2)
        t.circle(100)

hideturtle()
tracer(False)
exitonclick()