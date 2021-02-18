from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)        # 10x10
        self.color("blue")
        self.speed("fastest")
        self.set_location()

    def set_location(self):
        random_x = random.randint(-240, 240)
        random_y = random.randint(-240, 240)
        self.goto(x=random_x, y=random_y)





















