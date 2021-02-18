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
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(15):
            position = (i*-20, 0)
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        last_segment = self.segments[-1]
        self.add_segment(last_segment.position())

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)
        self.head.forward(MOVE_INSTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # self.head.forward(MOVE_INSTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
