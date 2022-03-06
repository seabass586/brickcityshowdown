import pygame
import Mob
import Player
import Boss
import Bullet
import random
import os
from sys import exit

WIDTH = 1280
HEIGHT = 720
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player.Player()
boss = Boss.Boss()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display = pygame.Surface((WIDTH, HEIGHT))


def UI_setup():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()


def run_game():
    UI_setup()

    # initialize pygame and create window
    pygame.display.set_caption("BrickBreaker")
    clock = pygame.time.Clock()

    bg = pygame.image.load("assets/bg.jpg")
    gb = pygame.image.load("assets/game_box.jpg")
    gb_small = pygame.transform.scale(gb, (300, 300))

    # add the player sprite to the master sprite group
    all_sprites.add(player)
    all_sprites.add(boss)

    # add 8 mobs to the master sprite group
    for i in range(8):
        m = Mob.Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Game loop
    running = True
    immune = False
    collision_time = 0

    while running:
        # keep loop running at right speed
        clock.tick(FPS)

        # process input(events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shooter()

        # update sprites and mobs
        all_sprites.update()
        mobs.update()

        for mob in mobs.sprites():
            if pygame.sprite.spritecollide(mob, bullets, False):
                for bullet in bullets.sprites():
                    if pygame.sprite.spritecollide(bullet, mobs, False):
                        bullet.kill()
                mob.respawn()



        # detects collision, changes player HP, and stores data in a tuple
        collision_data = collision_detection(collision_time, immune)
        immune = collision_data[1]
        collision_time = collision_data[0]

        # draw/render
        render_game(screen, gb_small)

        # present the text onto the screen
        present_text(screen)

        # after drawing everything, flip the display
        pygame.display.flip()

        if player.HP == 0:
            running = False

    game_over(screen)


def present_text(screen):
    HP = player.HP
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Health: ' + str(HP), False, WHITE)
    screen.blit(textsurface, (0, 0))


def render_game(screen, game_box):
    screen.fill(BLACK)
    screen.blit(game_box, (490, 390))
    all_sprites.draw(screen)


def collision_detection(collision_time, immune):
    # if the player is no longer immune to damage, turn off immunity
    if (pygame.time.get_ticks() - collision_time) > 2000:
        immune = False

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits and immune is False:
        player.Hit()
        collision_time = pygame.time.get_ticks()
        immune = True

    return collision_time, immune


def game_over(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        screen.fill(BLACK)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('YOU WERE DEFEATED!', False, WHITE)
        screen.blit(textsurface, (470, 360))

        pygame.display.flip()
