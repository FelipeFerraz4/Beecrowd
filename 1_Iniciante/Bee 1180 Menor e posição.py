times = int(input())

numbers = input().split()
menor = 0
posicao = 0

for i in range(0, times):
    number = int(numbers[i])
    if i == 0:
        menor = number
    
    if number < menor:
        menor = number
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
