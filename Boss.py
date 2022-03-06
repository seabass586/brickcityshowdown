import pygame
import shooter
import Bullet


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 30
        self.image = pygame.image.load("assets/Rickie.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 190
        self.rect.bottom = 350
        self.speedx = 2
        self.moved = 0
        self.move_right = True

    def update(self):  # moving logic

        if self.move_right:
            self.rect.x += self.speedx
            self.moved += self.speedx
        else:
            self.rect.x -= self.speedx
            self.moved -= self.speedx

        if self.moved == 500:
            self.move_right = False
        elif self.moved == 0:
            self.move_right = True

        if self.rect.right > shooter.WIDTH - 200:
            self.rect.right = shooter.WIDTH - 200
        if self.rect.left < 200:
            self.rect.left = 200
