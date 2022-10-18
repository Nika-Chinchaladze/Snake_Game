from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(1.5)
        self.color("dark green")
        self.speed("fastest")
        self.penup()

    def draw_border(self):
        self.goto(-270, 240)
        self.stamp()
        for i in range(18):
            self.forward(30)
            self.stamp()
        self.setheading(270)
        for j in range(17):
            self.forward(30)
            self.stamp()
        self.setheading(180)
        for i in range(18):
            self.forward(30)
            self.stamp()
        self.setheading(90)
        for i in range(16):
            self.forward(30)
            self.stamp()
