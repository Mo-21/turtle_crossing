from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Courier", 80, "normal"))

    def win_game(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write("You Won", align="center", font=("Courier", 80, "normal"))
