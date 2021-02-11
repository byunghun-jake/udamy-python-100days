import turtle
import random


class MyTurtle(turtle.Turtle):
    def draw_polygon(self, count, width):
        self.pendown()
        angle = 360 / count
        print(angle)
        for _ in range(count):
            self.forward(width)
            self.right(angle)

    def set_random_color(self):
        color_list = ["navy", "green", "orange red", "yellow", "peach puff"]
        self.color(random.choice(color_list))


t = MyTurtle()
for count in range(3, 20):
    t.set_random_color()
    t.draw_polygon(count, 100)

screen = turtle.Screen()
screen.exitonclick()