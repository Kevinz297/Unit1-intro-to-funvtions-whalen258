print("tests")
import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

x=5

for i in range(180):
        print(i)
        t.forward(x)
        t.left(120)

turtle.done()