import pygame
import Mob
import Player
import Boss
from sys import exit
import Menu

WIDTH = 1280
HEIGHT = 720
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SHADED_RED = (127, 0, 0)
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
    pygame.display.set_caption("Brick City Showdown")
    clock = pygame.time.Clock()

    dorm_room = pygame.image.load("assets/dormFloor.png")
    bg = pygame.image.load("assets/bg.jpg")
    gb = pygame.image.load("assets/game_box.jpg")
    gb2 = pygame.image.load("assets/game_box - Copy.png")
    gb_small = pygame.transform.scale(gb, (300, 300))
    gb_small2 = pygame.transform.scale(gb2, (300, 300))
    gb_small3 = pygame.transform.scale(gb, (300, 300))

    # add the player sprite to the master sprite group
    all_sprites.add(player)
    all_sprites.add(boss)

    # add 8 mobs to the master sprite group
    for i in range(4):
        m = Mob.Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Game loop
    running = True
    player_immune = False
    player_collision_time = 0

    rat_song = pygame.mixer.Sound("assets/rat song.mp3")
    rat_song.set_volume(0.2)
    pygame.mixer.Sound.play(rat_song, -1)

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

        # process collision with mobs and bullets
        for mob in mobs.sprites():
            if pygame.sprite.spritecollide(mob, bullets, False):
                for bullet in bullets.sprites():
                    if pygame.sprite.spritecollide(bullet, mobs, False):
                        hit_germ = pygame.mixer.Sound("assets/hit germ.wav")
                        hit_germ.set_volume(0.1)
                        pygame.mixer.Sound.play(hit_germ)
                        bullet.kill()
                if (not mob.isFreezing()):
                    mob.set_end_freeze_time(pygame.time.get_ticks() + 1000)
                    mob.update_time(pygame.time.get_ticks())
                    mob.respawn()
            if (mob.isFreezing()):
                mob.update_time(pygame.time.get_ticks())

        # process collusion with te bullets and the boss
        boss_collision_detection(rat_song)

        # detects collision, changes player HP, and stores data in a tuple
        player_collision_data = player_collision_detection(player_collision_time, player_immune)
        player_immune = player_collision_data[1]
        player_collision_time = player_collision_data[0]

        # draw/render
        render_game(screen, gb_small, gb_small2, gb_small3, player.HP, dorm_room)

        # present the text onto the screen
        present_text(screen)

        # after drawing everything, flip the display
        pygame.display.flip()

        if player.HP == 0:
            running = False
        if boss.HP <= 0:
            # victory(screen)
            Menu.winningscreen()

    Menu.deathscreen()


def present_text(screen):
    player_HP = player.HP
    boss_HP = boss.HP
    myfont = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 19)
    player_HP_text = myfont.render('Your Health: ' + str(player_HP), False, WHITE)
    boss_HP_text = myfont.render("Boss Health: " + str(boss_HP), False, WHITE)

    if boss.HP > 25:
        boss_msg1 = myfont.render("You really think you ", False, WHITE)
        boss_msg2 = myfont.render("can beat me!? Not a ", False, WHITE)
        boss_msg3 = myfont.render("chance!", False, WHITE)
        screen.blit(boss_msg1, (840, 415))
        screen.blit(boss_msg2, (840, 440))
        screen.blit(boss_msg3, (840, 465))
    elif boss.HP > 10:
        boss_msg1 = myfont.render("Now you've gone and", False, WHITE)
        boss_msg2 = myfont.render("made me angry! Take", False, WHITE)
        boss_msg3 = myfont.render("this!", False, WHITE)
        boss_msg4 = myfont.render("TIP: Don't spam!", False, WHITE)
        boss_msg5 = myfont.render("Wait for bacteria", False, WHITE)
        boss_msg6 = myfont.render("to disappear!", False, WHITE)
        screen.blit(boss_msg1, (840, 415))
        screen.blit(boss_msg2, (840, 440))
        screen.blit(boss_msg3, (840, 465))
        screen.blit(boss_msg4, (840, 500+40))
        screen.blit(boss_msg5, (840, 525+40))
        screen.blit(boss_msg6, (840, 550+40))
    elif boss.HP <= 10:
        boss_msg1 = myfont.render("No! This isn't", False, WHITE)
        boss_msg2 = myfont.render("possible! Germs,", False, WHITE)
        boss_msg3 = myfont.render("attack!", False, WHITE)
        screen.blit(boss_msg1, (840, 415))
        screen.blit(boss_msg2, (840, 440))
        screen.blit(boss_msg3, (840, 465))

    screen.blit(player_HP_text, (89, 415))
    screen.blit(boss_HP_text, (465, 30))


def render_game(screen, game_box, game_box2, game_box3, player_HP, dorm_room):
    if player_HP == 3:
        player_img = pygame.image.load("assets/Rickie.png")
    elif player_HP == 2:
        player_img = pygame.image.load("assets/Rickie2.png")
    else:
        player_img = pygame.image.load("assets/Rickie3.png")

    screen.fill(BLACK)
    screen.blit(dorm_room, (0, 0))
    screen.blit(pygame.image.load("assets/wallpaper.jpg").convert_alpha(), (0, 640))
    screen.blit(game_box2, (490, 390))
    screen.blit(pygame.transform.scale(game_box, (290, 290)), (80, 400))
    screen.blit(pygame.transform.scale(game_box3, (400, 290)), (830, 400))
    if (pygame.time.get_ticks() % 2000 > 1000):
        screen.blit(player_img, (110, 430))
    else:
        screen.blit(player_img, (110, 440))

    all_sprites.draw(screen)


def player_collision_detection(collision_time, immune):
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


def boss_collision_detection(song):
    if pygame.sprite.spritecollide(boss, bullets, False):
        for bullet in bullets.sprites():
            if pygame.sprite.collide_rect(bullet, boss):
                boss.HP -= 1

                if boss.HP == 25:
                    boss.rage = True
                    song.stop()
                    mad_song = pygame.mixer.Sound("assets/ANGRY RAT.wav")
                    mad_song.set_volume(0.2)
                    pygame.mixer.Sound.play(mad_song, -1)
                    boss.rect.bottom = 320

                if boss.HP == 10:
                    m = Mob.Mob()
                    all_sprites.add(m)
                    mobs.add(m)
                hit_sound = pygame.mixer.Sound("assets/bossHit.mp3")
                hit_sound.set_volume(0.2)
                pygame.mixer.Sound.play(hit_sound)
                bullet.kill()
