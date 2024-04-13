from logo import logo, vs
from data import data
import random

final_score = 0

print(logo)
print("")
option1 = random.choice(data)

while(True):
    data.remove(option1)
    print(f"Compare A: {option1.get('name')} a {option1.get('description')} from {option1.get('country')}")
    print("")
    print(vs)
    print("")
    option2 = random.choice(data)
    print(f"Compare B: {option2.get('name')} a {option2.get('description')} from {option2.get('country')}")
    print("")
    user_choice = input("Who has more followers? Type A or B: ")
    if(user_choice == 'A' and (option2.get('follower_count') > option1.get('follower_count'))):
        print(f"Sorry! that's wrong. Your final score is {final_score}")
        break
    elif(user_choice == 'B' and (option1.get('follower_count') > option2.get('follower_count'))):
        print(f"Sorry! that's wrong. Your final score is {final_score}")
        break
    else:
        final_score += 1
        data.append(option1)
        if(user_choice == 'B'):
            option1 = option2