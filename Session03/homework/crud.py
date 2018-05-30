word="CRUD"
print(*list(word),sep=', ')
items =['T-Shirt', 'Sweater']
for i in range (4):
    choice = input("What do you want: ")
    if choice in ["r","R"]:
        print ("Out items: ",*items, sep=', ')
    if choice in ["C","c"]:
        new = input("Enter new item: ")
        items.append(new)
        print ("Out items: ",*items,sep=', ')    
    elif choice in ["U","u"]:
        position = int(input ("Update position: "))
        update_item = input("New item ? ")
        items[position-1]=update_item
        print (*items, sep=', ')
    elif choice in ["D","d"]:
        delete = int(input("Delete position ? "))
        del items[delete-1]
        print (*items, sep=', ')