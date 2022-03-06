import pygame
import shooter
import main

pygame.init()
pygame.display.set_caption("Start Game")

GREY = (170,170,170)
DARK_GREY = (100,100,100)

res = (shooter.WIDTH, shooter.HEIGHT)
screen = pygame.display.set_mode(res) 
bigfont = pygame.font.SysFont('Comics Sans MS',50) 
smallfont = pygame.font.SysFont('Comics Sans MS',35) 
text1 = smallfont.render("Start", True, shooter.WHITE)
text2 = smallfont.render('Quit' , True , shooter.WHITE) 
bg = pygame.image.load("assets/mainScreen.png")

def startscreen():  
    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 610 <= mouse[0] <= 610+140 and 450 <= mouse[1] <= 490: 
                    shooter.run_game()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 610 <= mouse[0] <= 610+140 and 550 <= mouse[1] <= 590: 
                    pygame.quit() 

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

        screen.blit(text1, (610, 455)) 
        screen.blit(text2, (610, 555)) 

        pygame.display.update() 

def deathscreen():
    text1 = bigfont.render('YOU WERE DEFEATED!', False, shooter.WHITE)
    text2 = smallfont.render('One more time!', False, shooter.WHITE)
    text3 = smallfont.render('I give up...', False, shooter.WHITE)

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 480+140 and 455 <= mouse[1] <= 455+40: 
                    main.main()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if 480 <= mouse[0] <= 480+140 and 555 <= mouse[1] <= 555+40: 
                    pygame.quit() 

        mouse = pygame.mouse.get_pos() 

        screen.fill(shooter.BLACK)

        screen.blit(text1, (460, 150))
        screen.blit(text2, (480, 455))
        screen.blit(text3, (480, 555))

        pygame.display.update()

