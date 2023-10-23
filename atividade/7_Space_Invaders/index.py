import pygame
from pygame.locals import *
import random

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 600

rows = 5
cols = 5
alien_cooldown = 800
last_alien_shot = pygame.time.get_ticks()

RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((screen_width, screen_height), 0)
pygame.display.set_caption('Milky Way Defense')

backGround = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/img/bg.png")

def draw_backGround():
    screen.blit(backGround, (0, 0))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks()
        
    
    def update(self):
        speed = 5
        cooldown = 500
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width - 5:
            self.rect.x += speed
            
        time_now = pygame.time.get_ticks()    
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now
        #vidas
        
        
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
    
    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)


class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/alien" +
                                       str(random.randint(1, 4)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1
        
        
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 125:
            self.move_direction *= -1
            self.move_counter *= self.move_direction
    
    
class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/img/alien_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
    
    def update(self):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceship_group, False):
            self.kill()
            #reduzir a vida
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)
            

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for numero in range(1, 6):
            img = pygame.image.load(f"C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/img/exp{numero}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (160, 160))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        
        
    def update(self):
        explosion_speed = 3
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

def create_aliens():
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(200 + item * 100, 90 + row * 70)
            alien_group.add(alien)

spaceship = Spaceship((screen_width//2), screen_height - 40)
spaceship_group.add(spaceship)
create_aliens()

run = True
while run:
    
    clock.tick(fps)
    
    draw_backGround()
    
    time_now = pygame.time.get_ticks()
    if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
        attacking_alien = random.choice(alien_group.sprites())
        alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
        alien_bullet_group.add(alien_bullet)
        last_alien_shot = time_now
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    spaceship.update()
    bullet_group.update()
    alien_group.update()
    alien_bullet_group.update()
    explosion_group.update()
    
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)
    
    pygame.display.update()
            
pygame.quit()
