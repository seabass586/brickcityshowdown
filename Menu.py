from asyncio.windows_events import INFINITE
from tkinter import CENTER
import pygame
import shooter

pygame.init()
pygame.display.set_caption("Start Game")

GREY = (170,170,170)
DARK_GREY = (100,100,100)

res = (shooter.WIDTH, shooter.HEIGHT)
screen = pygame.display.set_mode(res) 
smallfont = pygame.font.SysFont('Comics Sans MS',35) 
text1 = smallfont.render("Start", True, shooter.WHITE)
text2 = smallfont.render('Quit' , True , shooter.WHITE) 
bg = pygame.image.load("assets/startscreen.png")

def startscreen():  
    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/3 <= mouse[1] <= shooter.HEIGHT/3+40: 
                    shooter.run_game()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/2 <= mouse[1] <= shooter.HEIGHT/2+40: 
                        pygame.quit() 

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))

        if shooter.WIDTH/2 <= mouse[0] <= (shooter.WIDTH/2+140) and shooter.HEIGHT/3 <= mouse[1] <= shooter.HEIGHT/3+40: 
            pygame.draw.rect(screen, GREY ,[shooter.WIDTH/2,shooter.HEIGHT/3,140,40]) 
        else: 
            pygame.draw.rect(screen, DARK_GREY ,[shooter.WIDTH/2,shooter.HEIGHT/3,140,40]) 

        if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/2 <= mouse[1] <= shooter.HEIGHT/2+40: 
            pygame.draw.rect(screen, GREY,[shooter.WIDTH/2,shooter.HEIGHT/2,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[shooter.WIDTH/2,shooter.HEIGHT/2,140,40]) 

        screen.blit(text1, (600, 300)) 
        screen.blit(text2, (600, 400)) 

        pygame.display.update() 

