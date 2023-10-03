import pygame

pygame.init()
screen = pygame.display.set_mode((800,600),0)

while True:
    #pygame.draw.rect(screen, (46,46,200), (400, 300, 200,200), 2)
    #rect = (600, 500, 50, 50)
    #pygame.draw.rect(screen, (45,200,61), rect)
    #pygame.draw.polygon(screen, (200,56,21), [(100,100), (200,200), (100,200)],3)
    #pygame.draw.line(screen, (255,255,0), (300,0),(300, 500), 3)

    point1 = (200, 200)
    point2 = (600, 200)
    point3 = (400, 100)

    point4 = (250, 250)
    point5 = (450, 250)

    color1 = (50, 100, 200)
    AMARELO = (255,255,0)
    PRETO = (0,0,0)

    casaEstrutura = (point1[0], point1[1], 400,150)
    pygame.draw.rect(screen, color1, casaEstrutura, 3)
    
    casaTelhado = [point1, point2, point3]
    pygame.draw.polygon(screen, color1, casaTelhado, 3)

    casaPortao = (point4[0], point4[1], 150, 100)
    pygame.draw.rect(screen, color1, casaPortao, 3)

    casaPorta = (point5[0], point5[1], 70, 100)
    casaFechadura = (510, 300)
    pygame.draw.rect(screen, color1, casaPorta, 3)
    pygame.draw.circle(screen, color1, casaFechadura, 5, 3)

    pygame.draw.line(screen, color1, (250, 300), ((400, 300)))
    pygame.draw.line(screen, color1, (250, 280), ((400, 280)))
    pygame.draw.line(screen, color1, (250, 320), ((400, 320)))
    

    pygame.display.update()

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()

