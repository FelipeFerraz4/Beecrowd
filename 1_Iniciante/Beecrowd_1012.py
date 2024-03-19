value = input().split()
a, b, c = float(value[0]), float(value[1]), float(value[2])
PI = 3.14159

triangulo = a * c / 2
circulo = PI * (c**2)
trapezio = ((a + b) * c)/2
quadrado = b * b
retangulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
