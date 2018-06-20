from turtle import *
def draw_square(length,colors):
    shape('classic')
    speed(0)
    color(colors)
    for i in range(4):
        forward(length)
        left(90)

