import random
question=[
    {
    "question": 'What color is the sky?',
    "answer_list": ['1. red', '2. green', '3. blue', '4. turqoise'],
    "correct_answer" : 3,
    },
    {
    "question": 'Who is the President of the US?',
    "answer_list": ['1. obama', '2. trump', '3. bush', '4. clinton'],
    "correct_answer" : 2,
    },
    {
    "question": '"Who won the World cup 2018?',
    "answer_list": ['1. france', '2. germany', '3. brazil', '4. vietnam'],
    "correct_answer" : 1,
    }
]

score = 0

while True: 
    ts = random.choice(question)
    print(ts['question'])
    for i in ts['answer_list']:
        print(i)
    user_input = int(input("your answer: "))
    
    if user_input == ts['correct_answer']:
        score += 1
        print("correct! Good Job")
        print("your score: ", score)
    else:
        print("Incorrect")
        print("The Correct answer is: ",ts['correct_answer'])
        break

print("total score is: ", score)            