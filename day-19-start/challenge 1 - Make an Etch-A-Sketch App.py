from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_right():
    t.right(5)


def turn_left():
    t.left(5)


def reset():
    t.reset()


# plus alpha (색상 바꾸기, spirograph 그리기)
def change_color():
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_spirograph():
    t.speed("fastest")
    for _ in range(72):
        t.circle(50)
        t.right(5)
    t.speed(1)


t.pensize(2)
screen.colormode(255)
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(reset, "c")
screen.onkey(change_color, "space")
screen.onkey(draw_spirograph, "p")

screen.exitonclick()
