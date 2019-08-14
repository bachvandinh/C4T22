items = ['com', 'chao', 'pho', 'thit cho']
while True:
    n = input("nhap gia tri can xoa: ")
    if n == "com" or "chao" or "pho" or "thit cho":
    # if n == items:
        items.remove(n)
        break
    else:
        print("hay nhap lai")
        
print(*items, sep= ' ,')        