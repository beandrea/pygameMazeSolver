from maze import Maze
from button import Button
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

button = Button((40, 40, 250), 600, 600, 175, 50, "Next ->", (255, 255, 255), screen)
maze = Maze(0, 0, 15, 15, 30, 30, screen)

running = True
screen.fill((0, 0, 0))

while running:
    button.draw()

    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pos[0] > 600 and pos[0] < 775 and pos[1] > 600 and pos[1] < 650:
            if event.type == pygame.MOUSEBUTTONUP:
                if maze.state == maze.stateList[2]:
                    maze.solve()

                if maze.state == maze.stateList[1]:
                    # screen.fill((0, 0, 0))
                    maze.break_entrance_and_exit()

                    maze.break_walls_r(0, 0)

                    maze.reset_cells_visited()

                if maze.state == maze.stateList[0]:
                    maze.draw()

            pygame.display.flip()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
