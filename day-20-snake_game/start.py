import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
screen.tracer(0)

turtles = []
for i in range(3):
    temp_turtle = turtle.Turtle("square")
    x_pos = -20 * i
    temp_turtle.penup()
    temp_turtle.color("white")
    temp_turtle.goto(x=x_pos, y=0)
    turtles.append(temp_turtle)

screen.update()
is_game_on = True

while is_game_on:
    print("loop")
    screen.update()
    time.sleep(0.2)
    # for t in turtles:
    #     t.forward(20)
    #
    # for i in range(len(turtles)):
    #     screen.update()
    #     time.sleep(1)
    #     for j in range(len(turtles)):
    #         if i == j:
    #             turtles[j].right(90)
    #         turtles[j].forward(20)

    # 가장 앞에 있는 것만 조종하고, 뒤에 따라오는 것들은 바로 앞에 있는 이전 좌표로 이동
    for idx in range(len(turtles) - 1, 0, -1):
        new_x = turtles[idx - 1].xcor()
        new_y = turtles[idx - 1].ycor()
        turtles[idx].goto(new_x, new_y)
    # turtles[0].left(90)
    turtles[0].forward(20)
























screen.exitonclick()
