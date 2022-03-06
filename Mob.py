import pygame
import shooter
import random


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        random_var = random.randrange(0,3)
        if random_var == 0:
            self.image = pygame.image.load("assets/bacteria1.png")
        elif random_var == 1:
            self.image = pygame.image.load("assets/bacteria2.png")
        else:
            self.image = pygame.image.load("assets/bacteria3.png")


        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(490, 790 - self.rect.width)
        self.rect.y = 390
        self.speedy = random.randrange(1, 4)
        self.speedx = random.randrange(-1, 2)
        
        self.end_freeze_time = -1
        self.freeze = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > 690 or self.rect.left < 490 or self.rect.right > 790:
            self.respawn()

    def respawn(self):
        self.rect.x = random.randrange(490, 790 - self.rect.width)
        self.rect.y = 390
        if (self.freeze):
            self.speedy = 0
        else:
            self.speedy = random.randrange(1, 4)
        
    def update_time(self, time):
        if (time - self.end_freeze_time > 0):
            self.freeze = False
            self.end_freeze_time = -1
            self.respawn()
        else:
            self.freeze = True
    
    def set_end_freeze_time(self, end_time):
        self.end_freeze_time = end_time 

    def isFreezing(self):
        return self.freeze