from turtle import Screen
from time import sleep
from My_Snake import Snake
from Draw_Grifline import GridLine
from Draw_Borders import Border
from Food_Section import Rat
from Count_Score import ScoreCounter


# prepare screen:
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.addshape("rat.gif")
screen.tracer(0)

# draw grid lines and borders:
grid_line = GridLine()
border = Border()
grid_line.draw_ordered()
border.draw_border()

# create rat and count score:
score = ScoreCounter()
rat = Rat()

try_again = True
while try_again:
    snake = Snake()
    screen.listen()
    screen.onkey(snake.move_north, "w")
    screen.onkey(snake.move_south, "s")
    screen.onkey(snake.move_west, "a")
    screen.onkey(snake.move_east, "d")

    play_game = True
    while play_game:
        screen.update()
        sleep(0.1)
        snake.move_forward()
        if snake.starter.distance(rat) < 25:
            rat.random_positions()
            snake.increase_snake()
            score.show_score()
        if snake.suicide_snake():
            score.game_over()
            play_game = False
        if snake.crashed_snake():
            score.game_over()
            play_game = False

    will = screen.textinput(title="end/continue", prompt="Do You Want to Try Again? Yes/No ").lower()
    if will == "no":
        try_again = False
    else:
        score.clear()
        score.restart_eaten()
        snake.reborn_snake()


screen.exitonclick()
