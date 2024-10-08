from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)

    def move_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
