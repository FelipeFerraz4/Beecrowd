while True:
    try:
        text = input()
        if text == 'esquerda':
            print('ingles')
        elif text == 'direita':
            print('frances')
        elif text == 'nenhuma':
            print('portugues')
        else:
            print('caiu')
    except EOFError:
        break