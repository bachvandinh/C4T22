score = [45, 67, 56, 78]
new_high_score = int (input("nhap du lieu: "))
score.append(new_high_score)
score.sort(reverse=True)
print(score)
for i, item in enumerate(score):


    print(i+1, score[i])


new_score = int(input("add score: "))
score.append(new_score)
score.sort(reverse=True)
score.remove(min(score))
print(score)
for i, item in enumerate(score):
    print(i+1, score[i])
