from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Turtle(shape="turtle")
turtle.color("white")
turtle.penup()
turtle.setheading(90)
screen.update()

screen.exitonclick()
