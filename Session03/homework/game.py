from random import *
mylist=['meticulous','champion','hexagon']
word = choice(mylist)
chars = list(word)
shuffle(chars)
print (*chars,sep=' ')
answer= input ("Your answer: ")
if answer == word:
    print ("Hura")
else:
    print (":(")