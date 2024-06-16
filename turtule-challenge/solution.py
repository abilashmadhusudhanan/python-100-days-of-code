from turtle import Turtle, Screen
from random import Random



def random_color():
    
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)

    color = tuple([red, blue, green])

    return color

turtle = Turtle()
screen = Screen()
random = Random()

screen.colormode(255)

for j in range(0, 10):
    turtle.setx(0)
    turtle.sety(j * 20)
    for i in range(0, 10):
        turtle.color(random_color())
        turtle.dot(10)
        turtle.penup()
        turtle.forward(20)
screen.exitonclick()
