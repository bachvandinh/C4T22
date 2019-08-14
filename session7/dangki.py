print("DANG KY TAI KHOAN LIEN XO CHAM MY")
name = input("\nHay nhap username? : ")
while True:
    password = input("\n Hay nhap password cua ban: ")
    if len(password) < 8:
        print ("hay nhap lai mat khau")
    elif  password.isalpha():
        print ("mat khau phai co it nhat 1 chu so")
    else:
            break
while True:

    re = input("\n Hay nhap lai mat khau: ")
    if re != password:
        print ("hay nhap lai mat khau")
    else:
        break     
while True:

    email = input("\n Nhap email cua ban: ")
    if "@" and "." in email:
        break 
    else:
        print ("hay nhap lai email")
  
print("BAN DA DANG KY THANH CONG")
print("CHAO MUNG DEN VOI LAUXANH.US")