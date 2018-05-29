fav = ['a','b','c','d']
for index, item in enumerate(fav):
    print("{0}. {1}".format(index+1,item))
possition = int(input("Nhap stt ban muon thay the: "))
update_fav= input("Nhap phan tu ban muon thay the: ")
fav[possition-1] = update_fav
print (fav)

