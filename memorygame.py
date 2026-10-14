import random
import time
import msvcrt
import os


def generate_string(level):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    secret = ""
    for i in range(level + 3):
        secret = secret + random.choice(letters)
    return secret


def clear_screen():
    os.system("cls")


def countdown():
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)


def play_game():
    level = 1
    levels_completed = 0
    while True:
        secret = generate_string(level)
        print("Level:", level)
        print(secret, end="", flush=True)
        countdown()
        clear_screen()
        while msvcrt.kbhit():
            msvcrt.getwch()
        guess = input("Enter the string you just saw (case insensitive): ")
        if guess.upper() != secret:
            return secret, guess, levels_completed
        print("Good job!")
        levels_completed = levels_completed + 1
        level = level + 1
        time.sleep(3)
        clear_screen()


start = input("Press Q to quit or anything else to start the game: ")

while start.upper() != "Q":
    secret, guess, levels_completed = play_game()

    print("Incorrect!")
    print("Correct string:", secret)
    print("Your guess:", guess)
    print("Levels completed:", levels_completed)

    if levels_completed <= 2:
        print("Wow, did you understand the game?")
    elif levels_completed <= 6:
        print("Not bad, keep working at it")
    else:
        print("Nice Job! You're a memory master!")

    answer = input("Would you like to play again? (Y/N): ")
    while answer.upper() != "Y" and answer.upper() != "N":
        answer = input("Please enter Y or N: ")

    if answer.upper() == "N":
        break

    start = "anything"

print("have a great day")