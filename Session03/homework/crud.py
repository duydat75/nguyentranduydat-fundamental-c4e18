word="CRUD"
print(*list(word),sep=', ')
items =['T-Shirt', 'Sweater']
for i in range (4):
    choice = input("What do you want: ")
    if choice == "R":
        print ("Out items: ",*items, sep=', ')
    if choice == "C":
        new = input("Enter new item: ")
        items.append(new)
        print ("Out items: ",*items,sep=', ')    
    elif choice == "U":
        position = int(input ("Update position: "))
        update_item = input("New item ? ")
        items[position-1]=update_item
        print (*items, sep=', ')
    elif choice == "D":
        delete = int(input("Delete position ? "))
        del items[delete-1]
        print (*items, sep=', ')