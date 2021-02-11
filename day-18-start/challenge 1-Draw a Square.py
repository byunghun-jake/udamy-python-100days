import turtle

t = turtle.Turtle()

t.shape("turtle")
t.color("purple")

for _ in range(3):
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

screen = turtle.Screen()
screen.exitonclick()