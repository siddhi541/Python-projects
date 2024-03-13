# random password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while(1):
    letter_count = int(input("How many letters would you like in your password? "))
    symbol_count = int(input("How many symbols would you like? "))
    number_count = int(input("How many numbers would you like?"))

    password = ""
    letter_rand = ''.join(random.sample(letters, letter_count))
    num_rand = ''.join(random.sample(numbers,number_count))
    symbi_rand = ''.join(random.sample(symbols, number_count))
    password+= letter_rand + num_rand + symbi_rand
    
    Final_PW = ''.join(random.sample(password, len(password)))
    print(Final_PW)

    choice= input("Want to generate again ? Y or N ")
    if choice == 'n' or choice == 'N':
        break