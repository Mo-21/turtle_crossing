from turtle import Screen
from turtle_player import TurtlePlayer

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

tim = TurtlePlayer()

screen.update()

screen.exitonclick()
