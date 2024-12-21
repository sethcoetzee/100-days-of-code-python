# Day 4 Project - Rock, Paper, Scissors Game

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

# human choice 

if choice == "0":
    print(f"You chose: {images[0]}\n")
elif choice == "1":
    print(f"You chose: {images[1]}\n")
elif choice == "2":
    print(f"You chose: {images[2]}\n")
else:
    print("Invalid choice. You lose by forfeit.")
    exit()

# computer choice

import random
computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f"The computer chose: {images[0]}\n")
elif computer_choice == 1:
    print(f"The computer chose: {images[1]}\n")
elif computer_choice == 2:
    print(f"The computer chose: {images[2]}\n") 

# game logic

if (choice == "0" and computer_choice == 2) or (choice == "1" and computer_choice == 0) or (choice == "2" and computer_choice == 1):
    print("You win!")

elif (choice == "0" and computer_choice == 1) or (choice == "1" and computer_choice == 2) or (choice == "2" and computer_choice == 0):
    print("You lose!")
    
else:
    print("It's a draw!")