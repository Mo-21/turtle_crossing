from turtle import Turtle


class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)

    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)
