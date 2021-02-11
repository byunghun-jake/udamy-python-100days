import turtle
import random


class MyTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color_list = ["navy", "green", "orange red", "coral1", "peach puff", "cornsilk4", "DeepPink", "DarkViolet", "DeepSkyBlue"]

    def random_color(self):
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def random_walk(self, count, length):
        angle_list = [0, 90, 180, 270]
        for _ in range(count):
            self.random_color()
            self.setheading(random.choice(angle_list))
            self.forward(length)


screen = turtle.Screen()
screen.colormode(255)
t = MyTurtle()
t.pensize(10)
t.speed(10)
t.random_walk(200, 20)


screen.exitonclick()

