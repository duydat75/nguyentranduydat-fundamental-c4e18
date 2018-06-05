number = int(input("How many B bacterias are there? "))
time = int(input("How much time in minute will we wait? "))
bacterias = number*(2**(time//2))
print ("Bacterias", bacterias)
