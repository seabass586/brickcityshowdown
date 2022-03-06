import pygame
import shooter


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 40
        self.current_image = pygame.transform.scale(pygame.image.load("assets/rat.png"), (200,200))
        self.rect = self.current_image.get_rect()
        self.rect.centerx = 190
        self.rect.bottom = 360
        self.speedx = 2
        self.moved = 0
        self.move_right = True
        self.rage = False
        self.image_up = pygame.transform.scale(self.current_image, (200, 200))
        self.image_down = pygame.transform.scale(self.current_image, (200, 190))

    def update(self):  # moving logic
        if (pygame.time.get_ticks() % 2000 > 1000):
            self.image_up = pygame.transform.scale(self.current_image, (200, 200))
            self.image = self.image_up
            self.rect.bottom = 350
        else:
            self.image_down = pygame.transform.scale(self.current_image, (200, 190))
            self.image = self.image_down
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
