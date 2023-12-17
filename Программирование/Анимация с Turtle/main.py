import turtle, colorsys
screen = turtle.Screen()
screen.setup(700,700)
screen.tracer(0)
screen.bgcolor('#ECF1FD')

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

hue = 0.0
a=200
b=50
degree=20
px=0
px2=2
while True :

    while b<190:

        t.clear()
        for f in range(15):

            t.penup()
            t.left(degree)
            t.fd(px)
            t.pendown()


            for i in range(6):
                color = colorsys.hsv_to_rgb(hue, 1, 0.5)
                t.pencolor(color)
                t.circle(a, 45)
                t.circle(b, 90)
                t.circle(a, 90)
                t.circle(b, 90)
                t.circle(a, 45)
            hue += 0.001
            t.pensize(f%3)

            a -= 1
            b += 1
            t.left(0.1)

            t.penup()
            t.left(180)
            t.fd(px2)
            t.pendown()
        screen.update()

    while a<190:
        t.clear()
        for f in range(15):
            t.penup()
            t.left(degree)
            t.fd(px)
            t.pendown()
            for i in range(6):
                color = colorsys.hsv_to_rgb(hue, 1, 0.5)
                t.pencolor(color)
                t.circle(a, 45)
                t.circle(b, 90)
                t.circle(a, 90)
                t.circle(b, 90)
                t.circle(a, 45)
            hue += 0.005
            t.pensize(f%3)
            a += 1
            b -= 1
            t.left(0.1)
            t.penup()
            t.left(180)
            t.fd(px2)
            t.pendown()

        screen.update()