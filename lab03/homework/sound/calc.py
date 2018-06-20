from random import randint, choice

def add(x, y): # no arguments
    print(x + y)

def evaluate(x, y, op):
    result = 0
    if op == "+":
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    else:
        result = x / y
    return result

# print(__name__)
