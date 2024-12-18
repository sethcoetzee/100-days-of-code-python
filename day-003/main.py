print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a cross road. Where do you want to go?\n   Type 'left' or right'\n").lower()

if choice == "left":
    choice = input("You've come to a lake. There is an island in the middle of the lake.\n   Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    
    if choice == "wait":
        choice = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow, and one blue. Which colour do you choose?\n").lower()
        
        if choice == "yellow":
            print("You found the treasure! You're now rich beyond your wildest dreams. You Win!")
        
        elif choice == "blue":
            print("You enter a room full of hungry beasts. They devour you. Game over :( ")
        
        elif choice == "red":
            print("It's a room full of blazing fire. You burn to a crisp. Game over :( ")
        
        else:
            print("Your inability to pay attention to details cost you your life this time. You lose. Game over :( ")
    
    else:
        print("You get attacked by trout. Game over :( ")
    
else:
    print("You fell into a hole. Game over :( ")