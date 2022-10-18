from turtle import Turtle


class GridLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.pencolor("steel blue")

    def draw_ordered(self):
        self.goto(-255, 225)
        self.pendown()
        self.setheading(0)
        # rows
        for i in range(8):
            self.forward(510)
            self.right(90)
            self.forward(30)
            self.right(90)
            self.forward(510)
            self.left(90)
            self.forward(30)
            self.setheading(0)
        self.forward(510)
        # columns
        self.setheading(90)
        for j in range(8):
            self.forward(480)
            self.left(90)
            self.forward(30)
            self.left(90)
            self.forward(480)
            self.right(90)
            self.forward(30)
            self.setheading(90)
        self.forward(480)
        self.left(90)
        self.forward(30)
        self.left(90)
        self.forward(480)

