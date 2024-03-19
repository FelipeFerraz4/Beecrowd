times = int(input())
valores = input().split()
carneiros = []
LocaisRoubados = []


for x in valores:
  carneiros.append(int(x))
  LocaisRoubados.append(0)

contador = 0
while 0 <= contador < times:
    if carneiros[contador] > 0:
        carneirosAntigos = carneiros[contador]
        carneiros[contador] -= 1
        
        LocaisRoubados[contador] = 1
        
        if carneirosAntigos % 2 == 0:
            contador -= 1
        else:
            contador += 1
    else:
        break

print(f'{sum(LocaisRoubados)} {sum(carneiros)}')
