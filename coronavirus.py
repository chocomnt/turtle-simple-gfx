from turtle import *
import colorsys

#t = Turtle é a forma simplificada de chamar a turtle
t = Turtle()

#altera a velocidade que a turtle anda
t.speed(10)

bgcolor("black")

b = 200 
h = 0

t.goto(200,0)

while b > 0:
    c = colorsys.hsv_to_rgb(h, 1, .8)
    h += 1
    t.left(b)
    t.forward(b*3)
    t.color(c)
    b -= 1

exitonclick()