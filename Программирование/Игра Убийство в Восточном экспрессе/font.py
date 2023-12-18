import pygame

def dialogue_font(size):
    return pygame.font.Font("fonts/comic.ttf", size)

def title_font(size):
    return pygame.font.Font("fonts/impact.ttf", size)

def blit_text(surface, text, font, color, pos, padding=10):
    words = [word.split(' ') for word in text.splitlines()]  
    space = font.size(' ')[0] 
    max_width, max_height = surface.get_size()
    
    pos = [i+padding for i in pos]
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width-padding:
                x = pos[0] 
                y += word_height 
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0] 
        y += word_height
