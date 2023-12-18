import pygame
import sys
from pygame.locals import *
import random

pygame.init()
font = pygame.font.Font(None, 30) #удалить эту строку и передать нужный шрифт при вызове функции, как в puzzle_game
pygame.mixer.init()
run_sound = pygame.mixer.Sound('sounds/train_game.wav')

def train_game(background_scene, font):
    """Функция при проигрыше возвращает 0, при выигрыше 1"""

    FPS = 60
    clock = pygame.time.Clock()

    width, height = 1280, 650
    screen = pygame.display.set_mode((width, height))

    counter, text = 15, '15'
    pygame.time.set_timer(pygame.USEREVENT, 1500)
    screen.blit(pygame.image.load(background_scene), (0, 0))


    class Bullet(pygame.sprite.Sprite):
        """Класс для создания пуль"""

        def __init__(self, speed):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("assets/bullet.png").convert_alpha()
            self.rect = self.image.get_rect(center = (random.randint(375, 875), 0))
            self.speed = speed

        def update(self):
            if self.rect.y < height:
                self.rect.y += self.speed
            else:
                self.rect.y = 0
                self.rect.x = random.randint(375, 875)


    class Detective(pygame.sprite.Sprite):
        """Класс для создания главного героя"""

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("assets/avoid_game.png").convert_alpha()
            self.rect = self.image.get_rect(center=(width/2, 600))

        def draw(self, surface):
            surface.blit(self.image, self.rect)

        def update(self):
            pressed_keys = pygame.key.get_pressed()
            if self.rect.left > 375:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)

            if self.rect.right < 875:
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)


    class Background:
        """Класс для двигающегося фона"""

        def __init__(self):
            self.bgimage = pygame.image.load('location/roof.png')
            self.rectBGimg = self.bgimage.get_rect()

            self.bgY1 = 0
            self.bgX1 = 315

            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 315

            self.moving_speed = 2

        def update(self):
            self.bgY2 += self.moving_speed
            self.bgY1 += self.moving_speed
            if self.bgY2 >= self.rectBGimg.height:
                self.bgY2 = -self.rectBGimg.height
            if self.bgY1 >= self.rectBGimg.height:
                self.bgY1 = -self.rectBGimg.height

        def render(self):
            screen.blit(self.bgimage, (self.bgX1, self.bgY1))
            screen.blit(self.bgimage, (self.bgX2, self.bgY2))

    def game_over(game_over_text):
        pygame.time.wait(1000)
        surf = pygame.Surface((650, 650))
        surf.fill((0, 0 , 0))
        rect = pygame.Rect((315, 0, 0, 0))
        screen.blit(surf, rect)
        screen.blit(font.render(game_over_text, True, (255, 255, 255)), (560, 200))
        pygame.display.update()
        pygame.time.wait(2700)
            

    detective = Detective()
    back_ground = Background()

    bullet1 = Bullet(4.6)
    bullet2 = Bullet(4)
    bullet3 = Bullet(4)
    bullet4 = Bullet(6)
    bullet5 = Bullet(4)
    bullets = pygame.sprite.Group()
    bullets.add(bullet1, bullet2, bullet3, bullet4, bullet5)

    running = True
    run_sound.play()
    run_sound.set_volume(0.2)

    while running:
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter)
                else:
                    run_sound.set_volume(0.0)
                    game_over('Вы выиграли.')
                    return 1

        if pygame.sprite.spritecollideany(detective, bullets):
            run_sound.set_volume(0.0)
            game_over('Вы проиграли.')
            return 0

        back_ground.update()
        back_ground.render()

        bullets.draw(screen)
        detective.draw(screen)

        bullets.update()
        detective.update()
        
        screen.blit(font.render(text, True, (255, 255, 255)), (620, 48))

        pygame.display.update()
        clock.tick(FPS)

