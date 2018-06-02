numb =input ("Enter sq of number: ")
numbers=list(numb)
balance=''
for i in range (len(numbers)):
    if numbers[0] == "0":
        del numbers[0]
    elif numbers [0] != "0":
        break
for i in range (len(numbers),0,-3):
    numbers.insert(i,",")
del numbers[-1]
numbers.insert(0,"$")
for i in range (len(numbers)):
    balance+= numbers[i]
print (balance)