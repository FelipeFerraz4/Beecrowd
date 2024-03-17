casos = 1
while True:
    try:
        subSequencia = str(input())
        sequencia = str(input())
        print(f'Caso #{casos}:')
        if sequencia.find(subSequencia) != -1:
            times = sequencia.count(subSequencia)
            print(f'Qtd.Subsequencias: {times}')
            print(f'Pos: {sequencia.rfind(subSequencia)+1}')
        else:
            print('Nao existe subsequencia')
        casos += 1
        print()
    except EOFError:
        break
