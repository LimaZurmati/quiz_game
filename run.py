import random

print("Welcome to the quiz game!")

questions = ("What is another word for 'capability'? ",
             "What is the synonym of the word 'suitable'? ",
             "Find the word which has the same meaning as 'attention'? ",
             "What is another word which means the same as 'intelligent'? ")

options = (("A. ability", "B. disability", "C. weak", "D. strong"),
           ("A. qualified", "B. proper", "C. A and B", "D. none"),
           ("A. care", "B. careless", "C. notice", "D. A and B"),
           ("A. smart", "B. clever", "C. lazy", "D. A and C"))

answers = ("A", "C", "D", "B")
guesses = []
score = 0
question_num = 0

randomized_indices = list(range(len(questions)))
random.shuffle(randomized_indices)

for idx in randomized_indices:
    question = questions[idx]
    print("***********")
    print("---------------------------------")
    print(question)

    for option in options[idx]:
        print(option)

    while True:
        guess = input("Enter (A, B, C, D) --->").upper()
        if guess in "ABCD":
            break
        else:
            print('INVALID! Please enter A, B, C, or D')

    guesses.append(guess)

    if guess == answers[idx]:
        score += 1
        print('Correct! You got 1 point')
    else:
        print("Incorrect!")
        print(f"{answers[idx]} is the correct answer!")

# Outcome
print("               Let's see the Outcome (:                  ")
print("---------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Score
try:
    percentage = (score * 100) / len(questions)
except ZeroDivisionError:
    print('0% questions are correct')
else:
    print(f'{percentage}% questions are correct!')
finally:
    print("----------------------------------")
    print("End of the Quiz <3")
    