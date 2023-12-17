import pygame
from pygame.locals import (QUIT)

class Player():
    def __init__(self, color):
        self.__color=color

    def color(self):
        return self.__color


    color=property(color)

def print_m(matrix):
    for i in matrix:
        print(i)

def place_to_move(matrix, column):
    flag=False
    for i in range(len(matrix)-1, -1, -1):
        if matrix[i][column]==0:
            flag=True
            return i
    if not flag:
        return -1

# def player_move(player):
#     flag=False
#     while not flag:
#         print('Ход игрока номер ',player)
#         print('Введите столбец')
#         row=int(input())
#         for i in range(len(matrix)-1,-1,-1):
#             if matrix[i][row-1]==0:
#                 matrix[i][row-1]=player
#                 flag=True
#                 break
#         if not flag:
#             print('В ряду нет места')
#         else:
#             print_m(matrix)

def find_row(matrix):
    four_in_row = False
    row_pos=[]
    for row in range(len(matrix)):
        for i in range(3):
            # горизонтально
            if matrix[row][i] == matrix[row][i + 1] == matrix[row][i + 2] == matrix[row][i + 3] != 0:
                four_in_row = True
                row_pos=[(row,i),(row,i+1),(row,i+2),(row,i+3)]
                break

            # вертикально
            if matrix[i][row] == matrix[i + 1][row] == matrix[i + 2][row] == matrix[i + 3][row] != 0:
                four_in_row = True
                row_pos=[(row,i),(i+1, row),(i+2, row),(i+3, row)]
                break

            # диагональ
            if row < 3:
                # вниз
                if matrix[row][i] == matrix[row + 1][i + 1] == matrix[row + 2][i + 2] == matrix[row + 3][i + 3] != 0:
                    four_in_row = True
                    row_pos=[(row,i),(row+1,i+1),(row+2,i+2),(row+3,i+3)]
                    break
                # вверх
                i+=3
                if matrix[row][i] == matrix[row + 1][i - 1] == matrix[row + 2][i - 2] == matrix[row + 3][i - 3] != 0:
                    four_in_row = True
                    row_pos=[(row,i),(row+1,i-1),(row+2,i-2),(row+3,i-3)]
                    break

    return [four_in_row, row_pos]

def drawn_game(matrix):
    for i in matrix:
        for j in i:
            if j==0:
                return False
    return True


matrix=[[0]*6 for _ in range(6)]
player_yellow=Player('жёлтый')
player_purple=Player('фиолетовый')
# run=True
# while run:
#     player_move(1)
#     if find_row(matrix)[0]:
#         print('Выиграл игрок номер 1')
#         print(find_row(matrix)[1])
#         break
#     player_move(2)
#     if find_row(matrix)[0]:
#         print('Выиграл игрок номер 2')
#         print(find_row(matrix)[1])
#         break

screen_width = 600
screen_height = 700
sc = pygame.display.set_mode((screen_width, screen_height))
pygame.init()

positions=[]
for i in range(6):
    a=[]
    for j in range(6):
        # x,y=screen_width//6,screen_height//6
        x, y=100, 100
        #width, height=50,42
        width, height=65,57

        a.append([j*width+x, i*height+y])
    positions.append(a)

# def bilt_text(text, x, y):
#     for shadow in [['_black', 0], ['_white', 2]]:
#         t='text_'+text+shadow[0]
#         sc.blit(locals()[t], locals()[t].get_rect(center=(x, y+shadow[1])))

current_player=player_yellow.color
winner=current_player
player_won=False

running = True
while running:
    # Закрытие окна
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # Фон
    background_image = pygame.image.load("images/background.jpg")
    sc.blit(background_image, [0, 0])


    empty_image = pygame.image.load("images/empty_cat.png").convert_alpha()
    empty_hover_image = pygame.image.load("images/empty_hover_cat.png").convert_alpha()
    yellow_image = pygame.image.load("images/yellow_cat.png").convert_alpha()
    purple_image = pygame.image.load("images/purple_cat.png").convert_alpha()
    yellow_alpha_image = pygame.image.load("images/yellow_alpha_cat.png").convert_alpha()
    purple_alpha_image = pygame.image.load("images/purple_alpha_cat.png").convert_alpha()

    size=[34, 54, 84] #размеры текста
    for s in size:
        locals()['font_'+str(size.index(s)+1)] = pygame.font.Font(None, s)


    text=[['yellow', 'Ход желтого котика', 'font_1'],
          ['purple','Ход фиолетового котика', 'font_1'],
          ['title','Четыре в ряд', 'font_3'],
          ['player_won',f'Выиграл {winner} котик', 'font_2'],
          ['drawn','Ничья', 'font_2']]
    for t in text:
        for color in ['white','black']:
            locals()['text_'+t[0]+'_'+color]= locals()[t[2]].render(t[1], True, color)

    black, white = (0, 0, 0), (255, 255, 255)
    # text_yellow_white = font_1.render('Ход желтого котика', True, white)
    # text_yellow_black = font_1.render('Ход желтого котика', True, black)
    # text_purple_white = font_1.render('Ход фиолетового котика', True, white)
    # text_purple_black = font_1.render('Ход фиолетового котика', True, black)
    # text_title_white = font_3.render('Четыре в ряд', True, white)
    # text_title_black = font_3.render('Четыре в ряд', True, black)
    # text_player_won_white = font_2.render(f'Выиграл {winner} котик', True, white)
    # text_player_won_black = font_2.render(f'Выиграл {winner} котик', True, black)
    # text_drawn_white = font_3.render('Ничья', True, white)
    # text_drawn_black = font_3.render('Ничья', True, black)

    text_pos_x=screen_width/2
    text_pos_y=600
    shadow=2

    # bilt_text('title', text_pos_x, 50)
    sc.blit(text_title_black, text_title_black.get_rect(center=(text_pos_x, 50+shadow)))
    sc.blit(text_title_white, text_title_white.get_rect(center=(text_pos_x, 50)))

    if not player_won and not drawn_game(matrix):
        if current_player==player_yellow.color:
            sc.blit(text_yellow_black, text_yellow_black.get_rect(center=(text_pos_x, text_pos_y+shadow)))
            sc.blit(text_yellow_white, text_yellow_white.get_rect(center=(text_pos_x, text_pos_y)))
            yellow_big_image=pygame.transform.scale(yellow_image, (90, 110))
            sc.blit(yellow_big_image, [70, text_pos_y-60])
            sc.blit(yellow_big_image, [425,text_pos_y-60])
        elif current_player==player_purple.color:
            sc.blit(text_purple_white, text_purple_white.get_rect(center=(text_pos_x, text_pos_y+shadow)))
            sc.blit(text_purple_black, text_purple_black.get_rect(center=(text_pos_x, text_pos_y)))
            purple_big_image=pygame.transform.scale(purple_image, (90, 110))
            sc.blit(purple_big_image, [50, text_pos_y-60])
            sc.blit(purple_big_image, [450, text_pos_y-60])

    # наведение мыши на столбец
    cursor = pygame.mouse.get_pos()
    for i in positions:
        for pos in i:
            sc.blit(empty_image, pos)

            if cursor[0] > pos[0] and cursor[0] < pos[0]+width and not player_won and not drawn_game(matrix):
                if cursor[1] > positions[0][1][1] and cursor[1]<positions[5][0][1]+height*4/3:
                    sc.blit(empty_hover_image, pos)
                    try:
                        column=positions[0].index(pos)
                    except: pass

                    try:
                        if current_player==player_yellow.color:
                            sc.blit(yellow_alpha_image, positions[place_to_move(matrix, column)][column])
                        elif current_player==player_purple.color:
                            sc.blit(purple_alpha_image, positions[place_to_move(matrix, column)][column])
                    except: pass

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if place_to_move(matrix,column)!=-1:
                                if current_player==player_yellow.color:
                                    matrix[place_to_move(matrix, column)][column]=1
                                    current_player=player_purple.color
                                elif current_player==player_purple.color:
                                    matrix[place_to_move(matrix, column)][column]=2
                                    current_player =player_yellow.color
                                if find_row(matrix)[0] or drawn_game(matrix):
                                    player_won=True

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                sc.blit(yellow_image, positions[i][j])
            if matrix[i][j]==2:
                sc.blit(purple_image, positions[i][j])

    if drawn_game(matrix):
        sc.blit(text_drawn_black, text_drawn_black.get_rect(center=(text_pos_x, text_pos_y+shadow)))
        sc.blit(text_drawn_white, text_drawn_white.get_rect(center=(text_pos_x, text_pos_y)))

        yellow_big_image=pygame.transform.scale(yellow_image, (90, 110))
        purple_big_image=pygame.transform.scale(purple_image, (90, 110))
        sc.blit(yellow_big_image, [100, text_pos_y-60])
        sc.blit(purple_big_image, [405,text_pos_y-60])

    elif player_won:
        if current_player==player_yellow.color:
            winner=player_purple.color
        elif current_player==player_purple.color:
            winner =player_yellow.color

        sc.blit(text_player_won_black, text_player_won_black.get_rect(center=(text_pos_x, text_pos_y+shadow)))
        sc.blit(text_player_won_white, text_player_won_white.get_rect(center=(text_pos_x, text_pos_y)))

        for pos in find_row(matrix)[1]:
            sc.blit(empty_image, positions[pos[0]][pos[1]])

    pygame.display.flip()
pygame.quit()

