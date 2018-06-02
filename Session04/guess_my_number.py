print ("Now think of a number from 0 to 100")
input()
print (" 'l' if larger than your number\n","'s' if smaller than your number\n","'c' if correct")
low = 0
high = 101
while True:
    numb = (low + high)//2
    print (numb, "Is your number ? ")
    dat = input ("Answer my guess: ")
    if dat == ("c"):
            print("I knew it")
            break
    elif dat == ("s"):
        low = numb
    elif dat == ("l"):
        high = numb
        
   
