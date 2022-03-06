import pygame
import shooter
import random

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(shooter.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(490, 790 - self.rect.width)
        self.rect.y = 390
        self.speedy = random.randrange(1, 4)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > 690 or self.rect.left < 490 or self.rect.right > 790:
            self.rect.x = random.randrange(490, 790 - self.rect.width)
            self.rect.y = 390
            self.speedy = random.randrange(1, 4)