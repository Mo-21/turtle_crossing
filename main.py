from turtle import Screen
from turtle_player import TurtlePlayer
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

tim = TurtlePlayer()

screen.listen()
screen.onkey(key="Up", fun=tim.move_forward)
screen.onkey(key="Down", fun=tim.move_backward)

car = Car()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_car()
    screen.update()

    for c in car.all_cars:
        if c.distance(tim) < 20:
            score.game_over()
            game_is_on = False

    if tim.ycor() > 260:
        score.win_game()
        game_is_on = False

screen.exitonclick()
