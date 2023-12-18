import pygame

pygame.init()

class Heroes():
    def __init__(self, first_name, last_name, image_name, x):
        self.x = x #чтоб двигать по оси x в зависимости от сцены
        self.original_image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (300, 550)) #изменение масштаба картинки
        self.rect = self.image.get_rect(center = (x, 400))
        self.__first_name = first_name
        self.__last_name = last_name
        self.__full_name = f'{first_name} {last_name}'

    def draw(self, scene):
        scene.blit(self.image, self.rect)

    def first_name(self):
        return self.__first_name

    def last_name(self):
        return self.__last_name
        
    def full_name(self):
        return self.__full_name

    first_name = property(first_name)
    last_name = property(last_name)
    full_name = property(full_name)
