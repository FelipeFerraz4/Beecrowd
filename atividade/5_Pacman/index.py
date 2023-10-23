import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800,600),0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

class Pacman(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.centroX = 400
        self.centroY = 300
        self.centro = (self.centroX, self.centroY)
        self.tamanho = 100
        self.raio = self.tamanho // 2
        self.current = 0
        self.speed_x = 1
        self.speed_y = 1

    
    def draw_screen1(self, Screen):
        pygame.draw.circle(Screen, YELLOW, self.centro, self.raio, 0)

        pointInferior = (self.centroX + self.raio, self.centroY + self.raio)
        pointSuperior = (self.centroX + self.raio, self.centroY - self.raio)
        boca = (self.centro, pointInferior, pointSuperior)

        pygame.draw.polygon(Screen, BLACK, boca, 0)

        pygame.draw.circle(screen, BLACK, (self.centroX + self.raio//5, self.centroY - self.raio//5 * 3), 7, 0)


    def draw_screen2(self, Screen):
        pygame.draw.circle(Screen, YELLOW, self.centro, self.raio, 0)

        pointInferior = (self.centroX + self.raio, self.centroY + self.raio//5 * 3)
        pointSuperior = (self.centroX + self.raio, self.centroY - self.raio//5 * 3)
        boca = (self.centro, pointInferior, pointSuperior)

        pygame.draw.polygon(Screen, BLACK, boca, 0)

        pygame.draw.circle(screen, BLACK, (self.centroX + self.raio//5, self.centroY - self.raio//5 * 3), 7, 0)


    def draw_screen3(self, Screen):
        pygame.draw.circle(Screen, YELLOW, self.centro, self.raio, 0)

        pointInferior = (self.centroX + self.raio, self.centroY + self.raio//5 * 1)
        pointSuperior = (self.centroX + self.raio, self.centroY - self.raio//5 * 1)
        boca = (self.centro, pointInferior, pointSuperior)

        pygame.draw.polygon(Screen, BLACK, boca, 0)

        pygame.draw.circle(screen, BLACK, (self.centroX + self.raio//5, self.centroY - self.raio//5 * 3), 7, 0)


    def draw_screen4(self, Screen):
        pygame.draw.circle(Screen, YELLOW, self.centro, self.raio, 0)

        pointInferior = (self.centroX + self.raio, self.centroY )
        pointSuperior = (self.centroX + self.raio, self.centroY )
        boca = (self.centro, pointInferior, pointSuperior)

        pygame.draw.polygon(Screen, BLACK, boca, 0)

        pygame.draw.circle(screen, BLACK, (self.centroX + self.raio//5, self.centroY - self.raio//5 * 3), 7, 0)


if __name__ == "__main__":
    pacman = Pacman(screen)
    screen.fill((0,0,0))
    
    figura = 1

    while True:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if figura == 1:
                        figura += 1
                    elif figura == 2:
                        figura += 1
                    elif figura == 3:
                        figura += 1
                    else:
                        figura = 1
                    
        if figura == 1:
            pacman.draw_screen1(screen)
        elif figura == 2:
            pacman.draw_screen2(screen)
        elif figura == 3:
            pacman.draw_screen3(screen)
        else:
            pacman.draw_screen4(screen)
        
        

