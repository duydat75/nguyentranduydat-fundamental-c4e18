for i in range (10):
    print ("1 0", end=" ")
print()    
n = int(input("Nhap so n "))
if n%2==1:
    for i in range (0,n-1,2):
        print ("1 0", end= " ")
    print("1")      
elif n%2!=1:
    for i in range (0,n,2):
        print ("1 0", end= " ")