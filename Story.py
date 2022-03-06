from multiprocessing.connection import wait
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
    
    wait_time = 300;
    
    while (wait_time > 0):
        for ev in pygame.event.get():     
            if ev.type == pygame.KEYDOWN: 
                wait_time = 0
        wait_time -= 1
        sleep(0.01)