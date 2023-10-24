import pygame
from pygame import mixer
from pygame.locals import *
import random

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 600

explosion_fx = pygame.mixer.Sound("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/audio/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/audio/explosion2.wav")
explosion2_fx.set_volume(0.25)

laser_fx = pygame.mixer.Sound("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/audio/laser.wav")
laser_fx.set_volume(0.25)

rows = 5
cols = 5
alien_cooldown = 800
last_alien_shot = pygame.time.get_ticks()
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0
score = rows * cols
quantity_alien = rows * cols

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height), 0)
pygame.display.set_caption('Milky Way Defense')

fonte1 = pygame.font.Font("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/fonte/Pixeled.ttf", 20)
fonte2 = pygame.font.Font("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/fonte/Pixeled.ttf", 15)
fonte3 = pygame.font.Font("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/fonte/Pixeled.ttf", 30)
 
backGround = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/bg.png")
terra = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/terra.png")
lua = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/lua.png")

def draw_backGround():
    screen.blit(backGround, (0, 0))
    screen.blit(terra, (100, 350))
    screen.blit(lua, (500, 100))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks()
        self.health_start = health
        self.health_remaining = health
        
    
    def update(self):
        speed = 5
        cooldown = 500
        game_over = 0
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width - 5:
            self.rect.x += speed
        
        time_now = pygame.time.get_ticks()    
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            laser_fx.play()
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now
        
        self.mask = pygame.mask.from_surface(self.image)
            
        pygame.draw.rect(screen, RED, (self.rect.x, (self.rect.bottom + 2), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, GREEN, (self.rect.x, (self.rect.bottom + 2), 
                                             int(self.rect.width * ((self.health_remaining - 1)/(self.health_start-1))), 10))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            game_over = -1
            return game_over
        return game_over
        
        
        
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
    
    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            explosion_fx.play()
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
        self.image = pygame.image.load("C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/alien_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
    
    def update(self):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            explosion2_fx.play()
            spaceship.health_remaining -= 1
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)
            

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for numero in range(1, 6):
            img = pygame.image.load(f"C://Users/Softex/Documents/GitHub/Python/atividade/7_Space_invaders/assests/image/exp{numero}.png")
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

spaceship = Spaceship((screen_width//2), screen_height - 40, 3)
spaceship_group.add(spaceship)
create_aliens()

run = True
while run:
    
    clock.tick(fps)
    
    draw_backGround()
    if countdown == 0:
        draw_text(f'NAVES INIMIGAS RESTANTES: {score}', fonte1, WHITE, 10, 0)
        draw_text('FASE 1', fonte1, WHITE, (screen_width//2 + 150), 0)
        if len(alien_group) < quantity_alien:
            score -= (quantity_alien - len(alien_group))
            quantity_alien = len(alien_group)
        
        time_now = pygame.time.get_ticks()
        if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
            attacking_alien = random.choice(alien_group.sprites())
            alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            alien_bullet_group.add(alien_bullet)
            last_alien_shot = time_now
    
        if len(alien_group) <= 0:
            game_over = 1 
               
        if game_over == 0:
            game_over = spaceship.update()
            bullet_group.update()
            alien_group.update()
            alien_bullet_group.update()
        else:
            if game_over == -1:
                draw_text('Game Over!', fonte3, WHITE, (screen_width//2 - 135), (screen_height//2 + 80))
            elif game_over == 1:
                draw_text('You Win!', fonte3, WHITE, (screen_width//2 - 100), (screen_height//2 + 80))
                
        
    if countdown > 0:
        draw_text('PREPARE-SE COMANDANTE!', fonte1, WHITE, (screen_width//2 - 205), (screen_height//2 + 100))
        draw_text(f'DECOLAGEM EM {countdown}', fonte2, WHITE, (screen_width//2 - 95), (screen_height//2 + 140))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer
    
    explosion_group.update()
    
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()
