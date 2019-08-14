import random
print("\n Welcome to the jumble game ")
item = ('python', 'apple', 'refund', 'telephone', 'computer')
answer = random.choice(item)
string_one = list(answer)
random.shuffle(string_one)
for i in string_one:
    print(i)
print("What's the right word?")

guess = input("What's your answer: ")    
while guess != answer:
    print("You are wrong")
    guess = input("What's your answer: ")    
if guess == answer:
    print("That's right! Good job")     
    exit()
