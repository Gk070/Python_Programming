import turtle

def triangle(t, length):
    for i in range(3):
        t.forward(length)
        t.left(120)

t = turtle.Turtle()

triangle(t, 100)