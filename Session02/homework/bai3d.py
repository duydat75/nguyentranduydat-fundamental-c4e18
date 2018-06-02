for i in range(10):
    string = ""
    for j in range(10):
        value = str(j % 2)
        string += " " + value + " "
    if(i % 2 == 1):
        string = string[::-1]
    print (string)       
n =int (input("Input n: "))
for i in range(n):
    string = ""
    for j in range(n):
        value = str(j % 2)
        string += " " + value + " "
    if(i % 2 == 1):
        string = string[::-1]
    print (string)
