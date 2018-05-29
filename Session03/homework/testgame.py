from random import shuffle
word = "champion"
chars = list(word)
shuffle(chars)
print(*chars,sep=' ')
answer= input("Your answer: ")
if answer == word:
    print("Hura")
else:
    print(":(")