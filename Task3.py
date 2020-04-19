import random


# Function for Easy level
def easy_level():
    print("WELCOME TO EASY LEVEL.\nGUESS THE HIDDEN NUMBER(Hint: from 1 to 10)")
    hidden_numb = random.randint(1, 10)
    chances = 6

    while chances >= 0:

        guess = input("\nENTER YOUR GUESS\n> ").upper()

        if int(guess) == hidden_numb:
            print(" YOU GOT IT !")
            play_again = input("DO YOU WANT TO PLAY AGAIN ? (NO/YES) ").upper()
            if play_again == "YES":
                easy_level()
                break
            elif play_again == "NO":

                break
        elif guess != hidden_numb:
            print("THAT WAS WRONG!")
            chances -= 1
            if chances == 0:
                break
            print(f"TRY AGAIN, YOU HAVE {chances} CHANCES LEFT")


# Function for Medium Level
def medium_level():
    print("WELCOME TO MEDIUM LEVEL.\nGUESS THE HIDDEN NUMBER(Hint: from 1 to 20)")
    hidden_numb = random.randint(1, 20)
    chances = 4

    while chances >= 0:

        guess = input("\nENTER YOUR GUESS\n> ").upper()

        if int(guess) == hidden_numb:
            print(" YOU GOT IT !")
            play_again = input("DO YOU WANT TO PLAY AGAIN ? (NO/YES) ").upper()
            if play_again == "YES":
                medium_level()
                break
            elif play_again == "NO":

                break
        elif guess != hidden_numb:
            print("THAT WAS WRONG!")
            chances -= 1
            if chances == 0:
                break
            print(f"TRY AGAIN, YOU HAVE {chances} CHANCES LEFT")


# Function for Hard Level
def hard_level():
    print("WELCOME TO HARD LEVEL.\nGUESS THE HIDDEN NUMBER(Hint: from 1 to 50)")
    hidden_numb = random.randint(1, 50)
    chances = 3

    while chances >= 0:

        guess = input("\nENTER YOUR GUESS\n> ").upper()

        if int(guess) == hidden_numb:
            print(" YOU GOT IT !")
            play_again = input("DO YOU WANT TO PLAY AGAIN ? (NO/YES) ").upper()
            if play_again == "YES":
                hard_level()
                break
            elif play_again == "NO":

                break
        elif guess != hidden_numb:
            print("THAT WAS WRONG!")
            chances -= 1
            if chances == 0:
                break
            print(f"TRY AGAIN, YOU HAVE {chances} CHANCES LEFT")


# Main Program
print("WELCOME TO NUMBER GUESSING GAME\n\nTHERE ARE 3 LEVELS  IN THIS GAME (EASY, MEDIUM AND HARD)")
level = input("PLEASE ENTER THE LEVEL YOU WANT TO START WITH \n>").upper()

if level == "EASY":
    easy_level()
    print("GAME OVER!")
elif level == "MEDIUM":
    medium_level()
    print("GAME OVER!")
elif level == "HARD":
    hard_level()
    print("GAME OVER!")
else:
    print("INVALID INPUT")
    print("GAME OVER!")