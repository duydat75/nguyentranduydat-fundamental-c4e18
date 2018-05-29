from random import randint
count = 0
numb = randint(0,100)
print (numb)
while count < 7: 
    n = int(input("Nhap so n :"))
    if n < numb:
        print ("Too small")
    elif n > numb:
        print ("Too big")
    elif n == numb:
        print ("Bingo")
        count = 7
    count +=1
    