import pygame
import shooter

pygame.init()

GREY = 170,170,170
DARK_GREY = 100,100,100

res = (shooter.WIDTH, shooter.HEIGHT)
screen = pygame.display.set_mode(res) 
smallfont = pygame.font.SysFont('Comics Sans MS',35) 
text1 = smallfont.render("Start", True, shooter.WHITE)
text2 = smallfont.render('Quit' , True , shooter.WHITE) 
  
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

    screen.fill((shooter.BLACK)) 

    mouse = pygame.mouse.get_pos() 

    if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/3 <= mouse[1] <= shooter.HEIGHT/3+40: 
        pygame.draw.rect(screen, GREY ,[shooter.WIDTH/2,shooter.HEIGHT/3,140,40]) 
    else: 
        pygame.draw.rect(screen, DARK_GREY ,[shooter.WIDTH/2,shooter.HEIGHT/3,140,40]) 

    if shooter.WIDTH/2 <= mouse[0] <= shooter.WIDTH/2+140 and shooter.HEIGHT/2 <= mouse[1] <= shooter.HEIGHT/2+40: 
        pygame.draw.rect(screen, GREY,[shooter.WIDTH/2,shooter.HEIGHT/2,140,40]) 
    else: 
        pygame.draw.rect(screen,DARK_GREY,[shooter.WIDTH/2,shooter.HEIGHT/2,140,40]) 

    screen.blit(text1, (shooter.WIDTH/2,shooter.HEIGHT/3)) 
    screen.blit(text2, (shooter.WIDTH/2,shooter.HEIGHT/2)) 


    pygame.display.update() 