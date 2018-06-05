number = int (input("Enter a number: "))
numbers = [1,6,8,1,2,1,5,6]
count = 0
for numb in numbers:
    if numb == number:
        count += 1
print (number, "appears",count,"times in my list")
    