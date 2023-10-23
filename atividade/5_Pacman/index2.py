import pygame, sys

pygame.init()
sizeScreen = (800,600)
screen = pygame.display.set_mode(sizeScreen,0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

class Pacman(pygame.sprite.Sprite):
    def __init__(self, screen, sizeScreen):
        self.screen = screen
        self.centroX = 400
        self.centroY = 300
        self.tamanho = 100
        self.raio = self.tamanho // 2
        self.current = 0
        self.speed_x = 0.2
        self.speed_y = 0.2
        self.max_width = sizeScreen[0]
        self.max_hight = sizeScreen[1]


    def draw_screen(self):
        pygame.draw.circle(self.screen, YELLOW, (self.centroX, self.centroY), self.raio, 0)

        pointInferior = (self.centroX + self.raio, self.centroY + self.raio//5 * 3)
        pointSuperior = (self.centroX + self.raio, self.centroY - self.raio//5 * 3)
        boca = ((self.centroX, self.centroY), pointInferior, pointSuperior)

        pygame.draw.polygon(self.screen, BLACK, boca, 0)

        pygame.draw.circle(screen, BLACK, (self.centroX + self.raio//5, self.centroY - self.raio//5 * 3), 7, 0)
        
        
    def update(self, movement_x, movement_y):
        if movement_x > 0:
            self.centroX += self.speed_x
        elif movement_x < 0:
            self.centroX -= self.speed_x
            
        if movement_y > 0:
            self.centroY -= self.speed_y
        elif movement_y < 0:
            self.centroY += self.speed_y

        if self.centroX >= self.max_width - self.raio:
            self.centroX = self.max_width - self.raio
        elif self.centroX <= self.raio:
            self.centroX = self.raio
        
        if self.centroY >= self.max_hight - self.raio:
            self.centroY = self.max_hight - self.raio
        elif self.centroY <= self.raio:
            self.centroY = self.raio


if __name__ == "__main__":
    pacman = Pacman(screen, sizeScreen)
    movement_x = 0
    movement_y = 0

    while True:
        pygame.display.update()
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.update(movement_x=-1, movement_y=0)
                elif event.key == pygame.K_RIGHT:
                    pacman.update(movement_x=+1, movement_y=0)
                elif event.key == pygame.K_UP:
                    pacman.update(movement_x=0, movement_y=+1)
                elif event.key == pygame.K_DOWN:
                    pacman.update(movement_x=-1, movement_y=-1)
                    
        if pygame.key.get_pressed()[pygame.K_UP]:
            pacman.update(movement_x=0, movement_y=+1)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            pacman.update(movement_x=0, movement_y=-1)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            pacman.update(movement_x=-1, movement_y=0)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            pacman.update(movement_x=+1, movement_y=0)
            
        
        pacman.draw_screen()

