import pygame

pygame.init()
counter = 0


def find_puzzle_game(background_scene):
    W = 1280
    H = 650
    WHITE = (255, 255, 255)
    BEIGE = (185, 146, 103)
    DARK_BEIGE = (148, 95, 81)
    window = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    bg = pygame.image.load('location/cafe.png')
    window.blit(pygame.image.load(background_scene), (0, 0))
    font = pygame.font.SysFont('Arial', 50)
    text = font.render('Вы нашли части пазла!', True, DARK_BEIGE)
    textRect = text.get_rect()
    textRect.center = (W // 2, H // 2)
    pygame.display.set_caption("Мини-игра с поиском фрагментов пазла")
    find_sound = pygame.mixer.Sound('sounds/get_puzzle_piece.wav')

    class SpriteObject(pygame.sprite.Sprite):
        def __init__(self, x, y, color):
            super().__init__()
            self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.rect(self.original_image, color, (30, 30, 20, 20))
            self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.rect(self.click_image, color, (30, 30, 20, 20))
            pygame.draw.rect(self.click_image, WHITE, (30, 30, 20, 20), 2)
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(x, y))
            self.clicked = False

        def update(self, event_list):
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        global counter
                        if not self.clicked:
                            counter += 1
                            find_sound.play()
                        else:
                            counter -= 1
                        self.clicked = not self.clicked

            self.image = self.click_image if self.clicked else self.original_image

    group = pygame.sprite.Group([
        SpriteObject(window.get_width() // 3, window.get_height() // 11, BEIGE),
        SpriteObject(window.get_width() // 1.7, window.get_height() // 2, BEIGE),
        SpriteObject(window.get_width() // 3, window.get_height() * 2 // 3, BEIGE),
        SpriteObject(window.get_width() * 2 // 3, window.get_height() * 2 // 3, BEIGE),
    ])
    game_over = False
    run = True
    while run:
        clock.tick(60)
        window.blit(bg, (0, 0))
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    run = False

        group.update(event_list)

        group.draw(window)
        if counter == 4:
            pygame.draw.rect(window, (255, 255, 255),
                             (0, 0, 1280, 650))
            window.blit(text, textRect)
            game_over = True
        coord = pygame.mouse.get_pos()
        cursor = pygame.image.load('assets/cursor.png')
        window.blit(cursor, coord)
        #set_cursor(window)
        pygame.display.update()
