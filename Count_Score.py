from turtle import Turtle
ALIGNMENT = "center"
FONT_1 = ("Arial", 16, "bold")
FONT_2 = ("Arial", 24, "bold")


class ScoreCounter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.eaten = 0
        self.current_score()

    def current_score(self):
        self.goto(0, 265)
        self.write(f"Eaten Rats: {self.eaten}", align=ALIGNMENT, font=FONT_1)

    def show_score(self):
        self.eaten += 1
        self.clear()
        self.current_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_2)

    def restart_eaten(self):
        self.eaten = 0
        self.current_score()
