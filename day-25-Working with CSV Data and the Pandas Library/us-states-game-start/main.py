import turtle
import pandas

screen = turtle.Screen()
screen.title("미국 주 맞추기 게임")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# 주 정보를 불러온다.
data = pandas.read_csv("./50_states.csv")
# 주 정보 중 이름에 대한 시리즈를 리스트로 저장한다.
all_states = data.state.to_list()

guessed_states = []

# If answer_state is one of the states in all the states of the 50_states.csv
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} States Correct",
                                    prompt="What's another state's name?").title()

    # If they get it right:
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # Create a turtle to write the name of the state at the state's x and y coor
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        # t.write(answer_state)

    if answer_state == "Exit":
        break


# 결과 파일 만들기 (Save the missing states to a.csv)
# states_to_learn.csv
# all_states_set = set(all_states)
# guessed_states_set = set(guessed_states)
# missing_states = list(all_states_set - guessed_states_set)

missing_states = [state for state in all_states if state not in guessed_states]
# for state in all_states:
#     if state not in guessed_states:
#         missing_states.append(state)
new_data = pandas.DataFrame({"state": missing_states})
new_data.to_csv("./a.csv")
print(missing_states)























screen.exitonclick()



























































