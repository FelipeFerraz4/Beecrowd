letras = ['A', 'B', 'C', 'D', 'E']
run = True
while run:
    number_tests = int(input())
    
    if number_tests == 0:
        run = False
        break
    
    for item in range(number_tests):
        valores = list(map(int, input().split()))
        letra = []
        for item in range(5):
            if valores[item] <= 127:
                letra.append(letras[item])
                
        if len(letra) == 1:
            print(letra[0])
        else:
            print('*')