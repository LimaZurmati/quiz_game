print("Wellcome to quiz game !!")


questions = ("What is another word for 'capability'? ",
             "What is the synonym of the word 'suitable'? ",
             "Find the word which has the same meaning as'attention'? ",
             "What is another word which means the same as 'intelligent'? ",
             "Choose the word which means the opposite of 'beautiful'? ")

options = (("A.abilty","B.disability","C.weak","D.strong"),
           ("A.qualified","B.prope","C.A and b","D.none"),
           ("A.care","B.careless","C.notice","D.A and B"),
           ("A.smart","B.clever","C.lazy","D.A and C"),
           ("A.ugly","B.pretty","C.handsome","D.none"))

answers = ("A","C","D","B")
gusses = []
score = 0
question_num = 0

for question in questions:
    print("*********************************")
    print("---------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A,B,C,D):").upper()
    gusses.append(guess)

    if guess == answers[question_num]:
       score += 1
       print('Correct! you got 1 point')
    else:
       print("Incorrect!")
       print(f"{answers[question_num]} is the correct answer!")

    question_num += 1

