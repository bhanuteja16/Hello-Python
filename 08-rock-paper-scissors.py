import random

quit = "default"

while quit != "quit":
        num = int(input("Select your option: \n 1) Rock \n 2) Paper \n 3) Scissors \n"))
        if num not in range(1,4):
                print("Invalid option quitting...")
                break

        list = ["Rock" , "Paper" , "Scissors"]
        num2 = random.choice(list)
        print("Your opponent value is " + num2 )

        if num == 1:
                        if num2 == "Rock":
                                print("It's a tie.")
                        elif num2 == "Paper":
                                print(" You have LOST :( ")
                        else:
                                print(" You have WON !!! ")

        elif num == 2:
                        if num2 == "Paper":
                                print("It's a tie.")
                        elif num2 == "Scissors":
                                print(" You have LOST :( ")
                        elif num3 == "Rock":
                                print(" You have WON !!! ")

        elif num == 3:
                        if num2 == "Scissors":
                                print("It's a tie.")
                        elif num2 == "Rock":
                                print(" You have LOST :( ")
                        elif num3 == "Paper":
                                print(" You have WON !!! ")

        quit = input(("type 'quit' to quit the game or any key to restart "))


