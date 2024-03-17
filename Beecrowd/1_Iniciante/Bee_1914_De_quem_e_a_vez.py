times = int(input())

for x in range(times):
    dadosPessoas = input().split()
    dadosJogo = input().split()
    soma = int(dadosJogo[0]) + int(dadosJogo[1])
    
    if soma % 2 == 0:
        if dadosPessoas[1] == 'PAR':
          print(dadosPessoas[0])
        else:
          print(dadosPessoas[2])
    else:
        if dadosPessoas[1] == 'IMPAR':
          print(dadosPessoas[0])
        else:
          print(dadosPessoas[2])
