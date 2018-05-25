username = input ("Username: ")
if username != ("c4e"):
    print("Khong co user")
elif username == ("c4e"):
    password = input ("Password", show=" ")
    if password != ("123456"):
        print ("Sai mat khau")
    elif password == ("123456"):
        print ("Hello")
