
def enter_game():
    print("""You enter a room with 2 doors.
Do you go through door #1 or door #2.""")

    door = input("Enter selection here> ")

    if door == "1":
        print("There's a bear eating cake.")
        print("What do you do?")
        print("1. Take the cake.")
        print("2. Scream at the bear.")
        print("3. Wait patiently.")

        bear = input("> ")

        if bear == "1":
            print("The bear eats your face off. You ded!")
            play_again()
        elif bear == "2":
            print("The bear shouts and attacks you. Fatality!")
            play_again()
        else:
            print(f"Well, doing {bear} saved you.")
            print("Bear runs away. You survived! Congrats!")
            play_again()


    elif door == "2":
        print("There's 3 things visible.")
        print("1. Cranberry")
        print("2. iPod.")
        print("3. Dark movie.")

        move = input("> ")

        if move == "1" or move == "2":
            print("Jello/Music gives you super power.")
            print("Mission accomplished!")
            play_again()
        else:
            print("You fall into an abyss.")
            print("Fatality.")
            play_again()

    else:
        print("You didn't follow the orders, you stumble and die.")
        print("Fatality. Good bye!")
        play_again()


def play_again():
    print("Would you like to play again?")
    again = input("Y/N> ")

    if again == "Y" or again == "y":
        enter_game()
    else: 
        print("Thanks for playing! Hope to see you again :)")
        print("Game by Sasha.")



print("Hey! Welcome to Text Adventure game by Sushan.")
print("Let's play shall we?")

play = input("Y/N> ")

if play == "Y" or play == "y":
    enter_game()
elif play == "N" or play == "n":
    print("Thanks for your time! Hope to see you again :)")
    print("Game by Sasha.")
else:
    print("Error with input, I assume you would like to play.")
    enter_game()