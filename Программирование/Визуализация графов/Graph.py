import pygame
from pygame.locals import (K_ESCAPE,KEYDOWN,QUIT)
import random
#-----------------------------------
f = open('graf.txt', 'r')
f = f.readlines()

# Коллекция названий вершин
num = f[0].split()[1:]
print('Названия вершин')
print(num)
num_low = []
for i in num:
    num_low.append(i.lower())


#а - матрица путей без названий вершин
a = []
for i in range(1, len(f)):
    f[i] = f[i].split()
    for j in range(len(f[i])):
        try:
            f[i][j] = int(f[i][j])
        except:
            pass
    a.append(f[i][1:])


#d - словарь, в котором ключ=путь, значение=длина пути
d = dict()
d1 = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if i != j and a[i][j] != 0:
            s = str(num[i]) + str(num[j])
            d[s] = a[i][j]
            d1.append(s)
        elif i!=j:
            s = str(num[i]) + str(num[j])
            d[s]=10**8
print('Словарь всех имеющихся путей и их длин')
print('Остутствующие длины заменены на большое число, чтобы потом не учитывать их в минимуме')
print(d)
all_ways=d1[:]

print('------------------------------------')
#Ввод начала и конца пути
x=1
while x!=0:
    print('Введите две английские буквы без пробела - начало и конец пути')
    way=list(input())
    if (way[0] in num) and (way[1] in num):
        start=way[0]
        end=way[1]
        x=0
    elif (way[0] in num_low) and (way[1] in num_low):
        start=way[0].upper()
        end=way[1].upper()
        x=0
    else:
        pass

#Нахождение кратчайшего пути
c=[]
c.append(d[start+end])
for i in num:
    if i!=start and i!=end:
        try:
            way=d[start+i]+d[i+end]
            c.append(way)
        except:
            pass
        if min(c)==way:
            l=i
            ch=way
        elif min(c)==d[start+end]:
            l=end
            ch=d[start+end]
if end!=l:
    result=start+l+end
else:
    result=start+end
print('Кратчайший путь:')
print(result)
print('Длина пути:')
print(ch)
print('------------------------------------')
print('Посмотрите окно PyGame')
screen=pygame.display.set_mode((800, 500))
clock=pygame.time.Clock()
pygame.init()

#-----------------------------------
running=True
while running:
    #Закрытие окна
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running=False
        elif event.type== QUIT:
            running=False
    #Фон
    background_image = pygame.image.load("background.jpg").convert()
    screen.blit(background_image, [0, 0])
    #Координаты положения вершин графа
    A=(100, 180)
    B=(300, 100)
    C=(500, 100)
    D=(700, 180)
    E=(100, 360)
    F=(300, 440)
    G=(500, 440)
    H=(700, 360)
    start_line=0
    end_line=0


    def end(end_line):
        # Конец линии
        if one_way[1] == 'A':
            return A
        if one_way[1] == 'B':
            return B
        if one_way[1] == 'C':
            return C
        if one_way[1] == 'D':
            return D
        if one_way[1] == 'E':
            return E
        if one_way[1] == 'F':
            return F
        if one_way[1] == 'G':
            return G
        if one_way[1] == 'H':
            return H


    # Отрисовка линий исходя из входных данных
    for one_way in all_ways:
        # Начало линии
        if one_way[0] == 'A':
            start_line = A
        if one_way[0] == 'B':
            start_line = B
        if one_way[0] == 'C':
            start_line = C
        if one_way[0] == 'D':
            start_line = D
        if one_way[0] == 'E':
            start_line = E
        if one_way[0] == 'F':
            start_line = F
        if one_way[0] == 'G':
            start_line = G
        if one_way[0] == 'H':
            start_line = H
        end_line = end(end_line)

        pygame.draw.line(screen, (255, 255, 255), start_line, end_line, 3)

        if pygame.mouse.get_focused():
            #Положение курсора
            cursor = pygame.mouse.get_pos()

            font = pygame.font.Font(None, 24)
            text_way = font.render(str(d[one_way]), True,(53, 18, 80))

            #Наведение курсора на конкретную вершину
            if cursor[0] > A[0] - 30 and cursor[0] < A[0] + 30:
                if cursor[1] > A[1] - 30 and cursor[1] < A[1] + 30:
                    if one_way[0] == 'A':
                        start_line = A
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),A, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

            if cursor[0] > B[0] - 30 and cursor[0] < B[0] + 30:
                if cursor[1] > B[1] - 30 and cursor[1] < B[1] + 30:
                    if one_way[0] == 'B':
                        start_line = B
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),B, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

            if cursor[0] > C[0] - 30 and cursor[0] < C[0] + 30:
                if cursor[1] > C[1] - 30 and cursor[1] < C[1] + 30:
                    if one_way[0] == 'C':
                        start_line = C
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),C, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

            if cursor[0] > D[0] - 30 and cursor[0] < D[0] + 30:
                if cursor[1] > D[1] - 30 and cursor[1] < D[1] + 30:
                    if one_way[0] == 'D':
                        start_line = D
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),D, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

            if cursor[0] > E[0] - 30 and cursor[0] < E[0] + 30:
                if cursor[1] > E[1] - 30 and cursor[1] < E[1] + 30:
                    if one_way[0] == 'E':
                        start_line = E
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),E, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

            if cursor[0] > F[0] - 30 and cursor[0] < F[0] + 30:
                if cursor[1] > F[1] - 30 and cursor[1] < F[1] + 30:
                    if one_way[0] == 'F':
                        start_line = F
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),F, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

            if cursor[0] > G[0] - 30 and cursor[0] < G[0] + 30:
                if cursor[1] > G[1] - 30 and cursor[1] < G[1] + 30:
                    if one_way[0] == 'G':
                        start_line = G
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),G, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

            if cursor[0] > H[0] - 30 and cursor[0] < H[0] + 30:
                if cursor[1] > H[1] - 30 and cursor[1] < H[1] + 30:
                    if one_way[0] == 'H':
                        start_line = H
                        end_line = end(end_line)
                        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
                        pygame.draw.line(screen,(random.randint(168, 217), random.randint(135, 217), random.randint(175, 231)),start_line, end_line, 8)
                        pygame.draw.circle(screen, (151,56,123),H, 33)

                        if one_way[1]=='A' or one_way[1]=='B' or one_way[1]=='C' or one_way[1]=='D':
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]-40)))
                        else:
                            screen.blit(text_way, text_way.get_rect(center=(end_line[0], end_line[1]+40)))

    if result[0] == 'A':
        start_line = A
    if result[1] == 'A':
        end_line = A

    if result[0] == 'B':
        start_line = B
    if result[1] == 'B':
        end_line = B

    if result[0]=='C':
        start_line=C
    if result[1]=='C':
        end_line=C

    if result[0] == 'D':
        start_line = D
    if result[1] == 'D':
        end_line = D

    if result[0]=='E':
        start_line=E
    if result[1]=='E':
        end_line=E

    if result[0]=='F':
        start_line=F
    if result[1]=='F':
        end_line=F

    if result[0] == 'G':
        start_line = G
    if result[1] == 'G':
        end_line = G

    if result[0]=='H':
        start_line=H
    if result[1]=='H':
        end_line=H


    if len(result) == 2:
        pygame.draw.line(screen,(83,28,101),start_line, end_line, 12)
    else:
        if result[1] == 'A':
            middle_line = A
        if result[1] == 'B':
            middle_line = B
        if result[1] == 'C':
            middle_line = C
        if result[1] == 'D':
            middle_line = D
        if result[1] == 'E':
            middle_line = E
        if result[1] == 'F':
            middle_line = F
        if result[1] == 'G':
            middle_line = G
        if result[1] == 'H':
            middle_line = H

        if result[2] == 'A':
            end_line = A
        if result[2] == 'B':
            end_line = B
        if result[2] == 'C':
            end_line = C
        if result[2] == 'D':
            end_line = D
        if result[2] == 'E':
            end_line = E
        if result[2] == 'F':
            end_line = F
        if result[2] == 'G':
            end_line = G
        if result[2] == 'H':
            end_line = H
        pygame.draw.line(screen, (83, 28, 101), start_line, middle_line, 12)
        pygame.draw.line(screen, (83, 28, 101), middle_line, end_line, 12)


    # (168, 197, 231) голубой
    # (254,217,175) желтый
    # (213,135,185) розовый

    #Круги - вершины
    pygame.draw.circle(screen, (255, 255, 255),A, 30)
    pygame.draw.circle(screen, (255, 255, 255),B, 30)
    pygame.draw.circle(screen, (255, 255, 255),C, 30)
    pygame.draw.circle(screen, (255, 255, 255),D, 30)
    pygame.draw.circle(screen, (255, 255, 255),E, 30)
    pygame.draw.circle(screen, (255, 255, 255),F, 30)
    pygame.draw.circle(screen, (255, 255, 255),G, 30)
    pygame.draw.circle(screen, (255, 255, 255),H, 30)

    #Подпись вершин
    font = pygame.font.Font(None, 48)
    for i in range(len(num)):
        text = font.render(num[i], True,(0, 0, 0))
        if num[i]=='A':
            place = text.get_rect(center=A)
        if num[i]=='B':
            place = text.get_rect(center=B)
        if num[i]=='C':
            place = text.get_rect(center=C)
        if num[i]=='D':
            place = text.get_rect(center=D)
        if num[i]=='E':
            place = text.get_rect(center=E)
        if num[i]=='F':
            place = text.get_rect(center=F)
        if num[i]=='G':
            place = text.get_rect(center=G)
        if num[i]=='H':
            place = text.get_rect(center=H)
        screen.blit(text, place)
    #Текст сверху окна
    font = pygame.font.Font(None, 24)
    text_1=font.render('Наведите курсор на вершину, чтобы посмотреть какой длины пути из нее выходят', True, (53,18,80))
    screen.blit(text_1, text_1.get_rect(center=(400,30)))
    #Текст снизу окна
    text_result='Кратчайший путь: '+str(result)
    text_2=font.render(text_result, True, (53,18,80))
    screen.blit(text_2, text_2.get_rect(center=(130,450)))
    text_result='Длина пути: '+str(ch)
    text_2=font.render(text_result, True, (53,18,80))
    screen.blit(text_2, text_2.get_rect(center=(100,480)))



    pressed_keys = pygame.key.get_pressed()
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
