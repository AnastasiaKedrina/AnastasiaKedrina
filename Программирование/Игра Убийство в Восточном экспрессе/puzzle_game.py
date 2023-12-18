import pygame, random

pygame.init()
cursor = pygame.image.load('assets/cursor.png')
pygame.mouse.set_visible(False)
puzzle_sound = pygame.mixer.Sound('sounds/fon_puzzle.wav')


def puzzle_game(screen, width: int, height: int, size: int, margin: int, font, image: str, background: str,
                final_text: str):
    puzzle_done = False
    selected_img = None
    cells = []

    rows = size
    cols = size
    num_cells = rows * cols

    cell_width = width // rows
    cell_height = height // cols
    highlight_color = (255, 0, 0)

    cell = []
    rand_indexes = list(range(0, num_cells))

    for i in range(num_cells):
        x = (i % rows) * cell_width + margin
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': (255, 255, 255), 'order': i, 'pos': rand_pos})

    running = True
    puzzle_sound.play()
    while running:
        screen.blit(pygame.image.load(background), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if puzzle_done:
                    running = False
                else:
                    mouse_pos = pygame.mouse.get_pos()

                    for cell in cells:
                        rect = cell['rect']
                        order = cell['order']

                        if rect.collidepoint(mouse_pos):
                            if not selected_img:
                                selected_img = cell
                                cell['border'] = highlight_color
                            else:
                                current_img = cell
                                # if current_img['order'] != selected_img['order']:
                                    # меняем кусочки местами
                                temp = selected_img['pos']
                                cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                                cells[current_img['order']]['pos'] = temp

                                cells[selected_img['order']]['border'] = (255, 255, 255)
                                selected_img = None

                                # собран пазл или нет
                                puzzle_done = True
                                for cell in cells:
                                    if cell['order'] != cell['pos']:
                                        puzzle_done = False

        if not puzzle_done:
            for i, val in enumerate(cells):
                pos = cells[i]['pos']
                img_area = pygame.Rect(cells[pos]['rect'].x - margin, cells[pos]['rect'].y, cell_width, cell_height)
                screen.blit(image, cells[i]['rect'], img_area)
                pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)
        else:
            puzzle_sound.set_volume(0.0)
            screen.blit(pygame.image.load(background), (0, 0))
            screen.blit(image, (margin, 0))

            play_again_text = font.render(final_text, True, (255, 255, 255))
            screen.blit(play_again_text, play_again_text.get_rect(center=(width // 2 + margin, height // 2)))
        coord = pygame.mouse.get_pos()
        screen.blit(cursor, coord)
        pygame.display.update()
