string = input("Enter the string: ")
alist =list(string)
count=[[x,alist.count(x)] for x in set(alist)]
mylist = sorted(count)
for items in mylist:
    for item in items:
        print (item,end=' ',sep=' ')
    print ()