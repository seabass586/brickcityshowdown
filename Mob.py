import pygame
import shooter
import random

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(shooter.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(shooter.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > shooter.HEIGHT + 10 or self.rect.left < -25 or self.rect.right > shooter.WIDTH + 20:
            self.rect.x = random.randrange(shooter.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)