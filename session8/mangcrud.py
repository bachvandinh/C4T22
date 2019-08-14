print("Chao mung ban den voi chuong trinh")
items =  ['faker', 'anh toi', 'bach s', 'cold tick', 'techies']
n = input("ban muon lam gi (C/R/U/D)?: ")

if n == "c" or n == "C":
    new_item = input("nhap du lieu: ")
    items.append(new_item)
    print(*items, sep = ' ,')
elif n == "r" or n == "R": 
    for i, item in enumerate(items):
        print(i+1, items[i].upper())
            
elif n == "u" or n == "U":
    k = int(input("nhap phan tu ban muon update: "))
    update_item = input("nhap noi dung moi: ")
    items[k] = update_item
                 
    print(*items, sep = ' ,')       
elif n == "d" or n == "D":
    l = int(input(" nhap phan tu ban muon xoa: "))    
    items.pop(l)
        
    print(*items, sep = ' ,')
else:
    print("khong hop le, hay thu lai")        


