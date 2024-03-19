import math

numeroFibonacci = int(input())

raiz5 = math.sqrt(5)

primeiroTermo = ((1 + raiz5) / 2)**numeroFibonacci
segundoTermo = ((1 - raiz5) / 2)**numeroFibonacci
fibonacci = (primeiroTermo - segundoTermo) // raiz5

print(f'{fibonacci:.1f}')
