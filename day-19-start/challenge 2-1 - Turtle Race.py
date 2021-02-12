import turtle
import random


class RacingTurtle(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.goto(x=x, y=y)
        self.is_race_on = True

    def random_forwards(self):
        self.forward(random.randint(0, 10))

    def is_race_over(self):
        if self.xcor() > 230:
            return True


is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="선택", prompt="어떤 거북이가 우승할까요?: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for idx in range(len(colors)):
    x_pos = -230
    y_pos = 100 - 40*idx
    turtles.append(RacingTurtle(x=x_pos, y=y_pos, color=colors[idx]))


if user_bet in colors:
    is_race_on = True

# 게임 시작
while is_race_on:
    for t in turtles:
        if not t.is_race_over():
            t.random_forwards()
            continue

        winner_color = t.pencolor()
        print(f"{winner_color} is winner!")

        if user_bet == winner_color:
            print("You won!")
        else:
            print("You lost!")

        is_race_on = False
        break

