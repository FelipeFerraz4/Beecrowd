contador = 1
while True:
    try:
      numeroDoCaso = int(input())
      quantidade = 0
      numero = []
      valor = 1

      while valor <= numeroDoCaso:
        for x in range(valor):
            quantidade += 1
            numero.append(valor)
        valor += 1

      if numeroDoCaso == 0:
        print(f'Caso {contador}: {quantidade+1} numero')
        print('0')
      else:  
        print(f'Caso {contador}: {quantidade+1} numeros')
        print('0 ', end='')
        for x in range(quantidade):
            if x == quantidade-1:
                print(f'{numero[x]}')
            else:
                print(f'{numero[x]} ', end='')
    
      print()
      contador += 1
    except EOFError:
      break
