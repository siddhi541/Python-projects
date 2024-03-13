print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
while(True):
    LorR = input("Welcome to Tresure Island!\nYour mission is to find the tresure.\nYou are at cross road, where do you want to go? \"left\" or \"right\": ").lower()
    if LorR == "left":
        print("You came to lake. There is an island in the middle of the lake.")
        WorS = input('Type "wait" to wait fir the boat. Type "swim" to swim accross: ').lower()
        if WorS == "wait":
            print("You arrive at the island unharmed.")
            RorYorB = input("There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?: ").lower()
            if RorYorB == "red":
                print("It's a room full of fire. Game over.")
            elif RorYorB == "yellow":
                print("You found the treasure! You win!")
            elif RorYorB == "blue":
                print("You entered room full of beasts. Game over")
            else :
                print("Wrong input")
        elif WorS == "swim":
            print("You get attacked by the hungry trout. Game over.")
        else:
            print("Wrong input")
    elif LorR == "right":
        print("You fell into a hole. Game over.")
    else:
        print("Wrong input")
    cnt = input("Do you want to continue play ? Y or N: ").lower()
    if(cnt == 'n'):
        break
    else:
        continue


