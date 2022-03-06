import pygame
import shooter


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 40
        self.image = pygame.transform.scale(pygame.image.load("assets/rat.png"), (200,200))
        self.rect = self.image.get_rect()
        self.rect.centerx = 190
        self.rect.bottom = 360
        self.speedx = 2
        self.moved = 0
        self.move_right = True
        self.rage = False

    def update(self):  # moving logic
        if (pygame.time.get_ticks() % 2000 > 1000):
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.rect.bottom = 350
        else:
            self.image = pygame.transform.scale(self.image, (200, 190))
            self.rect.bottom = 360
        
        

        if self.move_right:
            self.rect.x += self.speedx
            self.moved += self.speedx
            if self.rage == True:
                self.rect.x += self.speedx
                self.moved += self.speedx
        else:
            self.rect.x -= self.speedx
            self.moved -= self.speedx
            if self.rage == True:
                self.rect.x -= self.speedx
                self.moved -= self.speedx

        if self.moved >= 500:
            self.move_right = False
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.moved <= 0:
            self.move_right = True
            self.image = pygame.transform.flip(self.image, True, False)

        if self.rect.right > shooter.WIDTH - 200:
            self.rect.right = shooter.WIDTH - 200
        if self.rect.left < 200:
            self.rect.left = 200
