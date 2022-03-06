from textwrap import fill
import pygame
import shooter
import Story
from sys import exit

pygame.init()
pygame.display.set_caption("Start Game")

GREY = (170,170,170)
DARK_GREY = (100,100,100)
mouse = 0

res = (shooter.WIDTH, shooter.HEIGHT)
screen = pygame.display.set_mode(res) 
bigfont = pygame.font.SysFont('Comics Sans MS',50) 
smallfont = pygame.font.SysFont('Comics Sans MS',35) 
text1 = smallfont.render("Start", True, shooter.WHITE)
text2 = smallfont.render("Help", True, shooter.WHITE)
text3 = smallfont.render('Quit' , True , shooter.WHITE) 
bg = pygame.image.load("assets/mainScreen.png")
dead = pygame.image.load("assets/Loss_screen.png")
rickie = pygame.image.load("assets/Rickie.png")

def startscreen():
    opening = pygame.mixer.Sound("assets/OVERTURE2.mp3")
    opening.set_volume(0.3)
    pygame.mixer.Sound.play(opening)
    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT:
                pygame.mixer.Sound.stop(opening)
                pygame.quit()
                exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 450 <= mouse[1] <= 490:
                    Story.storyScreen()
                    pygame.mixer.Sound.stop(opening)
                    shooter.run_game()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 550 <= mouse[1] <= 590:
                    Story.controlHelpScreen() 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 610 <= mouse[0] <= 610+140 and 650 <= mouse[1] <= 690:
                    pygame.mixer.Sound.stop(opening)
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(bg, (1280, 720))
        screen.blit(new, (0, 0))

        if 610 <= mouse[0] <= 610+140 and 450 <= mouse[1] <= 450+40: 
            pygame.draw.rect(screen, GREY,[575,450,140,40]) 
        else: 
            pygame.draw.rect(screen, DARK_GREY, [575,450,140,40]) 


        if 610 <= mouse[0] <= 610+140 and 550 <= mouse[1] <= 550+40: 
            pygame.draw.rect(screen, GREY,[575,550,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[575,550,140,40]) 


        if 610 <= mouse[0] <= 610+140 and 650 <= mouse[1] <= 650+40: 
            pygame.draw.rect(screen, GREY,[575,650,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[575,650,140,40]) 

        screen.blit(text1, (610, 455)) 
        screen.blit(text2, (610, 555))
        screen.blit(text3, (610, 655)) 

        pygame.display.update() 

def deathscreen():
    pygame.mixer.music.stop()
    text2 = smallfont.render('Exit Game', False, shooter.WHITE)

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()
                exit()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 560 <= mouse[0] <= 560+140 and 655 <= mouse[1] <= 655+40: 
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos() 
        new = pygame.transform.scale(dead, (1280, 720))
        screen.blit(new, (0, 0))

        if 560 <= mouse[0] <= 560+140 and 655 <= mouse[1] <= 655+40: 
            pygame.draw.rect(screen, GREY,[550,650,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[550,650,140,40]) 

        screen.blit(text2, (560, 655))

        pygame.display.update()

def winningscreen():
    pygame.mixer.music.stop()
    text1 = bigfont.render('RICKIE HAS REMAINED THE MASCOT!', False, shooter.WHITE)
    text2 = smallfont.render('Exit Game', False, shooter.WHITE)

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()
                exit()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 560 <= mouse[0] <= 560+140 and 555 <= mouse[1] <= 555+40: 
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos() 

        screen.fill(shooter.BLACK)
        screen.blit(rickie,(500, 255))

        if 560 <= mouse[0] <= 560+140 and 555 <= mouse[1] <= 555+40: 
            pygame.draw.rect(screen, GREY,[550,550,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[550,550,140,40]) 

        screen.blit(text1, (325, 150))
        screen.blit(text2, (560, 555))

        pygame.display.update()

def helpscreen():
    control = pygame.image.load("assets/controls.png")
    screen.blit(control, (0, 0))
    text1 = bigfont.render('Return to main menu', False, shooter.WHITE)

    while True:  
            for ev in pygame.event.get():     
                if ev.type == pygame.QUIT: 
                    pygame.quit()
                    exit()
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    if 560 <= mouse[0] <= 560+140 and 555 <= mouse[1] <= 555+40: 
                        pygame.quit()
                        exit()

            mouse = pygame.mouse.get_pos() 

            screen.fill(shooter.BLACK)

            if 560 <= mouse[0] <= 560+140 and 555 <= mouse[1] <= 555+40: 
                pygame.draw.rect(screen, GREY,[550,550,140,40]) 
            else: 
                pygame.draw.rect(screen,DARK_GREY,[550,550,140,40]) 

            screen.blit(text1, (470, 150))
            screen.blit(text2, (560, 555))

            pygame.display.update()
