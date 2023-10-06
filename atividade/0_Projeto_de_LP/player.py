import pygame
from laser import Laser

class Player:
    def __init__(self, screen, width, hight, sizeScreen):
        self.shoot = Laser(width//2 - 30, hight - 50,sizeScreen, screen)
        self.screen = screen
        self.width = width//2 - 30
        self.hight = hight - 40
        self.max_width = sizeScreen[0]
        self.max_hight = sizeScreen[1]
        self.image = pygame.image.load(r'C://Users/Softex/Documents/GitHub/Python/atividade/0_Projeto_de_LP/assets/image/player.png')
        pass
   
   
    def draw_player(self):
        self.screen.blit(self.image, (self.width, self.hight))
        pass 
    
    def updeteCoordenation(self, movement):
        coordenationX = self.width
        coordenationY = self.hight
        
        if coordenationX <= 0:
            coordenationX = self.max_width
            coordenationY -= 5
        elif coordenationX >= self.max_width:
            coordenationX = 0
            
        if coordenationY <= 0:
            coordenationY =  self.max_hight
            
        if movement < 0:
            coordenationX -= 5
        elif movement > 0:
            coordenationX += 5
        
        self.width = coordenationX
        self.hight = coordenationY
        pass
    
    def update(self, movement):
        self.shoot.update()
        self.shoot.draw_laser()
        self.updeteCoordenation(movement)