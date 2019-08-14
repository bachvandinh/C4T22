while True:

    cau = input("nhap cau cua ban: ")
    if not cau.isalpha():
        print ("invalid")
    else:    
        print (cau.upper())
        break    