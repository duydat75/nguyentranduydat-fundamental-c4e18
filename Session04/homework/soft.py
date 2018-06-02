mylist = [5,4,3,2,1,9,8,7,6]
alist = []
for i in range (len(mylist)):
    minn = min(mylist)
    dat=mylist.index(minn)
    alist.append(minn)
    del mylist[dat]
print (alist)