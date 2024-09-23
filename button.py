import pygame

class Button:
    def __init__(self, color: tuple[int, int, int], x: int, y: int, width: int, height: int, text: str, textColor: tuple[int, int, int], win):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__font = pygame.font.SysFont('couriernew', 35)
        self.__text = self.__font.render(text, True, (textColor))
        self.__surface = pygame.Surface((width, height))
        self.__win = win

    def draw(self):
        self.__surface.fill(self.__color)
        self.__surface.blit(self.__text, (10, 10))
        self.__win.blit(self.__surface, (self.__x, self.__y))
