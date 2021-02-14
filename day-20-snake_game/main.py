import turtle
import time
from snake import Snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
screen.tracer(0)

snake = Snake()

screen.update()
is_game_on = True

while is_game_on:
    print("loop")
    screen.update()
    time.sleep(0.2)

    snake.move()
























screen.exitonclick()
