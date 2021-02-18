import turtle
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.update()
is_game_on = True

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision snake with food
    if snake.head.distance(food) < 15:
        # Change location of food
        food.set_location()
        scoreboard.score_update()
        snake.extend()

    # Detect collision snake with wall
    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    if snake_x < -280 or snake_x > 280 or snake_y < -280 or snake_y > 280:
        scoreboard.game_over()
        snake.head.color("red")
        is_game_on = False

    # Detect collision snake with tail
    for segment in snake.segments[4:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            snake.head.color("red")
            is_game_on = False
    # if head collides with any segment in the tail:
        # trigger game_over























screen.exitonclick()
