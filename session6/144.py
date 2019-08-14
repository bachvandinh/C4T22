while True:
    password = input("nhap password: ")
    if len(password) < 8:
        print ("mat khau ngan")
    elif  password.isalpha():
        print ("mat khau phai co it nhat 1 chu so")
    else:
        print("mat khau da nhap dung")
        break