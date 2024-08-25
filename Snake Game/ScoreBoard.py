from turtle import Turtle

FONT=(["Arial", 24, "normal"])
ALLIGNMENT="center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.getScore()

    def getScore(self):
        Turtle.write(self, arg=f"Score:{self.score}", align=ALLIGNMENT, font=FONT)

    def score_increment(self):
        self.score+=1
        self.clear()
        self.getScore()

    def game_over(self):
        self.goto(0,0)
        Turtle.write(self, arg=f"Game Over! Your score is {self.score}", align=ALLIGNMENT,
                     font=FONT)



