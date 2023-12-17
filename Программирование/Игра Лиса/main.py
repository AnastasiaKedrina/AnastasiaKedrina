import pygame
import random
import tkinter as tk

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
    QUIT,
    RLEACCEL
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 533

playerSprite = pygame.sprite.Sprite()

first_enemySprite = pygame.sprite.Sprite()
second_enemySprite = pygame.sprite.Sprite()
third_enemySprite = pygame.sprite.Sprite()

first_enemySpeed = 0
second_enemySpeed = 0
third_enemySpeed = 0

def playerInit():
    global playerSprite
    playerSprite.image = pygame.image.load("fox.png").convert()
    playerSprite.image.set_colorkey((0,0,0),RLEACCEL)
    playerSprite.rect = playerSprite.image.get_rect()

def playerUpdate(pressed_keys):
    global playerSprite
    if pressed_keys[K_UP] or pressed_keys[K_w]:
        playerSprite.rect.move_ip(0,-7)
    if pressed_keys[K_DOWN] or pressed_keys[K_s]:
        playerSprite.rect.move_ip(0, 7)
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        playerSprite.rect.move_ip(-7,0)
    if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        playerSprite.rect.move_ip(7,0)

    if playerSprite.rect.left < 0:
        playerSprite.rect.left = 0
    if playerSprite.rect.right > SCREEN_WIDTH:
        playerSprite.rect.right=SCREEN_WIDTH
    if playerSprite.rect.top <=0:
        playerSprite.rect.top=0
    if playerSprite.rect.bottom >= SCREEN_HEIGHT:
        playerSprite.rect.bottom=SCREEN_HEIGHT

def enemyInit():
    global first_enemySpeed, second_enemySpeed, third_enemySpeed
    global first_enemySprite, second_enemySprite, third_enemySprite

    first_enemySprite.image = pygame.image.load("fly.png").convert()
    second_enemySprite.image= pygame.image.load("fly.png").convert()
    third_enemySprite.image= pygame.image.load("fly.png").convert()

    first_enemySprite.image.set_colorkey((0,0,0),RLEACCEL)
    second_enemySprite.image.set_colorkey((0,0,0),RLEACCEL)
    third_enemySprite.image.set_colorkey((0,0,0),RLEACCEL)

    first_enemySprite.rect = playerSprite.image.get_rect(
        center=(
            random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
            random.randint(0, SCREEN_HEIGHT),))
    second_enemySprite.rect= playerSprite.image.get_rect(
        center=(
            random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
            random.randint(0, SCREEN_HEIGHT),))
    third_enemySprite.rect= playerSprite.image.get_rect(
        center=(
            random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
            random.randint(0, SCREEN_HEIGHT),))

    first_enemySpeed = random.randint(10,20)
    second_enemySpeed = random.randint(3, 10)
    third_enemySpeed = random.randint(20, 30)


def enemyUpdate():
    global first_enemySprite, second_enemySprite, third_enemySprite
    first_enemySprite.rect.move_ip(-first_enemySpeed, 0)
    second_enemySprite.rect.move_ip(-second_enemySpeed, 0)
    third_enemySprite.rect.move_ip(-third_enemySpeed, 0)
    if first_enemySprite.rect.right < 0:
        first_enemySprite.rect = first_enemySprite.image.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 80),
                random.randint(25, SCREEN_HEIGHT-10),
            )
        )
    if second_enemySprite.rect.right < 0:
        second_enemySprite.rect = second_enemySprite.image.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 80),
                random.randint(25, SCREEN_HEIGHT-10),
            )
        )
    if third_enemySprite.rect.right < 0:
        third_enemySprite.rect = third_enemySprite.image.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 80),
                random.randint(25, SCREEN_HEIGHT-10),
            )
        )
pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def continue_game():
    baseWindow.destroy()
def exit_game():
    #pygame.quit()
    #baseWindow.destroy()
    quit()



playerInit()
enemyInit()
clock=pygame.time.Clock()
running=True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running=False
        elif event.type== QUIT:
            running=False

    pressed_keys = pygame.key.get_pressed()
    playerUpdate(pressed_keys)
    enemyUpdate()

    if pygame.sprite.collide_mask(playerSprite, first_enemySprite) or pygame.sprite.collide_mask(playerSprite, second_enemySprite) or pygame.sprite.collide_mask(playerSprite, third_enemySprite):

        baseWindow = tk.Tk()
        baseWindow.title('GameOver')
        baseWindow.geometry('300x200+600+300')
        baseWindow['bg'] = '#570B0E'

        text = tk.Label(baseWindow, text='Вы проиграли!', font='Arial 24', bg='#570B0E', fg='#F0D7B1')
        text.place(x='40', y='20')
        button1 = tk.Button(baseWindow, text='Ещё раз', width='15', font='Arial 16', bg='#EAA365', fg='#570B0E',command=continue_game)
        button1.place(x='55', y='80')
        button2 = tk.Button(baseWindow, text='Выйти', width='15', font='Arial 16', bg='#B7271C', fg='#EFE3EB',command=exit_game)
        button2.place(x='55', y='130')

        baseWindow.mainloop()

        try:
            playerInit()
            enemyInit()
        except:
            continue

    background_image = pygame.image.load("background.jpg").convert()
    screen.blit(background_image,[0,0])


    screen.blit(playerSprite.image, playerSprite.rect)
    screen.blit(first_enemySprite.image, first_enemySprite.rect)
    screen.blit(second_enemySprite.image, second_enemySprite.rect)
    screen.blit(third_enemySprite.image, third_enemySprite.rect)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()










