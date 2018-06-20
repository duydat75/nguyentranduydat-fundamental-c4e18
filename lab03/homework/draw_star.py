from turtle import *

shape("classic")
def draw_star(x,y,length):
    penup()
    setpos(x,y)
    pendown()
    for i in range (5):
        forward (length)
        right (144)
   
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)