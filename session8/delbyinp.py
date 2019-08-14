items = ['lol', 'csgo', 'doto']
while True:
    i = int(input("nhap phan tu muon xoa: "))
    if i>2:
        print("again")
    else:
        items.pop(i)
        break
print(*items, sep=' ,')

# items = ['lol', 'csgo', 'doto']
# i = int(input("nhap phan tu muon xoa: "))
# l = len(items)
# for i in range (l):
#   items.pop(i)
#   break
# print(*items, sep=' ,')

#for item in items
    #print(item)

# for i, item in enumerate(items)
#     print(i, item) 