numb =input ("Enter sq of number: ")
mylist = numb.strip().split(" ")
numbers = []
alist=[]
softed = True
for item in mylist:
    numbers.append(int(item))
for i in range (len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        softed=False
        for i in range (len(numbers)):
            minn = min(mylist)
            dat=mylist.index(minn)
            alist.append(minn)
            del mylist[dat]
        
if softed:
    print ("Da duoc sap xep:\n", numbers)
else:
    print ("Chua duoc sap xep")
    print (alist)