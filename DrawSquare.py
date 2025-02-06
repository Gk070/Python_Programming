import turtle

def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)

t = turtle.Turtle()

square(t, length = 100)