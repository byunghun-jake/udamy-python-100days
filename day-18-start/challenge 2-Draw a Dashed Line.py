import turtle


# 클래스 상속을 이용해보았습니다.
class DashTurtle(turtle.Turtle):
    def draw_dashed(self, length):
        position = 0
        while position < length:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(5)
            position += 20


t = DashTurtle()

t.shape("turtle")
screen = turtle.Screen()


# def draw_dashed(length):
#     position = 0
#     while position < length:
#         t.pendown()
#         t.forward(15)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         position += 20


for _ in range(4):
    t.draw_dashed(100)
    t.right(90)

screen.exitonclick()
