from random import randint, choice
import random
# from eval import cal
import eval

x = randint(1,10)
y = randint(1,10)

ops = ['+','-','*','/']
op = random.choice(ops)

res = eval.calc(x,y,op)

er = random.choice([-1,0,1,0])

quy = res + er

print (x,op,y,'=',quy)

answer = input("y/n ? ")

if er == 0:
    if answer   == 'y':
        count +=1
        print ("bingo")
    elif answer == 'n':
        print ("Sai roi")   
elif er  == -1 or er ==1:
    if answer == 'n':
        count+=1
        print("Bingo")
    elif answer == 'y':
        print ("sai roi")




