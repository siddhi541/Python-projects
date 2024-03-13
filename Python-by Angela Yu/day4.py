# stone paper scissors
import random
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
game = [rock, paper, scissors]
while(1):
    userSide = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:"))
    compSide = random.randint(0,2)

    print(userSide, compSide)
    if userSide >= len(game):
        print("Wrong input")
    else:
        print("You chose:")
        print(game[userSide])
        print("Computer chose:")
        print(game[compSide])

        if userSide == compSide:
            print("Match draw.")
        elif userSide == 0 and compSide == 1:
            print("You lose")
        elif userSide == 0 and compSide == 2:
            print("You win.")
        elif userSide == 1 and compSide == 0:
            print("You win.")
        elif userSide == 1 and compSide == 2:
            print("You lose.")
        elif userSide == 2 and compSide == 0:
            print("You lose.")
        elif userSide == 2 and compSide == 1:
            print("You win.")

        cont = input("Want to play again? Y or N : ")
        if cont == 'N':
            break