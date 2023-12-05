print("Wellcome to quiz game !!")
score = 0
question_num = 0

plying = input('Do you want to play ?').lower()

if plying == "yes":
    question_num += 1

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

for question in questions:
    print("*********************************")
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

