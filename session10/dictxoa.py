item = {
    "name": "Ronaldo",
    "age": "32",
    "land": "portugal",
    "club": "mu",
}

key = input("nhap key muon xoa: ")
del item[key]
#del item['age']
print(item)

print(item == {})