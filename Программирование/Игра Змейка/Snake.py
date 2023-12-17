import pygame, random, time
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

step=30 #одна клека
width, height=step*30, step*17 #размер окна

#слуйчайные координаты появления змейки
x1=step*6
y1=step*6
x2=step*20
y2=step*3
#слуйчайные координаты появления яблока
apple_x=step*20
apple_y=step*13
#случайный цвет яблока
color=[(157,120,249),(246,240,126),(111,238,244),(141,172,226),(197,140,245)]
apple_color=random.choice(color)

length_1=1
length_2=1
snake_1=[(x1, y1)]
snake_2=[(x2, y2)]

#направления змейки
dx_1=0
dy_1=0
dx_2=0
dy_2=0

speed=7 #скорость

pygame.init()
sc=pygame.display.set_mode([width, height])
clock=pygame.time.Clock()

score=0
font_score=pygame.font.SysFont('Arial', 25, bold=True)
font_text=pygame.font.SysFont('Arial', 15)
font_keys=pygame.font.SysFont('Arial', 35, bold=True)
font_end=pygame.font.SysFont('Arial', 106, bold=True)
render_end = font_end.render('GAME OVER', 1, (255, 255, 255))

text_restart = font_score.render('ЧТОБЫ НАЧАТЬ ЗАНОВО НАЖМИТЕ R', 1, (255, 255, 255))
text_snake = font_score.render('ВАША ЗМЕЙКА', 1, (111, 89, 190))
text_enemy = font_score.render('ВРАЖЕСКАЯ ЗМЕЙКА', 1, (111, 89, 190))
text_keys = font_keys.render('НАЖМИТЕ ЛЮБУЮ ИЗ КЛАВИШ WASD ИЛИ ← → ↑ ↓', 1, (255, 255, 255))
text_apple = font_score.render('ЯБЛОКО', 1, (111, 89, 190))
text_music = font_text.render('ПОСТАВИТЬ ФОНОВУЮ МУЗЫКУ НА ПАУЗУ', 1, (232, 225, 255))
text_score = font_text.render('КОЛИЧЕСТВО СЪЕДЕННЫХ ЯБЛОК', 1, (232, 225, 255))
text_wall = font_score.render('В СТЕНУ ВРЕЗАТЬСЯ НЕЛЬЗЯ!', 1, (111, 89, 190))

key=0
background=pygame.image.load('background.png').convert()

pygame.mixer.music.load('John-Cage-In-A-Landscape.mp3')
pygame.mixer.music.play(-1)

portal = pygame.mixer.Sound('portal.wav')
apple = pygame.mixer.Sound('apple.wav')
end_sound = pygame.mixer.Sound('end.wav')
click = pygame.mixer.Sound('click.wav')

pygame.mixer.pre_init()
pygame.mixer.init()

def game_over(end):
    # пишем game over
    #sc.fill((122, 186, 255))
    sc.blit(background, (0, 0))
    sc.blit(render_end, (170, 140))
    sc.blit(render_score, (400, 265))
    sc.blit(text_restart, (10, 10))
    text_gameover = font_score.render(end, 1, (111, 89, 190))
    sc.blit(text_gameover, (300,300))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
        elif event.type == pygame.QUIT:
            exit()
c=0 #флаг конца игры
c1=0 #флаг начала игры
pause=False

running=True
while running:
    #sc.fill((122, 186, 255))
    sc.blit(background, (0, 0))

    if c1==0:
        sc.blit(text_snake, (120, 140))
        sc.blit(text_enemy, (530, 50))
        sc.blit(text_apple, (575, 350))
        sc.blit(text_score, (10,0))
        sc.blit(text_music, (10,75))
        sc.blit(text_keys, (60,250))
        sc.blit(text_wall, (30,470))

    if not pause:
        pygame.mixer.music.unpause()
        pygame.draw.rect(sc, (255, 255, 255), (15, 50, 5, 20))
        pygame.draw.rect(sc, (255, 255, 255), (25, 50, 5, 20))
    else:
        pygame.mixer.music.pause()
        pygame.draw.polygon(sc, (255, 255, 255), [[15, 50], [30, 60], [15, 70]])


    #клеточки
    '''for i in range(0, width, step):
        for j in range(0, height, step):
            pygame.draw.rect(sc, (255, 255, 255),(i, j, step, step), 1)'''

    #рисуем змейку
    for i, j in snake_1[-1:]: #голова змейки
        #pygame.draw.rect(sc, (255, 255, 255), (i, j, step, step))
        #pygame.draw.rect(sc, (187,174,234), (i+2, j+2, step - 4, step - 4))
        pygame.draw.circle(sc, (149,131,213), (i+(step//2), j+(step//2)), step // 2+2)
        pygame.draw.circle(sc, (187,174,234), (i+(step//2), j+(step//2)), step // 2)

        #глаза змейки
        if dx_1==1 or not c1:
            pygame.draw.circle(sc, (149,131,213), (i, j+(step//2)), step // 2+2)
        elif dx_1==-1:
            pygame.draw.circle(sc, (149,131,213), (i+step, j+(step//2)), step // 2+2)
        elif dy_1==1:
            pygame.draw.circle(sc, (149,131,213), (i+(step//2), j), step // 2+2)
        elif dy_1==-1:
            pygame.draw.circle(sc, (149,131,213), (i+(step//2), j+step), step // 2+2)

        if dx_1 == 1 or not c1:
            pygame.draw.circle(sc, (187, 174, 234), (i, j + (step // 2)), step // 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 7, j + (step // 2) - 5), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 7, j + (step // 2) + 5), 2)
        elif dx_1 == -1:
            pygame.draw.circle(sc, (187, 174, 234), (i + step, j + (step // 2)), step // 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 7, j + (step // 2) - 5), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 7, j + (step // 2) + 5), 2)
        elif dy_1 == 1:
            pygame.draw.circle(sc, (187, 174, 234), (i + (step // 2), j), step // 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 5, j + (step // 2) + 7), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 5, j + (step // 2) + 7), 2)
        elif dy_1 == -1:
            pygame.draw.circle(sc, (187, 174, 234), (i + (step // 2), j + step), step // 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 5, j + (step // 2) - 7), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 5, j + (step // 2) - 7), 2)

    for i, j in snake_1[:-1]: #тело змейки
        #pygame.draw.rect(sc, (255, 255, 255), (i, j, step, step))
        #pygame.draw.rect(sc, (111, 89, 190), (i+2, j+2, step - 4, step - 4))
        pygame.draw.circle(sc, (87,65,169), (i+(step//2), j+(step//2)), step // 2+2)

        if dx_1==1:
            pygame.draw.circle(sc, (87,65,169), (i, j+(step//2)), step // 2+2)
        elif dx_1==-1:
            pygame.draw.circle(sc, (87,65,169), (i+step, j+(step//2)), step // 2+2)
        elif dy_1==1:
            pygame.draw.circle(sc, (87,65,169), (i+(step//2), j), step // 2+2)
        elif dy_1==-1:
            pygame.draw.circle(sc, (87,65,169), (i+(step//2), j+step), step // 2+2)

        if dx_1==1:
            pygame.draw.circle(sc, (111, 89, 190), (i, j+(step//2)), step // 2)
        elif dx_1==-1:
            pygame.draw.circle(sc, (111, 89, 190), (i+step, j+(step//2)), step // 2)
        elif dy_1==1:
            pygame.draw.circle(sc, (111, 89, 190), (i+(step//2), j), step // 2)
        elif dy_1==-1:
            pygame.draw.circle(sc, (111, 89, 190), (i+(step//2), j+step), step // 2)

        pygame.draw.circle(sc, (111, 89, 190), (i+(step//2), j+(step//2)), step // 2)

    #рисуем вражескую змейку
    for i, j in snake_2:
        pygame.draw.rect(sc, (255, 255, 255), (i, j, step, step))
        pygame.draw.rect(sc, (136,239,236), (i+2, j+2, step - 4, step - 4))
    for i, j in snake_2[-1:]: #голова змейки
        if dx_2 == 1 or not c1:
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 7, j + (step // 2) - 5), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 7, j + (step // 2) + 5), 2)
        elif dx_2 == -1:
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 7, j + (step // 2) - 5), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 7, j + (step // 2) + 5), 2)
        elif dy_2 == 1:
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 5, j + (step // 2) + 7), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 5, j + (step // 2) + 7), 2)
        elif dy_2 == -1:
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) - 5, j + (step // 2) - 7), 2)
            pygame.draw.circle(sc, (0, 0, 0), (i + (step // 2) + 5, j + (step // 2) - 7), 2)

    #рисуем яблоко
    pygame.draw.circle(sc, (255, 255, 255), (apple_x+(step//2)-5, apple_y+(step//2)), step // 2)
    pygame.draw.circle(sc, (255, 255, 255), (apple_x+(step//2)+5, apple_y+(step//2)), step // 2)
    pygame.draw.circle(sc, apple_color, (apple_x+(step//2)-5, apple_y+(step//2)), step // 2-2)
    pygame.draw.circle(sc, apple_color, (apple_x+(step//2)+5, apple_y+(step//2)), step // 2-2)
    pygame.draw.circle(sc, (255, 255, 255), (apple_x+(step//2)+10, apple_y+(step//2)-6), 3)
    pygame.draw.rect(sc, (0,0,0), (apple_x+(step//2)-1, apple_y+(step//2)-20, 2, 13))
    '''pygame.draw.rect(sc, (255, 255, 255),(apple_x, apple_y,step,step))
    pygame.draw.rect(sc, (apple_color),(apple_x+4, apple_y+4,step-8,step-8))'''


    render_score=font_score.render('SCORE:' + str(score), 1, (255, 255, 255))
    sc.blit(render_score, (15,15))

    #шаг змейки
    x1+=dx_1*step
    y1+=dy_1*step

    #шаг вражеской змейки
    dx_2=0
    dy_2=0
    if x2<apple_x and dx_2!=-1:
        if c1 and not c:
            dx_2=1
            x2+=step*0.5
    elif x2>apple_x and dx_2!=1:
        if c1 and not c:
            dx_2=-1
            x2-=step*0.5
    elif y2<apple_y and dy_2!=-1:
        if c1 and not c:
            dy_2=1
            y2+=step*0.5
    elif y2>apple_y and dy_2!=1:
        if c1 and not c:
            dy_2=-1
            y2-=step*0.5


    snake_1.append((x1, y1))
    snake_2.append((x2, y2))
    snake_1=snake_1[-length_1:] #срез по длине змейки
    snake_2=snake_2[-length_2:]

    #кушаем яблоко
    if snake_1[-1]==(apple_x, apple_y):
        apple.play()
        apple_color=random.choice(color)
        apple_x=random.randrange(step, width-step, step)
        apple_y=random.randrange(step, height-step, step)
        length_1+=1
        speed+=1
        score+=1

    #вражеская змейка кушает яблоко
    if snake_2[-1]==(apple_x, apple_y):
        apple.play()
        apple_color=random.choice(color)
        apple_x=random.randrange(step, width-step, step)
        apple_y=random.randrange(step, height-step, step)
        length_2+=1

    #змейка врезалась в стену
    if x1 < 0 or y1 < 0 or x1 > width or y1 > height:
        if c == 0:
            portal.play()
            c += 1
        end='Змейка разбилась об стену'
        game_over(end)

    '''
    #проход змейки через края экрана
    if x < 0:
        x=width
        portal.play()
    elif y < 0:
        y=height
        portal.play()
    elif x > width - step:
        x=0-step
        portal.play()
    elif y > height - step:
        y=0-step
        portal.play()'''

    #если змейка врезалась сама в себя
    if len(snake_1) != len(set(snake_1)):
        while True:
            if c==0:
                end_sound.play()
                c+=1
            end='Змейка сама в себя врезалась'
            game_over(end)
    '''
    if len(snake_2) != len(set(snake_2)):
        length_2=1'''

    '''
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE: #выход из программы
                running = False
            #нажатие клавиш для управления змейкой
            if event.key == K_UP or event.key == K_w: #проверка последней нажатой клавиши, чтобы не идти в сторону тела змейки
                if dy!=1:
                    time.sleep(0.05)
                    click.play()
                    c1=1
                    dx = 0
                    dy = -1
            if event.key == K_DOWN or event.key == K_s:
                if dy!=-1:
                    time.sleep(0.05)
                    click.play()
                    c1=1
                    dx = 0
                    dy = 1
            if event.key == K_RIGHT or event.key == K_d:
                if dx!=-1:
                    time.sleep(0.05)
                    click.play()
                    c1=1
                    dx = 1
                    dy = 0
            if event.key == K_LEFT or event.key == K_a:
                if dx!=1:
                    time.sleep(0.05)
                    click.play()
                    c1=1
                    dx = -1
                    dy = 0
        elif event.type == QUIT: #выход из программы
            running = False
        '''

    # нажатие клавиш для управления змейкой
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
        if dy_1!=1:
            time.sleep(0.05)
            click.play()
            c1=1
            dx_1 = 0
            dy_1 = -1
    if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
        if dy_1!=-1:
            time.sleep(0.05)
            click.play()
            c1=1
            dx_1 = 0
            dy_1 = 1
    if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        if dx_1!=-1:
            time.sleep(0.05)
            click.play()
            c1=1
            dx_1 = 1
            dy_1 = 0
    if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        if dx_1!=1:
            time.sleep(0.05)
            click.play()
            c1=1
            dx_1 = -1
            dy_1 = 0
    #рестарт
    if c!=0 and pressed_keys[pygame.K_r]:
        length_1=1
        length_2=1
        x1 = step * 6
        y1 = step * 6
        x2 = step * 20
        y2 = step * 3
        apple_x=step*20
        apple_y=step*13
        snake_1=[(x1, y1)]
        snake_2=[(x2, y2)]
        score=0
        dx_1=0
        dy_1=0
        dx_2=0
        dy_2=0
        speed=7
        c = 0
        c1 = 0



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:  # выход из программы
                running = False
        elif event.type == QUIT:  # выход из программы
            running = False
        #нажатие на кнопку паузы
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not pause and pygame.mouse.get_pos()[0]>=10 and pygame.mouse.get_pos()[0]<=28 and pygame.mouse.get_pos()[1]>=45 and pygame.mouse.get_pos()[1]<=75:
                pause=True
            elif pause and pygame.mouse.get_pos()[0]>=10 and pygame.mouse.get_pos()[0]<=28 and pygame.mouse.get_pos()[1]>=45 and pygame.mouse.get_pos()[1]<=75:
                pause=False

    pygame.display.flip()
    clock.tick(speed)
pygame.quit()