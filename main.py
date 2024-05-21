from turtle import Turtle, Screen


# Drawing functions
def move_forward():
    t.forward(20)


def move_backward():
    t.backward(20)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def reset():
    t.reset()


if __name__ == '__main__':
    t = Turtle()
    screen = Screen()

    screen.listen()
    screen.onkey(move_forward, 'w')
    screen.onkey(move_backward, 's')
    screen.onkey(turn_left, 'a')
    screen.onkey(turn_right, 'd')
    screen.onkey(reset, 'c')
    screen.exitonclick()