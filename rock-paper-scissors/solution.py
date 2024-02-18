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
print("Welcome to rock paper and scissors game")
print("")
options = [rock, paper, scissors]
playContinue = 'Y'
userWins = 0
computerWins = 0

while (playContinue == 'Y'):
    userOption = int(input("Enter your option (0 for rock, 1 for paper and 2 for scissors): "))
    computerOption = random.randint(0, 2)

    if (userOption > 2 or userOption < 0):
        print("The entered value is invalid")
        print("")
        continue

    print("User selected:")
    print(options[userOption])
    print("")
    print("Computer selected:")
    print(options[computerOption])
    print("")

    if (userOption == computerOption):
        print("Match drawn")
    elif ((userOption == 2 and computerOption == 0) or (computerOption > userOption)):
        print("Computer won the match")
        computerWins += 1
    else:
        print("User won the match")
        userWins += 1
    
    playContinue = input("Do you want to continuer the game (Y for Yes or N for No)? ")
    print("")

print("Game summary:")
print(f"User won: {userWins} matches")
print(f"Computer won: {computerWins} matches")
if (userWins > computerWins):
    print("User is the overall winner")
elif (userWins < computerWins):
    print("Computer is the overall winner")
else:
    print("Game tied")
