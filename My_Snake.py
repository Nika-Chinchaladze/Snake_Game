from turtle import Turtle
from random import choice

RANDOM_COLORS = ["alice blue", "pale green", "navajo white", "pink", "lavender", "aquamarine", "old lace", "azure"]
STARTING_POSITIONS = [(0, 0), (-30, 0), (-60, 0)]
DISTANCE = 30
UP = 90
DOWN = 270
WEST = 180
EAST = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.born_snake()
        self.starter = self.snake_list[0]

    def born_snake(self):
        for loc in STARTING_POSITIONS:
            self.add_snake(loc)

    def add_snake(self, location):
        snake = Turtle()
        snake.penup()
        snake.shape("circle")
        snake.shapesize(1.5)
        snake.color(choice(RANDOM_COLORS))
        snake.goto(location)
        self.snake_list.append(snake)

    def increase_snake(self):
        self.add_snake(self.snake_list[-1].pos())

    def move_forward(self):
        for current in range(len(self.snake_list)-1, 0, -1):
            x_coordinate = self.snake_list[current - 1].xcor()
            y_coordinate = self.snake_list[current - 1].ycor()
            self.snake_list[current].goto(x_coordinate, y_coordinate)
        self.starter.forward(DISTANCE)

    def suicide_snake(self):
        for snk in self.snake_list[1:]:
            if self.starter.distance(snk) < 15:
                return True

    def crashed_snake(self):
        if (self.starter.xcor() > 255 or self.starter.xcor() < -255) or \
                (self.starter.ycor() > 225 or self.starter.ycor() < -255):
            return True

    def move_north(self):
        if self.starter.heading() != DOWN:
            self.starter.setheading(90)

    def move_south(self):
        if self.starter.heading() != UP:
            self.starter.setheading(270)

    def move_west(self):
        if self.starter.heading() != EAST:
            self.starter.setheading(180)

    def move_east(self):
        if self.starter.heading() != WEST:
            self.starter.setheading(0)

    def reborn_snake(self):
        for snk in self.snake_list:
            snk.reset()
        self.snake_list = []
