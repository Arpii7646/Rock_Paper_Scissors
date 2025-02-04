# 0 => Rock
# 1 => Paper
# 2 => Scissors
import random
from termcolor import colored
import Art

computer = random.choice([0,1,2])
user_input = input(colored("Enter your choice: ", "blue", attrs =["bold"]))
# user_input = user_input.lower()
user_dict = {"rock" : 0, "paper" : 1, "scissor" : 2}
reverse_dict = {0 : "rock",1 : "paper", 2 : "scissor"}

you = user_dict[user_input]

print(colored(f"You chose: {colored(reverse_dict[you], "red")}\n","yellow", attrs=["bold"]), end = "")
print(colored(f"computer chose: {colored(reverse_dict[computer], "yellow")}", "cyan", attrs=["bold"]))

if(computer == you):
    print(colored("It's a tie!", "red", attrs = ["bold"]))

else:
    if (computer == 0 and you == 1):
        print(colored("YOU WIN!", "red", attrs=["bold"]))
        print(colored("Paper covers Rock..", "green", attrs=["bold"]))

    elif (computer == 0 and you == 2):
        print(colored("YOU LOSE!", "magenta", attrs=["bold"]))
        print(colored("Rock crush the scissor..", "cyan", attrs=["bold"]))

    elif (computer == 1 and you == 0):
        print(colored("YOU LOSE!", "magenta", attrs=["bold"]))
        print(colored("Paper covers Rock..", "cyan", attrs=["bold"]))

    elif (computer == 1 and you == 2):
        print(colored("YOU WIN!", "red", attrs=["bold"]))
        print(colored("Scissor cuts the paper..", "green", attrs=["bold"]))

    elif (computer == 2 and you == 0):
        print(colored("YOU WIN!", "red", attrs=["bold"]))
        print(colored("Rock crush the scissor..", "green", attrs=["bold"]))

    elif (computer == 2 and you == 1):
        print(colored("YOU LOSE!","magenta", attrs=["bold"]))
        print(colored("Scissor cuts the paper..", "cyan", attrs=["bold"]))

    else:
        print("Invalid input")

    