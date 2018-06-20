from random import choice

#function arguments / parameters
def calc(x, y, op):
    res = 0

    if op == '+':
        res = x+y
    elif op == '-':
        res = x-y
    elif op == '*':
        res = x*y
    else :
        res = x/y

    #  tra lai ket qua vua tinh
    return res

# print ("Hello world")
# a = 1
# b = 10
# operator = '*'
# # Nhan ket qua vua tinh
# result = calc(a,b,operator)
# print (result)