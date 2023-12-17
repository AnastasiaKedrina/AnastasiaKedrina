from datetime import datetime as dt
import pygame
from pygame.locals import (K_ESCAPE,QUIT)

class Tamagotchi:
    def __init__(self, name):
        self.__name = name
        self.__amount = 0
        self.__start = dt.now()

    def food(self, food_amount):
        if int(food_amount)>0:
            return str(round(self.__amount + int(food_amount)/50))

    def get_mood(self):
        a = ['смерть', 'расстроенный', 'нейтрально', 'довольный', 'счастливый', 'злой','очень злой']
        x=0
        for i in range(-10, 21, 5):
            if int(hungry_count) <= i*10:
                x=1
                return a[(i + 10) // 5]
                break
        if x==0:
            return a[0]

    def get_food(self):
        a=['смерть','очень голодный','голодный','в норме','сытый','переел','сильно переел']
        x = 0
        for i in range(-10, 21, 5):
            if int(hungry_count) <= i * 10:
                x = 1
                return a[(i + 10) // 5]
                break
        if x == 0:
            return a[0]

    def time(self, now):
        dif = (now - self.__start).seconds
        self.__start = dt.now()
        return dif

    for propert in ['get_food', 'get_mood']:
        locals()[propert]=property(locals()[propert])

stich = Tamagotchi('Stich')

screen=pygame.display.set_mode((889, 605))
pygame.init()
clock=pygame.time.Clock()

food_amount = '0'
hungry_count = '0'
life= 'alive'
dif_plus='0'
dif_minus='0'

running=True
while running:
    #Закрытие окна
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
        if event.type == QUIT:
            running = False
            pygame.quit()

    #Фон
    background_image = pygame.image.load('image/background.jpg').convert()
    screen.fill((143,206,224))
    screen.blit(background_image, [0, 105])

    happy_stich = pygame.image.load('image/happy.png').convert_alpha()
    pleased_stich = pygame.image.load('image/pleased.png').convert_alpha()
    okay_stich = pygame.image.load('image/okay.png').convert_alpha()
    upset_stich = pygame.image.load('image/upset.png').convert_alpha()
    angry_stich = pygame.image.load('image/angry.png').convert_alpha()
    dead_stich = pygame.image.load('image/dead.png').convert_alpha()
    game_over = pygame.image.load('image/game_over.png').convert_alpha()
    love = pygame.image.load('image/love.png').convert_alpha()
    hp = pygame.image.load('image/hp.jpg')

    pygame.draw.rect(screen, (0, 0, 0), (0, 100, 889, 5))

    font_1 = pygame.font.Font(None, 54)
    font_2 = pygame.font.Font(None, 24)
    font_3 = pygame.font.Font(None, 16)
    font_4 = pygame.font.Font(None, 30)
    font_5 = pygame.font.Font(None, 104)
    if life == 'alive':
        pygame.draw.rect(screen, (112, 178, 202), (40, 15, 400, 70))
        food_btn = font_1.render('Проверить Стича', True, (0, 0, 0))
        screen.blit(food_btn, food_btn.get_rect(center=(240, 50)))
    else:
        pygame.draw.rect(screen, (112, 178, 202), (240, 15, 400, 70))
        food_btn = font_1.render('Стич умер :(', True, (0, 0, 0))
        screen.blit(food_btn, food_btn.get_rect(center=(440, 50)))

    if life != 'dead':
        food_count = font_2.render('Сколько еды вы хотите дать Стичу?', True, (0, 0, 0))
        screen.blit(food_count, food_count.get_rect(center=(650, 20)))

        pygame.draw.rect(screen, (112, 178, 202), (560, 50, 180, 40))
        food_count = font_3.render('Выберите количество колесиком мыши', True, (0, 0, 0))
        screen.blit(food_count, food_count.get_rect(center=(650, 40)))

        food_count = font_1.render(food_amount, True, (0, 0, 0))
        screen.blit(food_count, food_count.get_rect(center=(650, 70)))

    pygame.draw.rect(screen, (255, 255, 255), (40, 125, 380, 115))
    pygame.draw.rect(screen, (143, 206, 224), (60, 170, 280, 40))
    text_mood = font_4.render('настроение: ' + stich.get_mood, True, (0, 0, 0))
    text_hungry = font_4.render('голод: ' + stich.get_food, True, (0, 0, 0))
    screen.blit(text_mood, text_mood.get_rect(center=(220, 150)))
    screen.blit(text_hungry, text_hungry.get_rect(center=(190, 190)))

    pygame.draw.rect(screen, (112, 178, 202), (320, 170, 60, 40))
    text_hungry_count = font_4.render(hungry_count, True, (0, 0, 0))
    screen.blit(text_hungry_count, text_hungry_count.get_rect(center=(350, 190)))

    screen.blit(hp, [63, 215])

    if int(hungry_count) <= -100 or int(hungry_count) >200:
        screen.blit(dead_stich, [230, 295])
        screen.blit(game_over, [360, 165])
        pygame.draw.rect(screen, (255,255,255), (270, 215, 110, 20))
    elif int(hungry_count) > -100 and int(hungry_count) <= -50:
        screen.blit(upset_stich, [250, 285])
        pygame.draw.rect(screen, (255,255,255), (40, 215, 100, 20))
        pygame.draw.rect(screen, (255,255,255), (270, 215, 110, 20))
        pygame.draw.circle(screen, (12, 78, 102), (140,222), 8)
    elif int(hungry_count) > -50 and int(hungry_count) <= 0:
        screen.blit(okay_stich, [250, 285])
        pygame.draw.rect(screen, (255,255,255), (40, 215, 140, 20))
        pygame.draw.rect(screen, (255,255,255), (270, 215, 110, 20))
        pygame.draw.circle(screen, (12, 78, 102), (180,222), 8)
    elif int(hungry_count) > 0 and int(hungry_count) <= 50:
        screen.blit(pleased_stich, [200, 245])
        pygame.draw.rect(screen, (255,255,255), (40, 215, 140, 20))
        pygame.draw.rect(screen, (255,255,255), (300, 215, 80, 20))
        pygame.draw.circle(screen, (12, 78, 102), (300,222), 8)
    elif int(hungry_count) > 50 and int(hungry_count) <= 100:
        screen.blit(happy_stich, [240, 205])
        pygame.draw.rect(screen, (255,255,255), (40, 215, 140, 20))
        pygame.draw.rect(screen, (255,255,255), (340, 215, 40, 20))
        pygame.draw.circle(screen, (12, 78, 102), (340,222), 8)
    elif int(hungry_count) > 100:
        screen.blit(angry_stich, [270, 285])
        pygame.draw.rect(screen, (255,255,255), (40, 215, 140, 20))
        pygame.draw.circle(screen, (12, 78, 102), (380,222), 8)

    if stich.get_food == 'смерть':
        life='dead'

    pygame.draw.rect(screen, (173,236,254), (780,565, 109, 40))
    text_mood = font_4.render('Выйти', True,(63,126,144))
    screen.blit(text_mood, text_mood.get_rect(center=(835,585)))

    if int(dif_plus)>=0:
        food_plus = font_2.render('+' + dif_plus, True, (0, 0, 0))
    else:
        food_plus = font_2.render('+0', True, (0, 0, 0))
    screen.blit(food_plus, food_plus.get_rect(center=(400, 205)))
    food_minus = font_2.render('-' + dif_minus, True, (0, 0, 0))
    screen.blit(food_minus, food_minus.get_rect(center=(400, 185)))

    cursor = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: #колесико мыши вверх
                food_amount = str(int(food_amount)+1)
            elif event.button == 5: #колесико мыши вниз
                if int(food_amount)-1>=0:
                    food_amount = str(int(food_amount)-1)

            elif event.button == 1 and life != 'dead':
                if cursor[0] > 40 and cursor[0] < 440 and cursor[1] > 15 and cursor[1] < 85:
                    x1=hungry_count
                    stich.food(int(food_amount))
                    if int(food_amount)>=0:
                        hungry_count=str(int(hungry_count)+int(food_amount))
                    now = dt.now()
                    hungry_count= str(int(hungry_count) - stich.time(now)*10)
                    dif_plus=food_amount
                    dif_minus = str(int(hungry_count)-int(x1)-int(dif_plus))
                    food_amount='0'
            if event.button == 1 and cursor[0] > 780 and cursor[0] < 889 and cursor[1] > 565 and cursor[1] < 605:
                running=False

        if event.type == pygame.MOUSEMOTION:
                if life!='dead' and stich.get_mood!='злой':
                    if cursor[0] > 263 and cursor[0] < 516 and cursor[1] > 292 and cursor[1] < 568:
                        screen.blit(love, [230, 205])

    if ((cursor[0] > 40 and cursor[0] < 440 and cursor[1] > 15 and cursor[1] < 85)and life!='dead') or (cursor[0] > 780 and cursor[0] < 889 and cursor[1] > 565 and cursor[1] < 605):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()
pygame.quit()




        
