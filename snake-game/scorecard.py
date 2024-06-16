from turtle import Turtle

class Scorecard:
    def __init__(self):
        self.scorecard = Turtle()
        self.scorecard.hideturtle()
        self.scorecard.penup()
        self.scorecard.goto(0, 300)
        self.score = 0
        self.update(f"score: {self.score}")

    def update(self, text):
        self.scorecard.write(text, False, "center", ("Arial", 20, "normal"))

    def increament(self):
        self.scorecard.clear()
        self.score += 1
        self.update(f"score: {self.score}")
    
    def gameover(self):
        self.scorecard.goto(0, 0)
        self.update("GAME OVER")