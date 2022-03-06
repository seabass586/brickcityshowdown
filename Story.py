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
    
    # skip story page
    while (wait_time > 0):
        for ev in pygame.event.get():     
            if ev.type == pygame.KEYDOWN: 
                wait_time = 0
        wait_time -= 1
        sleep(0.01)
    
def controlHelpScreen():
    while True:
        pygame.init()
        pygame.display.set_caption("Story Of the Game")
        res = (shooter.WIDTH, shooter.HEIGHT)
        screen = pygame.display.set_mode(res) 
        bg = pygame.image.load("assets/controls.png")
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))
        pygame.display.update()
    
        # navigate through pages
        for ev in pygame.event.get():     
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    if (storyHelpScreen()):
                        break
                elif ev.key == pygame.K_ESCAPE:
                    break
                
                
def storyHelpScreen():
    while True:
        pygame.init()
        pygame.display.set_caption("Story Of the Game")
        res = (shooter.WIDTH, shooter.HEIGHT)
        screen = pygame.display.set_mode(res) 
        bg = pygame.image.load("assets/controls.png")
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))
        pygame.display.update()
    
        # next page
        for ev in pygame.event.get():     
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    return False # return false will not break the control help loop.
                elif ev.key == pygame.K_ESCAPE:
                    return True # return true will break the control help loop as well