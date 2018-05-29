from turtle import *
shape("classic")
speed ("3")
colors = ['red', 'blue', 'brown', 'yellow', 'gray']  
for j in range(5):
    color(colors[j])
    begin_fill()
    fillcolor(colors[j])
    for i in range (2):
        forward(50)
        right (90)
        forward (100)
        right (90)
    forward(50)
    end_fill()
        
mainloop()