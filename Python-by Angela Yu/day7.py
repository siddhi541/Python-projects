import random
import stages

print(stages.logo_hangman)

while True:
    rand_word = ''.join(random.sample(stages.word_list , 1))
    # print(rand_word)
    rand_space = []
    for i in rand_word:
        rand_space.append("_")

    print(' '.join(rand_space))
    idx = 1
    while "_" in rand_space:
        guess_letter = input("Guess letter: ")
        stage_idx = len(stages.stages)
        flag = 1
        for i in range(0,len(rand_word)):
            if rand_word[i] == guess_letter:
                rand_space[i] = ""
                rand_space[i] = rand_word[i]
                flag = 0
            
        print(' '.join(rand_space))

        if flag == 1:
            print(f"you chose {guess_letter}, it is not in the word, you lose a life.")
            idx += 1
            print(stages.stages[len(stages.stages)-idx])
            if idx == len(stages.stages):
                print("You lost")
                break
            
        elif flag == 0:
            print("Right guess!")
            print(stages.stages[len(stages.stages)-idx])
            if "_" not in rand_space:
                print("You won!")
    
    choice = input("Want to play again? Y or N :")
    if choice == 'N' or choice == 'n':
        break




