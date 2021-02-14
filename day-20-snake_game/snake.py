import turtle
MOVE_INSTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_segment = turtle.Turtle("square")
            x_pos = -20 * i
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x_pos, 0)
            self.segments.append(new_segment)

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)
        self.segments[0].forward(MOVE_INSTANCE)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        # self.segments[0].forward(MOVE_INSTANCE)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
