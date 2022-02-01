import random
counter=0
numberCorrect=0
numberWrong=0
while counter < 10:
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the intger value of {randNumber1} + {randNumber2}?"))
    if correctAnswer==yourAnswer:
        print("Great job, you answered correctly!")
        numberCorrect +=1
    else:
        print("Oops, the correct answer is ",correctAnswer)
    numberWrong +=1
    counter +=1

    if numberWrong > 5:
        print("You really need to see a math tutor!")
        break

print("You answered ", numberCorrect, " questions correctly!")
print("Thanks for playing!")