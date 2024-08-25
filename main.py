import turtle

from Snake import Snake
from turtle import Screen, Turtle
from Food import Food
from ScoreBoard import ScoreBoard
import time

Screen=Screen()
Screen.bgcolor("dark olive green")
Screen.screensize(600, 600)
Screen.title("My Snake Game")
Screen.tracer(0)

snake=Snake()
food=Food()
score=ScoreBoard()
Screen.listen()
Screen.onkey(snake.goUp,"Up")
Screen.onkey(snake.goDown,"Down")
Screen.onkey(snake.goLeft,"Left")
Screen.onkey(snake.goRight,"Right")

game_is_still_on=True
while game_is_still_on:
    Screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        score.score_increment()
        print(score.score)

    # Detect collision with wall
    if snake.head.xcor()>600 or snake.head.xcor()<-600 or snake.head.ycor()>600 or snake.head.ycor()<-600:
        score.game_over()
        game_is_still_on=False

    # Detect collision with tail
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment)<10:
            score.game_over()
            game_is_still_on=False


Screen.exitonclick()


