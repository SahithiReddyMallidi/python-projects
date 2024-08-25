import turtle
from turtle import Turtle,Screen
import pandas

screen=Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def on_screen_click(x,y):
#     print(x,y)
#
# turtle.onscreenclick(on_screen_click)

data= pandas.read_csv("50_states.csv")
states=data["state"].to_list()
guessed_states=[]
count=0
while len(guessed_states)<50:
    ans_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Enter the state name").title()
    if ans_state=="Exit":
        missing_states=[]
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if ans_state in states:
        guessed_states.append(ans_state)
        count+=1
        t=Turtle()
        t.hideturtle()
        t.penup()
        cords=data[data["state"]==ans_state]
        t.goto(cords.x.item(),cords.y.item())
        t.write(arg=cords.state.item())



print(count)


screen.exitonclick()
