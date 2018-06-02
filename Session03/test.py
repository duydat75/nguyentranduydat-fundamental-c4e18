flock = [5,7,300,90,24,50,75]
print ("Hello my name is Hiep and here is my flock: \n",flock)
size_max = 0
a=0
total = 0
size_max = max(flock)
update = flock.index(size_max)
flock[update]=8
print ("Now my biggest sheep size", size_max,"let's shear it")
print (flock)
for i in range (3):
    for j in range (len(flock)):
        flock[j]+=50
        if i == 2:
            total += flock[j]
    print ("\nMonth",i+1,":")
    print ("One month has passed, now here is my flock: \n",flock)
    while i < 2:
        size_max = max(flock)
        update = flock.index(size_max)
        flock[update]=8
        print ("Now my biggest sheep size", size_max,"let's shear it","\nAfter shearing here is my flock: ")
        print (flock)
        break
print ("My flock has size inc total:",total)
print ("I would get", total,"* 2$ =",total*2, "$")