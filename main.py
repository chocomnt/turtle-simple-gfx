import random
from turtle import *


setup(1000, 1000)

#x são as coordenadas X
#Y são as coordenadas Y
#S é o tamanho da tela
#L é a quantidade de linhas a qual vai gerar 
#mode é definido entre "r" (retas) e "d" (diagonais)
def tiling(x, y, s, l, mode="r"):

    if l == 0:

        if mode == "r":

            if random.random() < .5:

                #linha vertical
                penup()
                goto(x, y-s)
                pendown()
                goto(x, y+s)
                
            else:

                #linha horizontal
                penup()
                goto(x-s, y)
                pendown()
                goto(x+s, y)


        elif mode == "d":

            if random.random() < .5:

                #baixo esquerdo - topo direita
                penup()
                goto(x-s, y-s)
                pendown()
                goto(x+s, y+s)
                
            else:

                #topo esquerdo - baixo direito
                penup()
                goto(x-s, y+s)
                pendown()
                goto(x+s, y-s)

    
    #divide a tela e vai para o proximo nivel(l)
    else:
        s /= 2 
        l -= 1
        tiling(x-s, y+s, s, l, mode)
        tiling(x+s, y+s, s, l, mode)
        tiling(x-s, y-s, s, l, mode)
        tiling(x+s, y-s, s, l, mode)


speed(0)
width(3)
hideturtle()
tiling(0, 0, 400, 4,mode="r")
tracer(True)
exitonclick()