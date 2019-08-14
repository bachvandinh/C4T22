items = ['ak47', 'm4a4', 'awp']
print(items)
new_item = input("nhap do: ")
items.append(new_item)
print(*items, sep=' ,')
print(items)