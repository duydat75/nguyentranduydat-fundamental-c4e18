
name = input ("Your full name: ").lower()
mylist = ' '.join(name.split())
alist = list(mylist)
alist[0]=chr(ord(alist[0])-32)
for i in range (len(alist)):
    if alist[i] == " ":
        alist[i+1]=chr(ord(alist[i+1])-32)
print ("".join(alist))