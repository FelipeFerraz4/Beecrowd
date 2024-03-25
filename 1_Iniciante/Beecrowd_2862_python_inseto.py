measurements = int(input())

for i in range(measurements):
    nivel = int(input())
    
    if nivel <= 8000:
        print('Inseto!')
    else:
        print('Mais de 8000!')