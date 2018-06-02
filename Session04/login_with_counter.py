count = 0
while True:
    username= input("Username: ")
    if username == "c4e":
        password = input("Password:")
        if password == "1":
            print ("Wellcome")
            break
        else :
            print("Wrong password")
    else :
        print("No such user")  
    count += 1
    if count ==3 :
        print ("Go away")
        break