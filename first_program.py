import pygame
import pygame.gfxdraw
from jutge import read_line as input

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

white = (255, 255, 255)

black = (0, 0, 0)

running = True

while running:

    screen.fill(black)

    # Our for loop, for the width of the screen
    for i in range(0, screenWidth):
        try:
            # draw the same x and y for the whole width
            pygame.gfxdraw.pixel(screen, i, i**2, white)
        except:
            pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
