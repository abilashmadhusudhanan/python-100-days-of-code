import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

user_cards = []
computer_cards = []
user_choice = 'y'

user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

while(user_choice == 'y'):
    user_cards.append(deal_card())
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards: {user_cards}, current score {user_score}")
    print(f"Computer's first cards: [{computer_cards[0]}]")

    if(computer_score ==  21):
        print("You lose")
        break
    elif(user_score == 21):
        print("You win")
        break
    else:
        if(user_score > 21):
            if(user_cards.__contains__(11)):
                if((user_score - 10) > 21):
                    print("You lose")
                    break
                else:
                    user_score -= 10
                    user_cards.remove(11)
                    user_cards.append(1)
            else:
                print("You lose")
                break
    
    user_choice = input("Do you want another card('y' for yes or 'n' for no)? ")

if(user_choice == 'n'):
    while(computer_score < 17):
        computer_cards.append(random.choice(deal_card))
        computer_score = sum(computer_cards)

    print(f"Computer cards: {computer_cards}, current score {computer_score}")
    if(computer_score > 21):
        print("You win")
    else:
        if(user_score > computer_score):
            print("You win")
        elif(user_score < computer_score):
            print("You lose")
        else:
            print("Draw")