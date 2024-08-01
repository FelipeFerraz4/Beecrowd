numeroCrianca = int(input())

criancas = input().split()
criancasEmOrdem = input().split()

for i in range(numeroCrianca):
    if i != numeroCrianca - 1:
        print(criancasEmOrdem[0], end=' ')
    else:
        print(criancasEmOrdem[0])

    if criancas[0] == criancasEmOrdem[0]:
        criancas.pop(0)
        criancasEmOrdem.pop(0)
    else:
        criancasEmOrdem.remove(criancas[0])
        criancas.pop(0)
        
    
