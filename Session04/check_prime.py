# count =0
# mylist=[0,1,2]
# n = int (input("Nhap so n: "))
# if n in mylist :
#     print ("khong phai so nguyen to")
# else:    
#     for i in range (1,n):
#         if n % i ==0:
#             count +=1
#     if count > 1 :
#         print ("Khong phai so nguyen to:")       
#     if count == 1:
#         print ("So nguyen to")

numb = int(input("Nhap so bat ki: "))
mylist=[0,1,2]
if numb in mylist:
    print ("Khong phai so nguyen to")
for i in range (2,numb):
    if numb % i == 0:
        print ("K phai so nguyen to")
        break
    else:
        print ("So nguyen to")
        break