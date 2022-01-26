from turtle import *
import math


uppercase = (50, 100)
lowercase = (40, 80)
kerning = 20


mode("logo")
pensize(10)
hideturtle()



def a(dim):
    width, height = dim
    p = pos()
    pendown()
    goto(p + (width/2, height))
    goto(p + (width, 0))
    penup()
    goto(p + (width/4, height/2))
    pendown()
    goto(p + (width*3/4, height/2))
    penup()
    goto(p + (width, 0))

def i(dim):
    width, height = dim
    p = pos()
    penup()
    goto(p + ( width*(1/5)  , height ) )
    pendown()
    goto(p + ( width*(4/5)  , height ) )
    goto(p + ( width/2      , height ) )
    goto(p + ( width/2      , 0      ) )
    goto(p + ( width*(1/5)  , 0      ) )
    goto(p + ( width*(4/5)  , 0      ) )
    penup()
    goto(p + (width, 0))

def d(dim):
    width, height = dim
    p = pos()
    pendown()
    goto(p + ( 0    , height ) )
    right(90)
    circle(-height/2, 180)
    penup()
    goto(p + ( width, 0 ) )

def n(dim):
    width, height = dim
    p = pos()
    pendown()
    goto(p + ( 0, height ) ) 
    goto(p + ( width, 0) )
    goto(p + ( width, height) )
    penup()
    goto(p + ( width, 0) )


def space():
    goto(pos() + (kerning, 0))
    


speed(1)
pencolor("red")

goto(uppercase[0] + 4*lowercase[0] , 0)

a(lowercase)
space()
i(uppercase)
space()
d(lowercase)
space()
a(uppercase)
space()
n(lowercase)


done()