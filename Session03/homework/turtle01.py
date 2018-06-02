from turtle import *
shape("classic")
speed(5)
colors = ['red','blue','brown','yellow','gray']
for i in range (3,8):
    color (colors[i-3])
    for j in range (i):
        forward (120)
        left (360/i)
mainloop()