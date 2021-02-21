# TODO 1: Create the Screen
import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(-1)

com_paddle = Paddle(380)
user_paddle = Paddle(-380)
ball = Ball()
com_score = ScoreBoard(40)
user_score = ScoreBoard(-40)

time.sleep(0.1)
screen.update()
screen.listen()

on_game_over = False

while not on_game_over:
    time.sleep(0.1)
    com_paddle.move()
    user_paddle.move()
    screen.onkey(user_paddle.change_direction, "space")

    # Detect collision paddle width wall
    if com_paddle.head.ycor() > 260 or com_paddle.head.ycor() < -260:
        com_paddle.change_direction()
    if user_paddle.head.ycor() > 260 or user_paddle.head.ycor() < -260:
        user_paddle.change_direction()

    # Ball move
    ball.move()

    # Detect collision ball with wall and bounce
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        current_heading = ball.heading()
        ball.setheading(-current_heading)

    # Detect collision with paddle
    for paddle in com_paddle.paddles:
        if ball.distance(paddle) < 15:
            current_heading = ball.heading()
            ball.setheading(180-current_heading)
            break
    for paddle in user_paddle.paddles:
        if ball.distance(paddle) < 15:
            current_heading = ball.heading()
            ball.setheading(180 - current_heading)
            break

    # Detect when paddle messes
    if ball.xcor() < -400:
        com_score.score_update()
        ball.game_start()
        screen.update()
        time.sleep(1)
    elif ball.xcor() > 400:
        user_score.score_update()
        ball.game_start()
        screen.update()
        time.sleep(1)


    # ScoreBoard


    screen.update()




























screen.exitonclick()
