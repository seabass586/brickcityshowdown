import pygame
import shooter
from time import sleep

def storyScreen():   
    pygame.init()
    pygame.display.set_caption("Story Of the Game")
    res = (shooter.WIDTH, shooter.HEIGHT)
    screen = pygame.display.set_mode(res) 
    bg = pygame.image.load("assets/Story.png")
    new = pygame.transform.scale(bg, (1280, 720))
    screen.blit(new, (0, 0))
    pygame.display.update()
    sleep(4)

