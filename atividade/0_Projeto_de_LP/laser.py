import pygame

class Laser:
    def __init__(self, width, hight, sizeScreen, screen):
        self.screen = screen
        self.width = width
        self.hight = hight
        self.max_width = sizeScreen[0]
        self.max_hight = sizeScreen[1]
        pass
    
    def draw_laser(self):
        pygame.draw.rect(self.screen, (255,255,255), 
                         (self.width, self.hight, 3, 10), 0)
        
    def update(self):
        coordenationX = self.width
        coordenationY = self.hight
        
        if coordenationY <= 0:
            coordenationY =  self.max_hight
            coordenationX += 20 
        
        if coordenationX >= self.max_width:
            coordenationX = 0
        
        coordenationY = coordenationY-5
        
        self.width = coordenationX
        self.hight = coordenationY