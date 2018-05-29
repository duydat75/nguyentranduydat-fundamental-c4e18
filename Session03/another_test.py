favs = ["bau","cua","tom","Ca",'Nai','ga']
# print ("Hi there, here your fav things: ", favs)
# print (*favs, sep=', ')
# print ("*"*10)
new_fav= input("Name: ")
favs.append(new_fav)
print (favs)
first_item=favs[2]
print (first_item)
for i in range (len(menu)):
    print ("{0}. {1}".format(i+1,menu[i]))
print ("_"*20)
for index, item in enumerate(menu):
    print("{0}. {1}".format(index+1,item))
print ("_"*20)
for item in menu:
    print (item)
menu[2]="Cua"
print (*menu, sep=", ")