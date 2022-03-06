import pygame
import shooter
import Player



def sounds_player(player):
    if player.HP <= 1:
        pygame.mixer.music.load("assets/lowHP.mp3")
        pygame.mixer.music.play(-1)

    return None