import os
import stages


print(stages.logo_day9)

while True:
    bidding_dict = {}
    max = 0
    name = ""
    while  True:
        bidder_name = input("What is your name?: ")
        bidding_amount = int(input("What is your bid? $ "))
        # save it to dict
        
        bidding_dict[bidder_name] = bidding_amount
        print(bidding_dict)
        for i in bidding_dict:
            if bidding_dict[i] > max:
                max = bidding_dict[i]
                name = i

        choice = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if(choice == 'yes'):
            os.system('cls')
        else:
            print(f"The winner is {name} with bid amount of ${max}")
            break
    
    ask = input("Want to play again? 'yes' or 'no': ")
    if(ask == 'no'):
        break


