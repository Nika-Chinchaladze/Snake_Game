from turtle import Turtle
from random import randint


class Rat(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("rat.gif")
        self.random_positions()

    def random_positions(self):
        x_coordinate = randint(-225, 225)
        y_coordinate = randint(-225, 205)
        self.goto(x_coordinate, y_coordinate)
