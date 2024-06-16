from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scorecard
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.grow()
        food.move()
        scorecard.increament()

    if snake.head.xcor() < -340 or snake.head.xcor() > 340 or snake.head.ycor() < -340 or snake.head.xcor() > 340:
        scorecard.gameover()
        break

    for segment in snake.snakeShape:
        if segment != snake.head:
            if snake.head.distance(segment) < 15:
                scorecard.gameover()
                break

screen.exitonclick()