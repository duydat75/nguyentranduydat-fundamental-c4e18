from random import *
from is_inside import is_inside


dat_text = ''
dat_color = ''

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text = choice(['red','blue','green','yellow'])
    color = choice(['#C62828','#3F51B5','#4CAF50','#FFD600'])
    quiz_type = randint (0,1) #0 meaning, 1 color
    return [text,color,quiz_type] 

def mouse_press(x, y, text, color, quiz_type):

    for shape in shapes:
        if is_inside([x,y],shape['rect']):
            dat_text = shape['text']
            dat_color = shape['color']
    if quiz_type == 0 :
        if dat_text == text:
            return True
        else:
            return False
    if quiz_type == 1 :
        if dat_color == color:
            return True
        else:
            return False



    
    return True
