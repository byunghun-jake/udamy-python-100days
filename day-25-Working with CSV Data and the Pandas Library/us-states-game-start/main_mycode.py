import turtle
import pandas

screen = turtle.Screen()
screen.title("미국 주 맞추기 게임")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

class State(turtle.Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(name, True, align="center")

# 스크린에서 클릭한 위치를 알고 싶을 때
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# 주 정보를 불러온다.
data_states = pandas.read_csv("./50_states.csv")
states = data_states.state
states_list = states.to_list()

# 50개의 주를 맞춘다.
answer_list = []

while len(answer_list) < 50:
    answer_state = screen.textinput(title=f"{len(answer_list)}/50 States Correct?", prompt="What's another state name?").lower()

    # 정답 확인
    state_row = data_states[data_states.state.str.lower() == answer_state]

    # 정답이 아니라면?
    if state_row.empty:
        print("Wrong!")
        continue

    # 이미 정답
    if answer_state in answer_list:
        print("이미 입력했어")
        continue

    # 정답
    print(state_row)
    answer_list.append(state_row.state.values[0].lower())
    print(state_row.state.values)
    x_pos = int(state_row.x)
    y_pos = int(state_row.y)
    # 거북이 생성
    State(state_row.state.values[0], x_pos, y_pos)


screen.exitonclick()

















screen.exitonclick()



























































