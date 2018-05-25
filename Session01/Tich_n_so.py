n = int(input("Nhap so can tinh n: "))
tich = 1
if n == 0:
    print ("0")    
elif n!=0:     
    for i in range (1,n+1):
        tich *= i
    print(tich)    
 