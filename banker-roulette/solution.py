import random

friends = input("Enter the names of the friends separated by comma: ").split(',')
no_of_friends = len(friends)

print(f"{friends[random.randint(0, (no_of_friends - 1))]} is going to pay for the meal today")