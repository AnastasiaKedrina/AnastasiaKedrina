import pygame
from button import Button
from font import title_font, blit_text
from game import set_cursor, pygame_btn_quit, game
def main_menu():
    menu_width = 1280
    menu_height = 650
    menu_dis = pygame.display.set_mode((menu_width, menu_height))
    pygame.mixer.music.load('sounds/menu.wav')
    pygame.mixer.music.play()

    def options():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            menu_dis.fill('#020c26')

            text_description = 'Вы – великий сыщик Эркюль Пуаро.  Возвращаетесь в Англию на поезде,  в котором вместе с вами едут представители всех возможных национальностей.  На следующий день в одном из купе находят мертвое тело американца.  Поезд наглухо застревает в снежных заносах.  Ваша задача найти убийцу до того,  как экспресс продолжит свой путь...'

            # рендер текста с автоматическим переносом строк
            blit_text(menu_dis, text_description, title_font(28), (255, 255, 255), (0, 0), 50)

            OPTIONS_BACK = Button(image=None, pos=(menu_height, 550),
                                  text_input='НАЗАД', font=title_font(28), base_color='#696969', hovering_color='white')

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(menu_dis)

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()

            set_cursor(menu_dis)
            pygame.display.update()

    running = True
    while running:
        menu_dis.blit(pygame.image.load('assets/back.jpg'), (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        base_color = '#000000'
        hovering_color = '#0f3739'
        PLAY_BUTTON = Button(image=pygame.image.load('assets/Play.png'), pos=(200, 150),
                             text_input='ИГРАТЬ', font=title_font(80), base_color=base_color, hovering_color=hovering_color)
        OPTIONS_BUTTON = Button(image=pygame.image.load('assets/Options.png'), pos=(255, 300),
                                text_input='ОПИСАНИЕ', font=title_font(80), base_color=base_color,
                                hovering_color=hovering_color)
        QUIT_BUTTON = Button(image=pygame.image.load('assets/Quit.png'), pos=(200, 450),
                             text_input='ВЫХОД', font=title_font(78), base_color=base_color, hovering_color=hovering_color)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(menu_dis)

        for event in pygame.event.get():
            pygame_btn_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # нажатие на кнопку 'играть' запускает функцию игры
                    pygame.mixer.music.stop()
                    game()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False
                    quit()
        set_cursor(menu_dis)
        pygame.display.update()
