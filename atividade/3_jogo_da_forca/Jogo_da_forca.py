import random

def secreta_palavra():
    palavras = ['Monitor', 'Teclado', 'Mouse', 
                'Impressora', 'Scanner', 'Notebook']

    return palavras[random.randrange(0, len(palavras))].upper()

if __name__ == '__main__':

    palavra_secreta = secreta_palavra()
    palavra_secretaOriginal = palavra_secreta

    palavra_user = len(palavra_secreta) * '_'

    life = 7

    while life > 0:
        print(palavra_user)
        letra_user = input('Digite uma letra:').strip().upper()

        if letra_user in palavra_secreta:
            while letra_user in palavra_secreta:
                start = 0
                end = len(palavra_secreta)
                position = palavra_secreta.find(letra_user, start, end)
                palavra_user.split()
                palavra_user = palavra_user[0:position] + letra_user + palavra_user[position+1:end]
                palavra_secreta = palavra_secreta[0:position] + '*' + palavra_secreta[position+1:end]
                start = position
            print('letra encontrada')
        else:
            print('letra não encontrada')
            life -=1
        
        if palavra_user == palavra_secretaOriginal:
            break

    print(palavra_user)
    print(f'Palavra secreta: {palavra_secretaOriginal}')
