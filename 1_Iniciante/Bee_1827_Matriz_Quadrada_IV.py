while True:
  try:
    tamanho = int(input())
    borda = tamanho//3
    for i in range(tamanho):
        for j in range(tamanho):
            number = 0
            
            if i == j and i + j == tamanho - 1:
              number = 4
            elif (borda - 1 < j < tamanho - borda) and (borda - 1 < i < tamanho - borda):
                number = 1
            elif i + j == tamanho - 1:
              number = 3
            elif i == j:
              number = 2
              
            
            print(number, end='')
        print()
    print()
  except EOFError:
    break
