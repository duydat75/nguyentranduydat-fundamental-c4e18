from random import *
import random
from eval import calc

def generate_quiz():
    x = randint(1,10)
    y = randint(1,10)
    ops = ['+','-','*','/']
    op = random.choice(ops)
    res =calc(x,y,op)
    er = random.choice([-1,0,1,0])
    quy = res + er
    return [x, y, op, quy]

def check_answer(x, y, op, dislay_result, user_choice):
    res =calc(x,y,op)
    if dislay_result == res:
        return user_choice
    else :
        return not user_choice