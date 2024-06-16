from turtle import Turtle, Screen
from random import Random

screen = Screen()
betted_turtle = screen.textinput("Betting", "Which turtule color will win?")
random = Random()
screen.setup(width=500, height=400)

red = Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.setx(-240)
red.sety(190)

green = Turtle()
green.shape("turtle")
green.color("green")
green.penup()
green.setx(-240)
green.sety(0)

blue = Turtle()
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.setx(-240)
blue.sety(-190)

while True:
    red.forward(random.randint(1, 10))
    green.forward(random.randint(1, 10))
    blue.forward(random.randint(1, 10))

    if red.xcor() >= 250:
        winner = "red"
        break
    elif green.xcor() >= 250:
        winner = "green"
        break
    elif blue.xcor() >= 250:
        winner = "blue"
        break
    else:
        continue

print(f"The winner is {winner}")

if winner == betted_turtle:
    print("You won the bet!")
else:
    print("You lost the bet")

screen.exitonclick()