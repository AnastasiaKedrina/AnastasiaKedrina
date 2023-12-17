#Кедрина Анастасия 14122
#Интерпритация розы Гранди, несколько вариантов
#На вход получает число и рисует картинку по этому номеру
#Большие (длинные) числа в count были найдены через random
import turtle, math, random
screen = turtle.Screen()
screen.setup(700,700)
screen.tracer(0)
screen.bgcolor('#DEDEDE')

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

d=300
i=0
count=[7, 3, 1.5, 1.8, 0.21460106395107575, 0.4289379494900796,  0.7521542330599897, 0.38477787402839964, 0.5704589017381768, 0.7858770152072595]

k=0
while k!=1:
    try:
        print('Введите число от 0 до ', len(count) - 1)
        n=int(input())
        if n>=0 and n<len(count):
            k=1
        else:
            k=0
    except ValueError:
        k=0

print('Черепашка нарисовала рисунок')
c=count[n]

#c=count[random.randrange(0, len(count))]
ro=d*math.sin(c*i)
x=ro*math.sin(i)
y=ro*math.cos(i)

for i in range(700):

    t.goto(x, y)
    ro = d * math.sin(c * i)
    x = ro * math.sin(i)
    y = ro * math.cos(i)

screen.mainloop()
