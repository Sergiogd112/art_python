import pygame

import numpy as np
# set our screen's width and height
screenWidth, screenHeight = (8000, 4000)

pygame.init()

pygame.display.set_caption("10 PRINT in Pygame")
screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True

white = (255, 255, 255)
black = (0, 0, 0)

# size of square, in pixels
square = 20


def drawScreen():
    screen.fill(black)
    # Python version of 10 PRINT happens here
    for x in range(0, screenWidth, square):
        for y in range(0, screenHeight, square):
            if np.random.random(1) >= 0.5:
                pygame.draw.line(screen, white, (x, y),
                                 (x + square, y + square))
            else:
                pygame.draw.line(
                    screen, white, (x, y + square), (x + square, y))


while running:
    key = pygame.key.get_pressed()
    # only draw if user presses spacebar
    if key[pygame.K_SPACE]:
        drawScreen()
    # quit if user presses q
    if key[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # this updates the display
    pygame.display.flip()
