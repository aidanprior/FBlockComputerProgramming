from turtle import *
import math

height, width, kerning = 100, 50, 10

def angledLine(angle, x, y):
    left(angle)
    forward(math.sqrt(x**2 + y**2))


def a():
    angledLine(65, width/2, height)
    angledLine(0, width/2, height)



a()

done()