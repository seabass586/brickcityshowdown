import pygame
from sys import exit
import pygame.locals

pygame.init()

# create the base screen
screen = pygame.display.set_mode((800, 600))

# basic game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

