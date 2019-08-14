print("Welcome to the Quiz")
print("How many legs an octopus has:")
print('''1. One leg
2. Two legs
3. Four legs
4. Eight legs''')
n = int(input("Please Write your answer: "))

while True:
    if n == 1:
        print("Correct")
        break
    else:
        print("Wrong answer, Try again")
        n = int(input("Please Write your answer"))


