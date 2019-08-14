laptop = {
    'hp': 20,
    'dell': 50,
    'macbook': 12,
    'asus': 30,
}


laptop.update({'toshiba': 20})
laptop.update({'fujitsu': 15})
laptop.update({'alienware': 5})

laptop_price = {
    'hp': 600,
    'dell': 650,
    'macbook': 12000,
    'asus': 400,
    'toshiba': 600,
    'fujitsu': 900,
    'alienware': 1000,
    }    
# print(laptop)
# key = input("Enter the key: ")
# print(laptop[key])

# update = input("nhap phan tu ban muon cap nhat: ")
# dl = input("nhap du lieu: ")
# laptop[update] = dl
# print(laptop)

total = sum(laptop.values())
print(total)
for i, k in laptop.items():
    print(i, k, sep= ": ")

# print(laptop_price['asus'])
# key1 = input("Enter the key: ")
# print(laptop_price[key1])

laptop.update({'dell': 10, 'macbook': 2})
for i, k in laptop.items():
    print(i, k)

a = input("enter the computer: ")
b = int(input("enter number of Computers: "))
tong = laptop_price[a] * b
print("total money: ", tong)


