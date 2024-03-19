password = 0
while password != 2002:
    password = int(input())
    if password == 2002:
        print('Acesso Permitido')
    else:
        print('Senha Invalida')
