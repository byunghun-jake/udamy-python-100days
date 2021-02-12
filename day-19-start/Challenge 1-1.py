import turtle
import random


class ControlTurtle(turtle.Turtle):
    def move_forwards(self):
        self.forward(10)

    def move_backwards(self):
        self.backward(10)

    def turn_right(self):
        self.right(5)

    def turn_left(self):
        self.left(5)

    def reset_turtle(self):
        self.reset()

    def change_color(self):
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_spirograph(self):
        self.speed("fastest")
        for _ in range(72):
            self.circle(50)
            self.right(5)
        self.speed(1)


screen = turtle.Screen()
t = ControlTurtle()

t.pensize(2)
screen.colormode(255)
screen.listen()
screen.onkey(t.move_forwards, "w")
screen.onkey(t.move_backwards, "s")
screen.onkey(t.turn_left, "a")
screen.onkey(t.turn_right, "d")
screen.onkey(t.reset, "c")
screen.onkey(t.change_color, "space")
screen.onkey(t.draw_spirograph, "p")

screen.exitonclick()
