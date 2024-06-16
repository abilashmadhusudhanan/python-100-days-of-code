from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.listen()

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.onkey(key="w", fun=lambda: turtle.forward(10))
screen.onkey(key="s", fun=lambda: turtle.backward(10))
screen.onkey(key="a", fun=lambda: turtle.left(10))
screen.onkey(key="d", fun=lambda: turtle.right(10))
screen.onkey(key="c", fun=clear)

screen.exitonclick()