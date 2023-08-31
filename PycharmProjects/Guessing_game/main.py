#modules
import random

#var
chance = 10
word = ["hi","school","bird","pencil"]
choice = random.choice(word)
name = None
guess = " "
guess_letter = " "


#code
name = input("what is your name? : ")
print("ok let's start it !")

while chance > 0:
    guess = input("what is the letter of the word?: ")
    guess_letter += guess
    wrong = 0


    for i in choice:
        if i in guess_letter:
            print(i)
        else:
            wrong = 1
            print("_")

    if wrong == 0:
        print("congratulation", name, "you have guess all the answer correct!")
        print("the word is : ", choice)
        break

    if guess not in choice:
        chance -= 1
        print("your were wrong")
        print("you have ", chance,"more chance guesses")

        if chance == 0:
            print("sorry you loss u have 0 chance left")