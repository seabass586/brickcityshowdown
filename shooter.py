import pygame
import Mob
import Player 
import Bullet
import random
import os

# from tinker import *

WIDTH = 500
HEIGHT = 768
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

def UI_setup():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

def main():
    UI_setup()

    # initialize pygame and create window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BrickBreaker")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player.Player()
    all_sprites.add(player)
    for i in range(8):
        m = Mob.Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Game loop
    running = True

    while running:
        # keep loop running at right speed
        clock.tick(FPS)

        # process input(events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # update
        all_sprites.update()
        mobs.update()

        # check to see if a mob hit the player
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            running = player.Hit()

        # draw/render
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # text
        score = 0;
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Score: ' + str(score), False, WHITE)
        screen.blit(textsurface, (0, 0))

        # after drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()