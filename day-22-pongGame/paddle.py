# TODO 2: Create and move a paddle
import turtle


class Paddle:
    def __init__(self, x_pos):
        self.paddles = []
        self.position = [-30, -10, -10, 30]
        self.direction = 1
        for i in range(4):
            new_t = turtle.Turtle("square")
            new_t.speed("fastest")
            new_t.penup()
            new_t.color("white")
            new_t.setheading(90)
            # position = (x_pos, -20*i)
            new_t.goto(x_pos, self.position[i])
            self.paddles.append(new_t)
        self.head = self.paddles[0]
        self.paddles[0].color("red")

    def move(self):
        # y_distance = self.direction * 20
        for i in range(len(self.paddles)-1, 0, -1):
            self.paddles[i].goto(self.paddles[i-1].xcor(), self.paddles[i-1].ycor())
        self.head.forward(20)

    def change_direction(self):
        self.head.setheading(-self.head.heading())

    # def game_start(self):


















