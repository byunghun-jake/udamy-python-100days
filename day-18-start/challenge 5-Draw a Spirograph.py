import turtle
import random


class MyTurtle(turtle.Turtle):
    def set_random_color(self):
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def spiro_graph(self, size_of_gap):
        count = 360 / size_of_gap
        for _ in range(int(count)):
            self.right(size_of_gap)
            self.set_random_color()
            self.circle(100)


t = MyTurtle()
t.pensize(2)
t.speed(11)
screen = turtle.Screen()
screen.colormode(255)
t.spiro_graph(5)


screen.exitonclick()