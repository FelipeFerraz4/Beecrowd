import math
valores = input().split()
dividendo = int(valores[0])
divisor = int(valores[1])

if divisor < 0:
  quociente = math.ceil(dividendo/divisor)
  resto = dividendo % (-divisor)
else:
  quociente = math.floor(dividendo/divisor)
  resto = dividendo % divisor

print(f'{quociente} {resto}')