import turtle


def staircase(t, num, tread, riser):
    for i in range(num):
        stair(t, tread, riser)
    return


def stair(t, tread, riser):
    t.down()
    t.forward(tread)
    t.right(90)
    t.forward(riser)
    t.left(90)
    return

s = turtle.screen()
t = turtle.Turtle()
staircase()


