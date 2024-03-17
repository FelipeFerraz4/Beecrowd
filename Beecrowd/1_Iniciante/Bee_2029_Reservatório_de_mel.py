while True:
  try:
    volume = float(input())
    raio = (float(input())) / 2
    
    area = 3.14 * (raio*raio)
    altura = volume / area
    
    print(f'ALTURA = {altura:.2f}')
    print(f'AREA = {area:.2f}')
    
    
  except EOFError:
    break
