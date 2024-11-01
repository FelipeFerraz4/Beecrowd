import math

while True:
    try:
        numbers = list(map(int, input().split()))
        
        semi_perimetro = sum(numbers)/2
        PI = 3.1415926535897
        
        aux = semi_perimetro
        for i in range(3):
            aux *= (semi_perimetro - numbers[i])
        area_triangulo = math.sqrt(aux)
        
        raio_circuncritito = (numbers[0]*numbers[1]*numbers[2])/(4*area_triangulo)
        area_circuncritito = PI * (raio_circuncritito**2)
        
        raio_inscrito = area_triangulo/semi_perimetro
        area_inscrito = PI * (raio_inscrito**2)
        
        sunflowers = area_circuncritito - area_triangulo
        violets = area_triangulo - area_inscrito
        roses = area_inscrito
        
        print(f'{sunflowers:.4f} {violets:.4f} {roses:.4f}')
        
    except EOFError:
        break
