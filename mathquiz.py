import random
from sys import exit


name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the maths quiz game")


def randomNum():
    numberOne = random.randint(1, 10)
    numberTwo = random.randint(1, 10)
    return numberOne, numberTwo


def game(numberOne, numberTwo):

    global STORELIST
    STORELIST = [numberOne, numberTwo]

    realAnswer = numberOne + numberTwo

    userAnswer = int(input("{} + {} = ".format(numberOne, numberTwo)))
    return userAnswer, realAnswer


def quiz(userAnswer, realAnswer):
    play = "y"
    while play == "y":
        if userAnswer == realAnswer:
            print("GOOD JOB!")
            choice = input("Do you want to continue? (y/n) ").lower()
            while choice not in ['y', 'n']:
                choice = input("Do you want to continue? (y/n) ").lower()
            if choice == 'y':
                main()
            else:
                print("BYE BYE!!!")
                exit()
        else:
            print("Try Again")
            answer1, answer2 = game(STORELIST[0], STORELIST[1])
            quiz(answer1, answer2)


def main():
    random1, random2 = randomNum()
    val1, val2 = game(random1, random2)
    quiz(val1, val2)


main()
