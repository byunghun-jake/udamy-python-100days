# Create and move a paddle
import turtle


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move(self):
        # self.forward(20)
        pass

    def change_direction(self):
        self.setheading(-self.heading())

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)













