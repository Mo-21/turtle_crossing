from turtle import Turtle
import random

COLORS = ["red", "blue", "white", "brown", "green", "yellow", "purple"]


class Car:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=3)
            car.goto(x=320, y=random.randint(-260, 260))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(10)
