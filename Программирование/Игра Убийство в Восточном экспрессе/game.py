import pygame
from button import Button
from heroes import Heroes
from font import blit_text
from font import dialogue_font
from puzzle_game import puzzle_game
from train_game import train_game
from find_puzzle import find_puzzle_game

pygame.init()
pygame.display.set_caption('Убийство в «Восточном экспрессе»')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
cursor = pygame.image.load('assets/cursor.png')
pygame.mouse.set_visible(False)
scary_sound = pygame.mixer.Sound('sounds/the_bloody_compartment.wav')


def set_cursor(screen):
    coord = pygame.mouse.get_pos()
    screen.blit(cursor, coord)


def pygame_btn_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()


def plot_dict():
    file = open('plot/plot.txt', encoding='utf-8')
    f = file.readlines()
    file.close()

    branches = []
    branches_num = []
    scenes = {}
    cur_scene = ''
    for i in range(len(f)):
        if 'branch' in f[i]:
            branches.append(f[i][:-1])
            branches_num.append(i)
            globals()[f[i][:-1]] = {}

        elif 'scene' in f[i]:
            scenes[f[i][:-1]] = i
            cur_scene = f[i][:-1]
            globals()[cur_scene + '_dialogue'] = []
            globals()[cur_scene + '_button'] = []

        elif 'button' in f[i]:
            globals()[cur_scene + '_button'].append(f[i].split(':')[1:])

        elif ':' in f[i]:
            globals()[cur_scene + '_dialogue'].append(f[i].split(':'))
    branches_num.append(len(f))
    branches.append('')
    return [branches, branches_num, scenes]


def game():
    scene_width = 1280
    scene_height = 650
    scene_dis = pygame.display.set_mode((scene_width, scene_height))
    dialogue_font_size = 22
    title_font_size = 32
    white = (255, 255, 255)

    x = 300
    poirot = Heroes('Эркюль', 'Пуаро', 'assets/main_character.png', x)  # Hercule Poirot
    macqueen = Heroes('Гектор', 'Маккуин', 'assets/konductor_1.png', x)  # Hector MacQueen
    waiter = Heroes('Официант', 'Стивен', 'assets/waiter.png', x)  # Официант Стивен

    # цвет кнопок
    base_color = '#EBF9FF'
    hovering_color = '#1b1b1b'

    branches, branches_num, scenes = plot_dict()
    for i in range(len(branches) - 1):
        for scene, scene_num in scenes.items():
            if scene_num > branches_num[i] and scene_num < branches_num[i + 1]:
                globals()[branches[i]][scene] = ()

    def get_text(current_scene, btn=False):
        # возвращает текст из файла для нужной сцены
        for branch in branches[:-1]:
            for scene, value in globals()[branch].items():
                if scene == current_scene:
                    if btn:
                        return [i for i in globals()[scene + '_button']]
                    else:
                        return [i for i in globals()[scene + '_dialogue']]

    def show_text(hero: str, text: str):
        # показывает диалог с изображением персонажа
        if hero == 'Автор':
            center_text(text)
        elif hero == poirot.last_name:
            poirot.draw(scene_dis)
            show_dialogue(poirot, text)
        elif hero == macqueen.last_name:
            macqueen.draw(scene_dis)
            show_dialogue(macqueen, text)
        elif hero == waiter.first_name:
            waiter.draw(scene_dis)
            show_dialogue(waiter, text)

    def location(scene, image: str):
        # отрисовка фона
        scene.blit(pygame.image.load(image), (0, 0))

    def show_dialogue(hero: str, text: str):
        # текст диалога вместе с именем персонажа
        y_text = 500
        margin = 20
        scene_dis.blit(pygame.image.load('assets/dialogue_background.png'),
                       (0, y_text - margin))
        scene_dis.blit(dialogue_font(title_font_size).render(hero.full_name, True, white),
                       (margin * 2, y_text - margin))

        blit_text(scene_dis, text, dialogue_font(
            dialogue_font_size), white, (margin, y_text + margin))

    def center_text(text: str):
        # показывает текст автора по центру окна
        scene_dis.blit(pygame.image.load('assets/back_athor.png'),
                       (40, scene_height // 3))
        blit_text(scene_dis, text, dialogue_font(
            dialogue_font_size), white, (0, scene_height // 4), 50)

    def show_puzzle(picture: str, size: int):
        # показывает паззл
        image = pygame.image.load(picture)
        width, height = 650, 650
        margin = (scene_width - width) / 2
        puzzle_game(scene_dis, width, height, size, margin, dialogue_font(
            title_font_size), image, 'location/blood_for_mini_game.png', 'Вы собрали пазл')

    def set_button(num: str, text: str):
        # возвращает кнопку выбора в игре
        if int(num) == 1:
            y = 150
        else:
            y = 350
        btn_background = 'assets/back_choice.png'
        return Button(image=pygame.image.load(btn_background), pos=(scene_width // 2, y),
                      text_input=text,
                      font=dialogue_font(dialogue_font_size),
                      base_color=base_color, hovering_color=hovering_color)

    def update_button(btn_1, btn_2, mouse_pos, scene=scene_dis):
        # показывает кнопки
        for button in [btn_1, btn_2]:
            button.changeColor(mouse_pos)
            button.update(scene)

    # -----------------start_branch
    global scene_1_intro

    def scene_1_intro():
        # Сцена 1 (предыстория)

        pygame.mixer.init()
        pygame.mixer.music.load('sounds/fon_music.wav')
        pygame.mixer.music.play(100)
        pygame.mixer.music.set_volume(0.2)

        click_count = 0
        running = True
        while running:
            location(scene_dis, 'assets/mountain.png')

            # отрисовка текста из файла
            texts = get_text('scene_1_intro')
            for i in range(len(texts)):
                if i == click_count:
                    show_text(*texts[i])

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1
                    if click_count == 1:
                        running = False

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_2_train_window

    def scene_2_train_window():
        # Сцена 2 (фон: окно поезда)
        click_count = 0
        running = True
        while running:
            location(scene_dis, 'location/day.png')

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1
                    if click_count == 1:
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound('sounds/scream.wav').play()
                    elif click_count == 2:
                        running = False

            if click_count >= 1:
                location(scene_dis, 'location/night.png')

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_3_coupe

    def scene_3_coupe():
        # Сцена 3 (фон: окровавленное купе поезда)
        scary_sound.play()
        click_count = 0  # считаем число кликов для смены диалогов внутри сцены
        running = True
        while running:
            location(scene_dis, 'location/blood.png')
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1

                    if btn_1.checkForInput(mouse_pos):
                        running = False

                    if btn_2.checkForInput(mouse_pos):
                        show_branch(ask_passengers_branch)
                        running = False

            for i in range(2):
                num, text = get_text('scene_3_coupe', True)[i]
                globals()['btn_' + str(i + 1)] = set_button(num, text[:-1])

            # отрисовка текста из файла
            texts = get_text('scene_3_coupe')
            for i in range(len(texts)):
                if i <= click_count:
                    show_text(*texts[i])

            if click_count >= 1:
                update_button(btn_1, btn_2, mouse_pos)

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_3_second_choice

    def scene_3_second_choice():
        # Сцена 3 (фон: окровавленное купе поезда) второй выбор
        running = True
        while running:
            location(scene_dis, 'location/blood.png')
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if btn_1.checkForInput(mouse_pos):
                        # pygame.mixer.music.stop()
                        show_branch(crime_scen_view_branch)
                        running = False

                    if btn_2.checkForInput(mouse_pos):
                        # pygame.mixer.music.stop()
                        show_branch(compartment_view_branch)
                        running = False

            for i in range(2):
                num, text = get_text('scene_3_second_choice', True)[i]
                globals()['btn_' + str(i + 1)] = set_button(num, text[:-1])

            update_button(btn_1, btn_2, mouse_pos)

            set_cursor(scene_dis)
            pygame.display.update()

    # -----------------crime_scen_view_branch (осмотр места преступления)
    global scene_1_blood_coupe

    def scene_1_blood_coupe():
        # Сцена 1(фон: окровавленное купе)
        click_count = 0
        running = True
        while running:
            location(scene_dis, 'location/blood.png')

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1
                    if click_count == 2:
                        running = False

            # отрисовка текста из файла
            texts = get_text('scene_1_blood_coupe')
            for i in range(len(texts)):
                if i == click_count:
                    show_text(*texts[i])

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_2_corridor

    def scene_2_corridor():
        # Сцена 2(фон: коридор поезда с купе)
        click_count = 0
        running = True
        scary_sound.set_volume(0.0)
        pygame.mixer.music.play(100)
        pygame.mixer.music.set_volume(0.2)
        while running:
            location(scene_dis, 'location/hall.png')

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1

            # отрисовка текста из файла
            texts = get_text('scene_2_corridor')
            for i in range(len(texts)):
                if i == click_count:
                    show_text(*texts[i])

            if click_count == 1:
                show_branch(ask_passengers_branch)
                running = False

            set_cursor(scene_dis)
            pygame.display.update()

    # -----------------compartment_view_branch (осмотр других кают)
    global scene_1_view_corridor

    def scene_1_view_corridor():
        # Сцена 1(фон: коридор поезда с купе)
        scary_sound.set_volume(0.0)
        pygame.mixer.music.play(100)
        pygame.mixer.music.set_volume(0.2)
        click_count = 0
        running = True
        while running:
            location(scene_dis, 'location/hall.png')

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1
                    if click_count == 3:
                        running = False

            # отрисовка текста из файла
            texts = get_text('scene_1_view_corridor')
            for i in range(len(texts)):
                if i == click_count:
                    show_text(*texts[i])

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_2_blood_coupe

    def scene_2_blood_coupe():
        # Сцена 2(фон: окровавленное купе)
        click_count = 0
        running = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound('sounds/luke.wav').play()
        while running:
            location(scene_dis, 'location/blood.png')
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1

                    if btn_1.checkForInput(mouse_pos):
                        running = False

                    if btn_2.checkForInput(mouse_pos):
                        show_branch(ask_passengers_branch)
                        running = False

            for i in range(2):
                num, text = get_text('scene_2_blood_coupe', True)[i]
                globals()['btn_' + str(i + 1)] = set_button(num, text[:-1])

            # отрисовка текста из файла
            texts = get_text('scene_2_blood_coupe')
            for i in range(len(texts)):
                if i == click_count:
                    show_text(*texts[i])

            if click_count >= 3:
                update_button(btn_1, btn_2, mouse_pos)

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_run_game

    def scene_run_game():
        # Игра уворачивалка
        click_count = 0
        win_game = False
        running = True
        pygame.mixer.music.play(100)
        pygame.mixer.music.set_volume(0.2)
        while running:
            location(scene_dis, 'location/blood.png')

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1
                    if click_count == 3:
                        show_branch(end_branch)
                        running = False

            # отрисовка текста из файла
            texts = get_text('scene_run_game')
            for i in range(len(texts)):
                if click_count >= 2:
                    if win_game:
                        location(scene_dis, 'assets/end_happy.png')
                        show_text(*texts[len(texts) - 2])
                    else:
                        location(scene_dis, 'assets/end_bad.png')
                        show_text(*texts[len(texts) - 1])

                elif click_count == len(texts) - 3:
                    win_game = train_game('location/blood_for_mini_game.png', dialogue_font(dialogue_font_size))
                    click_count += 1

                elif i == click_count:
                    show_text(*texts[i])

            set_cursor(scene_dis)
            pygame.display.update()

    # -----------------ask_passengers_branch
    global scene_1_restaurant

    def scene_1_restaurant():
        # Сцена 1 (фон: вагон ресторан)

        scary_sound.set_volume(0.0)
        pygame.mixer.music.play(100)
        pygame.mixer.music.set_volume(0.2)

        click_count = 0
        running = True
        while running:
            location(scene_dis, 'location/cafe.png')

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1

            # отрисовка текста из файла
            texts = get_text('scene_1_restaurant')
            for i in range(len(texts)):
                if click_count == len(texts) - 4:
                    find_puzzle_game('location/cafe.png')
                    click_count += 1
                if click_count == len(texts) - 2:
                    pygame.mixer.music.stop()
                    show_puzzle('assets/puzzle.jpg', 3)
                    click_count += 1
                if i == click_count:
                    show_text(*texts[i])

            # НАЧАЛО МИНИ-ИГРЫ(поиск пазлов)
            # НАЧАЛО МИНИ-ИГРЫ(собрать пазлы)

            if click_count >= len(texts):
                running = False

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_2_end

    def scene_2_end():
        # Сцена 1 (фон: вагон ресторан)
        click_count = 0
        running = True
        pygame.mixer.music.play(100)
        pygame.mixer.music.set_volume(0.2)
        while running:
            location(scene_dis, 'assets/end_happy.png')

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1

            # отрисовка текста из файла
            texts = get_text('scene_2_end')
            for i in range(len(texts)):
                if i == click_count:
                    show_text(*texts[i])

            if click_count >= len(texts):
                show_branch(end_branch)
                running = False

            set_cursor(scene_dis)
            pygame.display.update()

    global scene_end_game

    def scene_end_game():
        # Конец
        click_count = 0
        running = True
        while running:
            location(scene_dis, 'assets/back.jpg')
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                pygame_btn_quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_count += 1

                    # if btn_1.checkForInput(mouse_pos):
                    #     game()
                    #     running = False
                    #
                    # if btn_2.checkForInput(mouse_pos):
                    #     quit()

            # for i in range(2):
            #     num, text = get_text('scene_end_game', True)[i]
            #     globals()['btn_' + str(i + 1)] = set_button(num, text[:-1])

            # отрисовка текста из файла
            texts = get_text('scene_end_game')
            for i in range(len(texts)):
                if i == click_count:
                    show_text(*texts[i])

            if click_count >= len(texts):
                quit()
            #     update_button(btn_1, btn_2, mouse_pos)

            set_cursor(scene_dis)
            pygame.display.update()

    def show_branch(branch):
        # функция показа веток
        for function, arguments in branch.items():
            # преобразование строки (имени функции) в вызов функции
            globals()[function](*arguments)

    show_branch(globals()[branches[0]])

    quit()
