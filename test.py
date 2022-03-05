import pygame

from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        self.surf = pygame.Surface((25, 25))

        self.surf.fill(0, 200, 255)
        self.rect = self.surf.get_rect()

pygame.init()

screen = pygame.display.set_mode((800, 600))

square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False

    screen.blit(square1.surf, (40, 40))
    screen.blit(square2.surf, (40, 530))
    screen.blit(square3.surf, (730, 40))
    screen.blit(square4.surf, (730, 530))

    pygame.display.flip()