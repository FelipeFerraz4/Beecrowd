mensagem = str(input())

quantidade = mensagem.count('1')

if quantidade % 2 == 1:
    print(f'{mensagem}1')
else:
    print(f'{mensagem}0')
