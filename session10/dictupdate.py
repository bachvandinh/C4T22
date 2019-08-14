item = {
    "name": "Ronaldo",
    "age": "32",
    "land": "portugal",
    "club": "mu",
}
# age = int(input("nhap tuoi: "))
# club = input("nhap clb: ")
# item['age'] = age #cap nhat du lieu vao dict
# item['club'] = club

update = input("nhap phan tu ban muon cap nhat: ")
dl = input("nhap du lieu: ")
item[update] = dl

print(item)

print(item == {})