flock = [5,7,300,90,24,50,75]
print ("Hello my name is Hiep and here is my flock: \n",flock)
size_max=flock[0]
a=0
total = 0
for i in range (len(flock) - 1):
    if flock[i+1] > size_max:
        size_max= flock [i+1]
        a=i+1
flock[a]= 8
print ("Now my biggest sheep size", size_max,"let's shear it")
print (flock)

for i in range (3):
    for j in range (len(flock)):
        flock[j]+=50
        if i == 2:
            total += flock [j]
    size_max=flock[0]
    a=0
    for q in range (len(flock) - 1):
        if flock[q+1] > size_max:
            size_max= flock [q+1]
            a=q+1
    print ("MONTH", i+1)
    print ("1 month has passed, now here is my flock\n", flock)
    flock[a]= 8     
    print ("Now my biggest sheep size", size_max,"let's shear it","\nAfter shearing here is my flock: ")
    print (flock)   
print ("My flock has size in total: ",total,"\nI would get",total, "* 2$ =", total *2,"$")


