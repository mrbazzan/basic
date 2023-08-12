import random
from sys import exit

def game(number_one: int, sign: int, number_two: int):
    global STORELIST
    STORELIST = [number_one, sign, number_two]

    signs = {1: "+", 2: "-", 3: "*"}
    try:
        user_answer = int(input("{} {} {} = ".format(number_one, signs.get(sign), number_two)))
    except ValueError:
        print("You should have entered a valid number")
        exit()

    if sign == 1:
        real_answer = number_one + number_two
    elif sign == 2:
        real_answer = number_one - number_two
    elif sign == 3:
        real_answer = number_one * number_two
    else:
        print("Invalid sign")
        exit()

    return user_answer, real_answer

def quiz(user_answer: int, real_answer: int):
    play = "y"
    while play == "y":
        if user_answer == real_answer:
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
            first, second = game(STORELIST[0], STORELIST[1], STORELIST[2])
            quiz(first, second)

def main():
    sign = int(input(
        "Enter the type of quiz: 1. Addition, 2. Subtraction, 3.Multiplication\n"
    ))
    while sign not in [1, 2, 3]:
        sign = int(input(
            "Enter the type of quiz: 1. Addition, 2. Subtraction, 3.Multiplication\n"
        ))
    first, second = game(random.randint(1, 10), sign, random.randint(1, 10))
    quiz(first, second)

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the maths quiz game")
main()
