
name = input ("Your full name: ").lower()
mylist = ' '.join(name.split())
alist = list(mylist)
for i in range (len(alist)):
    if alist[i] == " ":
        alist[i+1]=alist[i+1].upper()
alist[0]=alist[0].upper()
print ("".join(alist))