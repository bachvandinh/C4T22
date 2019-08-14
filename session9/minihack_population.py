thanhpho = ['pochinki', 'mylta', 'gatka', 'bootcamp', 'ha tinh']
sodan = [1000, 3243, 4521, 3324, 5354]
# area = [1231, 1244, 1243, 4362, 1354]
# for thanhpho, i in enumerate(sodan):
#         print (thanhpho, i)
for index, i in enumerate(sodan):
    # sst, giatri
    print(thanhpho[index], i)
    
print("So dan lon nhat: ", max(sodan))
print("So dan nho nhat: ", min(sodan))

print("-----------")

a = max(sodan)
vitri = 0
for i in range(len(sodan)):
    if sodan[i] == a:
        print(i)
        vitri = i

print(thanhpho[vitri])
# for index, i in enumerate(thanhpho):
#     # sst, giatri
#     print(index, i)