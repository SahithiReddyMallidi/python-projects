from turtle import Turtle

FONT=(["Arial", 24, "normal"])
ALLIGNMENT="center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lscore=0
        self.rscore=0
        self.printScore()

    def l_point(self):
        self.lscore+=1
        self.printScore()

    def r_point(self):
        self.rscore+=1
        self.printScore()

    def printScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.lscore}", align=ALLIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.rscore}", align=ALLIGNMENT, font=FONT)
