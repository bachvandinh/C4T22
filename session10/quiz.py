question_answer=[
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

# print(question_answer[0])
score = 0
bien = 0
percent = 0
# print(len(question_answer))
for bien in range(len(question_answer)):
    print(question_answer[bien]['question'])   
    for i in question_answer[bien]['answer_list']:
        print(i)
    user_input=int(input("What's your answer: "))
    if user_input == question_answer[bien]['correct_answer']:
        score += 1
        print("Correct! Good Job!")
        print("Your score is: ", score)
    else:
        print("Incorrect")
        print("The Correct answer is: ",question_answer[bien]['correct_answer'])   
        print("Your score is: ", score)

percent = (score/len(question_answer))*100
print("You have finish the quiz, Well Done!!!")
print("Your total score is: ", score)   
print("Your percentage is: ", round(percent, 3))
    # print(question_answer[bien])



