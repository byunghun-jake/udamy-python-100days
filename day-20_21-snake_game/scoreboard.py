import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.shapesize(0.1, 0.1, 0.1)
        self.score = -1
        self.score_update()

    def score_update(self):
        self.clear()
        self.score += 1
        text = f"score: {self.score}"
        self.write(text, align="center", font=("Courier", 18, "bold"))

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("Courier", 18, "bold"))
























