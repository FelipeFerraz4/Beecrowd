while True:
    try:
        membros = int(input())
        votos = input().split()
        contra = 0
        afavor = 0
        for x in range(membros):
            if votos[x] == '0':
                contra += 1
            else:
                afavor += 1
        if afavor >= (2/3) * membros:
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break