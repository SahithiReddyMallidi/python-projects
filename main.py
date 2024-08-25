from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import ScoreBoard
import time


screen=Screen()
screen.title("My Pong Game")
screen.screensize(300,300,"black")
screen.tracer(0)

paddle1=Paddle(-350,0)
paddle2=Paddle(350,0)
screen.update()

screen.listen()
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")
screen.onkey(paddle2.move_up,"w")
screen.onkey(paddle2.move_down,"s")

ball=Ball()
score=ScoreBoard()

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor()>=350 or ball.ycor()<=-350:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(paddle1)<50 or ball.distance(paddle2)<50:
        ball.bounce_x()

    # Paddle2 misses the ball
    if ball.xcor()>=400:
        ball.restart()
        score.l_point()

    # Paddle1 misses the ball
    if ball.xcor() <= -400:
        ball.restart()
        score.r_point()








screen.exitonclick()