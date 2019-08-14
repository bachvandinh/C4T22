person_list = []

p1 = {
    'name': 'Huy',
    'job': 'waiter',
    'hour': 12,
    'salary per hour': 0.8,
}

p2 = {
    'name': 'Tung',
    'job': 'cook',
    'hour': 24,
    'salary per hour': 1.5,

}

p3 = {
    'name': 'M. Duc',
    'job': 'accountant',
    'hour': 20,
    'salary per hour': 2,
}

person_list.append(p1)
person_list.append(p2)
person_list.append(p3)

p4 = {
    'name': 'Don',
    'job': 'waiter',
    'hour': 12,
    'salary per hour': 0.9,
}

p5 = {
    'name': 'H. Duc',
    'job': 'waiter',
    'hour': 14,
    'salary per hour': 0.7,
}


person_list.append(p4)
person_list.append(p5)

person_list[0] = {
    'name': 'Huyen',
    'job': 'waitress',
    'hour': 14,
    'salary per hour': 1,
}
total = 0
# person_list.pop(4)
# print(person_list)
for index, item in enumerate(person_list):
    # print(index+1, item)
    print(index+1, item["hour"]) #item la cuc dict luon nen ta dung ngoac vuong de chi gia tri cua dict
    tieng = item["hour"]
    salary = item["salary per hour"]
    tong = tieng*salary
    print(index+1, tong)
    total += tong
print("cong ty phai tra: ", total) 


    






# p2 = person_list[2]
# print(p3)

# print(person_list)