import pygame
import shooter
import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.HP = 3;
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = shooter.WIDTH / 2
        self.rect.bottom = shooter.HEIGHT - 40
        self.speedx = 0
        self.speedy = 0

    def update(self): # moving logic
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4
            
        if keystate[pygame.K_UP]:
            self.speedy = -4
        if keystate[pygame.K_DOWN]:
            self.speedy = 4
            
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        if self.rect.bottom > shooter.HEIGHT-30:
            self.rect.bottom = shooter.HEIGHT-30 
        if self.rect.top < shooter.HEIGHT-330:
            self.rect.top = shooter.HEIGHT-330
        
        if self.rect.right > shooter.WIDTH - 490:
            self.rect.right = shooter.WIDTH - 490
        if self.rect.left < 490:
            self.rect.left = 490

    def shooter(self):
        bullet = Bullet.Bullet(self.rect.centerx, self.rect.top)
        shooter.all_sprites.add(bullet)
        shooter.bullets.add(bullet)
    
    def isConcious(self):
        if self.HP <= 0:
            death_sound = pygame.mixer.Sound("assets/DEATH.mp3")
            death_sound.set_volume(0.4)
            pygame.mixer.Sound.play(death_sound)
            pygame.mixer.music.stop()


        return self.HP > 0
    
    def Hit(self):
        hit_sound = pygame.mixer.Sound("assets/owwFast.wav")
        hit_sound2 = pygame.mixer.Sound("assets/pop.mp3")
        hit_sound.set_volume(0.2)
        hit_sound2.set_volume(0.6)
        pygame.mixer.Sound.play(hit_sound)
        pygame.mixer.Sound.play(hit_sound2)

        if self.isConcious():
            self.HP -=1                
            if self.HP == 1:
                pygame.mixer.music.load("assets/lowHP.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)