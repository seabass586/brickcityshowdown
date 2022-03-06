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
    
    isEscaped = False 
    while not isEscaped:
        pygame.init()
        pygame.display.set_caption("Story Of the Game")
        res = (shooter.WIDTH, shooter.HEIGHT)
        screen = pygame.display.set_mode(res) 
        bg = pygame.image.load("assets/controls.png")
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))
        # navigate through pages
        pygame.display.update()
        for ev in pygame.event.get():     
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    if (storyHelpScreen()):
                        isEscaped = not isEscaped
                elif ev.key == pygame.K_ESCAPE:
                    isEscaped = not isEscaped
                
                
def storyHelpScreen():
    isEscaped = False
    while not isEscaped:
        pygame.init()
        pygame.display.set_caption("Story Of the Game")
        res = (shooter.WIDTH, shooter.HEIGHT)
        screen = pygame.display.set_mode(res) 
        bg = pygame.image.load("assets/tutorialScreen2.png")
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))
        pygame.display.update()
        for ev in pygame.event.get():     
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    return False # return false will not break the control help loop.
                elif ev.key == pygame.K_ESCAPE:
                    return True # return true will break the control help loop as well