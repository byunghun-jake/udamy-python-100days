# Create the ball and make it move
import turtle
import random


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.shapesize(0.5)
        self.game_start()
        self.x_move = 4
        self.y_move = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.forward(8)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def game_start(self):
        # self.speed("fastest")
        self.home()
        # self.speed("fast")
        # self.setheading(random.randint(0, 360))
        # self.setheading(180)

