import pygame
import shooter
import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 3;
        self.image = pygame.Surface((50, 40))
        self.image.fill(shooter.GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = shooter.WIDTH / 2
        self.rect.bottom = shooter.HEIGHT - 10
        self.speedx = 0

    def update(self): # moveing logic
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4
        self.rect.x += self.speedx
        if self.rect.right > shooter.WIDTH:
            self.rect.right = shooter.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shooter(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        shooter.all_sprites.add(bullet)
        shooter.bullets.add(bullet)
    
    def isConcious(self):
        return (self.HP > 0)
    
    def Hit(self, mobs):
        if (self.isConcious()):
            self.HP -=1
        print(self.HP)
        return self.isConcious()