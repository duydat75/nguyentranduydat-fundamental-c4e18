mylist = [1,4,1,64,2,128,5,4,7,31]
print ("Có những cặp số sau có tích bằng 128")
data=[]
for i in  range (len(mylist)):
    if 128 % mylist[i] == 0:
        n = 128/mylist[i]
        data.append(mylist[i])
        if n in mylist and n not in data:
            m= i+1
            print (mylist[i], "và", n, "tại vị trí",m, "và", mylist.index(n)+1)