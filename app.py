print("tests")
import turtle
from turtle import *
t = Turtle()
t.speed(99)
t.shape('turtle')

sidelength = 100
rotate=144

def square(sidelength, rotate):
    for i in range(5):
        t.forward(sidelength)
        t.left(rotate)

def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, rotate)
        length += 5
        t.right(5)
doubleSquares(60)
