# import colorgram
#
# colors = colorgram.extract("./damien-hirst-lactulose.jpg", 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     if r + g + b > 600:
#         continue
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import random

color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31)]
t = turtle.Turtle()
# 1. 좌측 하단으로 거북이 이동
# 2. y축으로 반복문 수행
# 2-1. x축으로 반복문 수행 (10번 반복)
# 2-1-1. 색상 설정 / 점 그리기
# 2-1-2. 우측으로 50만큼 이동

screen = turtle.Screen()
screen.colormode(255)

t.penup()
t.speed(11)
for y in range(10):
    pos_y = -325 + 70 * y
    t.sety(pos_y)
    for x in range(10):
        pos_x = -325 + 70 * x
        t.setx(pos_x)
        t.dot(20, random.choice(color_list))

screen.exitonclick()

