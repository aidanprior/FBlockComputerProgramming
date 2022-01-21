from turtle import *

penSize = 2
angle = 90
distance = 2



bgcolor("red")
color("blue")
pensize(penSize)
speed(7)


for x in range(1,30):
    # dot(2*penSize)
    forward(x*distance*penSize)
    right(angle)



done()
