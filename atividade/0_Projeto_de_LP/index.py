import pygame, sys
from laser import Laser
from player import Player

if __name__ == "__main__":
    pygame.init()
    
    screen_width = 800
    screen_hight = 600
    sizeScreen = (screen_width, screen_hight)
    
    screenGame = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption('Defesa Alienígena')
    nave = Player(screenGame, screen_width, screen_hight, sizeScreen)
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(80)
        screenGame.fill((0,0,0))
        
        nave.draw_player()
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    nave.update(movement=-1)
                elif event.key == pygame.K_RIGHT:
                    nave.update(movement=+1)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            nave.update(movement=+1)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            nave.update(movement=-1)
        pygame.display.update()
                
