from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="선택하세요!", prompt="어떤 거북이가 1등할까요?: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# 반복문으로 거북이 초기화하기
for i in range(len(colors)):
    turtles.append(Turtle("turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=(100 - 40 * i))

# red = Turtle("turtle")
# orange = Turtle("turtle")
# yellow = Turtle("turtle")
# green = Turtle("turtle")
# blue = Turtle("turtle")
# purple = Turtle("turtle")
#
# # 색상 초기화
# red.color("red")
# red.color("orange")
# red.color("yellow")
# red.color("green")
# red.color("blue")
# red.color("purple")
#
# # 펜 업
# red.penup()
# orange.penup()
# yellow.penup()
# green.penup()
# blue.penup()
# purple.penup()
#
# # 위치 초기화
# red.goto(x=-230, y=100)
# orange.goto(x=-230, y=60)
# yellow.goto(x=-230, y=20)
# green.goto(x=-230, y=-20)
# blue.goto(x=-230, y=-60)
# purple.goto(x=-230, y=-100)


# 레이스
if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        # 게임 종료 조건
        if t.xcor() > 230:
            winner_t = t.pencolor()
            print(f"{winner_t} is winner!", end=" ")
            is_race_on = False
            break

        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)

if winner_t == user_bet:
    print(f"You won! congratulations!")
else:
    print(f"You lost... Winner turtle is {winner_t}.")


screen.exitonclick()
