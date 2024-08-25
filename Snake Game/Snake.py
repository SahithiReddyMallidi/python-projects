from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_segment(position)

    def add_snake_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("olive")
        new_turtle.penup()
        new_turtle.setpos(position)
        self.snakes.append(new_turtle)

    def extend(self):
        self.add_snake_segment(self.snakes[-1].position())

    def move(self):
        for snake in range(len(self.snakes) - 1,0,-1):
            x = self.snakes[snake-1].xcor()
            y = self.snakes[snake-1].ycor()
            self.snakes[snake].goto(x, y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def goUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def goDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def goLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def goRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
