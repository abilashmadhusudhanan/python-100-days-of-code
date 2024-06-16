from turtle import Turtle

class Snake:
    def __init__(self):
        self.pos = [(0, 0), (-20, 0), (-40, 0)]
        self.snakeShape = []

        for snake_pos in self.pos:
            segment = Turtle("square")
            segment.penup()
            segment.goto(snake_pos[0], snake_pos[1])
            self.snakeShape.append(segment)

        self.head = self.snakeShape[0]

    def move(self):
        for i in range((len(self.snakeShape) - 1), 0, -1):
            self.snakeShape[i].goto(self.snakeShape[i - 1].xcor(), self.snakeShape[i - 1].ycor())
        self.snakeShape[0].forward(20)
    
    def up(self):
        if self.snakeShape[0].heading() != 270:
            self.snakeShape[0].setheading(90)
    
    def down(self):
        if self.snakeShape[0].heading() != 90:
            self.snakeShape[0].setheading(270)
    
    def right(self):
        if self.snakeShape[0].heading() != 180:
            self.snakeShape[0].setheading(0)
    
    def left(self):
       if self.snakeShape[0].heading() != 0:
            self.snakeShape[0].setheading(180)

    def grow(self):
        segment = Turtle("square")
        segment.penup()
        lastSegmentPosX = self.snakeShape[len(self.snakeShape) - 1].xcor()
        lastSegmentPosY = self.snakeShape[len(self.snakeShape) - 1].ycor()
        segment.goto((lastSegmentPosX - 20), lastSegmentPosY)
        self.snakeShape.append(segment) 