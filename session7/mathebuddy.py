import random

print ("Herzlich Willkommen zu den Mathe-Spiel")
diem = 0
while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    d = random.randint(-1,1)
    #print("d = ",d)
    c = a + b + d
    print(f"{a} + {b}  = {c}  ")

    dapan = input ("nhap dap an cua ban(T/F): ")

    if d == 0:
        if dapan == "T" or dapan == "t":
            print("Dap an Dung")
            diem = diem + 1
            print("\nDiem  cua ban: ", diem)
        else:
            print("Dap an Sai") 
            print("\nGame Over")
            print("\nDiem  cua ban: ", diem)
            break        
    else:
        if dapan == "F" or dapan == "f":
            print("Dap an Dung")
            diem = diem + 1
            print("\nDiem cua ban: ", diem)
        else:
            print("Dap an Sai")
            print("\nGame Over")
            print("\nDiem cua ban: ", diem)
            break
