while True:
    try:
        alfabeto = str(input())
        numeroLampada = int(input())
        lampadas = input().split()
        mensagem = []
        for x in lampadas:
            mensagem.append(alfabeto[int(x) - 1])
        print(''.join(mensagem))
    except EOFError:
        break