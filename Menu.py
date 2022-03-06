import pygame
import shooter
import main

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
            pygame.draw.rect(screen, GREY ,[575,shooter.HEIGHT/3,140,40]) 
        else: 
            pygame.draw.rect(screen, DARK_GREY ,[575,shooter.HEIGHT/3,140,40]) 

        if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/2 <= mouse[1] <= shooter.HEIGHT/2+40: 
            pygame.draw.rect(screen, GREY,[575,shooter.HEIGHT/2,140,40]) 
        else: 
            pygame.draw.rect(screen,DARK_GREY,[575,shooter.HEIGHT/2,140,40]) 

        screen.blit(text1, (610, 400)) 
        screen.blit(text2, (610, 500)) 

        pygame.display.update() 

def deathscreen():
    text1 = smallfont.render('YOU WERE DEFEATED!', False, shooter.WHITE)
    text2 = smallfont.render('One more time!', False, shooter.WHITE)
    text3 = smallfont.render('I give up...', False, shooter.WHITE)

    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/3 <= mouse[1] <= shooter.HEIGHT/3+40: 
                    main.main()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/2 <= mouse[1] <= shooter.HEIGHT/2+40: 
                    pygame.quit() 

        mouse = pygame.mouse.get_pos() 

        screen.fill(shooter.BLACK)
      
        screen.blit(text1, (500, 100))
        screen.blit(text2, (500, shooter.HEIGHT/3))
        screen.blit(text3, (500, shooter.HEIGHT/2))

        pygame.display.update()

