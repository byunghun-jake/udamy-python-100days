# Create the Screen
import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(-1)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
com_score = ScoreBoard(40)
user_score = ScoreBoard(-40)

time.sleep(0.1)
screen.update()
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.02)
    r_paddle.move()
    l_paddle.move()

    # Listen Event
    screen.onkey(l_paddle.change_direction, "space")
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    # Detect collision paddle width wall
    if r_paddle.ycor() > 260 or r_paddle.ycor() < -260:
        r_paddle.change_direction()
    if l_paddle.ycor() > 260 or l_paddle.ycor() < -260:
        l_paddle.change_direction()

    # Ball move
    ball.move()

    # Detect collision ball with wall and bounce
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
        # current_heading = ball.heading()
        # ball.setheading(-current_heading)

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        continue
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        continue

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






























screen.exitonclick()
