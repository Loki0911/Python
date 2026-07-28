import random
import time

def winGame(comp, you):
    if comp == you:
        return None
    elif comp == "S":
        if you == "R":
            return True
        elif you == "P":
            return False
    elif comp == "P":
        if you == "S":
            return True
        elif you == "R":
            return False
    elif comp == "R":
        if you == "P":
            return True
        elif you == "S":
            return False

keep_playing = True
while keep_playing:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        comp = "S"
    elif randomNumber == 2:
        comp = "P"
    elif randomNumber == 3:
        comp = "R"

    while True:
        you = input("Your Turn: Sissor(S), Paper(P) or Rock(R): ").upper()
        if you in ["S", "P", "R"]:
            break
        else:
            print("Error: Invalid Input! Please enter S for Sissor, P for Paper, or R for Rock")

    result = winGame(comp, you)
    time.sleep(0.5)
    print(f"Computer Said: {comp}")
    print(f"You Said: {you}")
    if result is None:
        print("Tie")
    elif result:
        print("You Won!...")
    else:
        print("You Loose!....")
    time.sleep(0.5)

    while True:
        play_again = input("Do you want to play again [Y/N]: ").upper()
        if play_again in ["Y", "N"]:
            break
        else:
            print("Error: Invalid Input! Please enter Y for Yes or N for No")

    if play_again == "N":
        print("Exiting........")
        keep_playing = False
    elif play_again == "Y":
        print("Starting a new game...")
        continue