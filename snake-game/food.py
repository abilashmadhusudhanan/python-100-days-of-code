from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-320, 320), random.randint(-320, 320))
    
    def move(self):
        self.goto(random.randint(-320, 320), random.randint(-320, 320))