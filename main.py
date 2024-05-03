from turtle import Screen
from turtle_player import TurtlePlayer

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

tim = TurtlePlayer()

screen.listen()
screen.onkey(key="Up", fun=tim.move_forward)
screen.onkey(key="Down", fun=tim.move_backward)

game_is_on = True
while game_is_on:
    screen.update()

    if tim.ycor() > 280:
        print("You won")

screen.exitonclick()
