import pygame

class Cell:
    def __init__(self, screen):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__screen = screen

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1 + 50
        self.__x2 = x2 + 50
        self.__y1 = y1 + 50
        self.__y2 = y2 + 50

        if self.has_left_wall:
            pygame.draw.line(self.__screen, (255, 255, 255), (self.__x1, self.__y1), (self.__x1, self.__y2))
        else:
            pygame.draw.line(self.__screen, (0, 0, 0), (self.__x1, self.__y1), (self.__x1, self.__y2))

        if self.has_top_wall:
            pygame.draw.line(self.__screen, (255, 255, 255), (self.__x1, self.__y1), (self.__x2, self.__y1))
        else:
            pygame.draw.line(self.__screen, (0, 0, 0), (self.__x1, self.__y1), (self.__x2, self.__y1))

        if self.has_right_wall:
            pygame.draw.line(self.__screen, (255, 255, 255), (self.__x2, self.__y1), (self.__x2, self.__y2))
        else:
            pygame.draw.line(self.__screen, (0, 0, 0), (self.__x1, self.__y1), (self.__x2, self.__y2))

        if self.has_bottom_wall:
            pygame.draw.line(self.__screen, (255, 255, 255), (self.__x1, self.__y2), (self.__x2, self.__y2))
        else:
            pygame.draw.line(self.__screen, (0, 0, 0), (self.__x1, self.__y2), (self.__x2, self.__y2))

    def draw_move(self, to_cell, undo: bool = False):
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1

        fill_color = (250, 25, 30)
        if undo:
            fill_color = (150, 150, 150)

        pygame.draw.line(self.__screen, fill_color, (x_center, y_center), (x_center2, y_center2))
