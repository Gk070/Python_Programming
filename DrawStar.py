import turtle

def star(t, length):
    for i in range(5):
        t.forward(length)
        t.left(144)

t = turtle.Turtle()
star(t, length = 100)