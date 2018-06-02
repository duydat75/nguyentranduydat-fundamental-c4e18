flock= [1,2,3,4,5,6,7]
size_max=max(flock)
update = flock.index(size_max)
flock[update] = 10
print (flock)
for j in range (3):
    for i in range (len(flock)):
        flock[i]+=50
    print ("Month", j+1)
    print (flock)
    while j < 2:
        size_max = max(flock)
        update = flock.index(size_max)
        flock[update]= 10
        print (flock,"\nAfter :")   
        break