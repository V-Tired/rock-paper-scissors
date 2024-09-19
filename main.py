import random

"""Simple console-based rock paper scissors."""


question = True
while question:
    player_choice = input("Rock, paper, scissors, shoot!\n").lower()
    if player_choice == "rock":
        player_num = 0
        break
    elif player_choice == "paper":
        player_num = 1
        break
    elif player_choice == "scissors":
        player_num = 2
        break
    else:
        continue

print(f"You chose {player_choice}.")

computer = random.randint(0, 2)

if computer == 0:
    computer_choice = "rock"
if computer == 1:
    computer_choice = "paper"
if computer == 2:
    computer_choice = "scissors"

print(f"Computer chose {computer_choice}. ")

list_1 = [1, 2, 3]
list_2 = [3, 1, 2]
list_3 = [2, 3, 1]

joined_list = (list_1, list_2, list_3)

decision = joined_list[computer][player_num]


if decision == 1:
    print("It's a tie.")
if decision == 2:
    print("You win!")
if decision == 3:
    print("You lose.")
