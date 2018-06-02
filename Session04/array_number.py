numb =input ("Enter sq of number: ")
mylist = numb.strip().split(" ")
numbers = []
for item in mylist:
    numbers.append(int(item))
print (numbers)