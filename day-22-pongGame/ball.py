# TODO 4: Create the ball and make it move
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
        # self.setheading(-5)

    def move(self):
        self.forward(20)

    def game_start(self):
        self.speed("fastest")
        self.home()
        self.speed("fast")
        self.setheading(random.randint(0, 360))


