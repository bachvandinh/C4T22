thanhpho = ['pochinki', 'mylta', 'gatka', 'bootcamp', 'ha tinh']
sodan = [1000, 3243, 4521, 3324, 5354]
area = [1231, 1244, 1243, 4362, 1354]
count = 0
tp = 0
for index, i in enumerate(sodan):
    # res = [i / j for i, j in zip(sodan, area)] #chia trong mang dung res
    # print(thanhpho[index], i, round(res[index], 4)) #in ra va lam tron
    print (area[index], i)
    check = i / area[index]
    count += check
    tp +=1

total = check / tp 
print("tb la: ", round(total, 4))