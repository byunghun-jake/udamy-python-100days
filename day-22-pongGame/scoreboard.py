import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x_pos, 260)
        # self.shape()
        self.score = -1
        self.score_update()

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Courier", 18, "bold"))