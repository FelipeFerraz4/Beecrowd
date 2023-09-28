import random

def level_jogo():    
    level1 = 20
    level2 = 10
    level3 = 5

    print('Nível do jogo: ')
    print('1 - Fácil')
    print('2 - Médio')
    print('3 - Difícil')

    level = int(input('Digite qual o nível: '))

    if level == 1:
        return level1
    elif level == 2:
        return level2
    else:
        return level3


def result(secret_number):
    number_user = -1
    while number_user < 0 or number_user > 100:
        number_user = int(input('Digite um número entre 0 e 100: '))

    if number_user == secret_number:
        print('Você acertou')
        return -1
    else:
        if number_user > secret_number:
            print(f'O número {number_user} é maior que o número secreto')
        else:
            print(f'O número {number_user} é menor que o número secreto')
        
        return abs(secret_number - number_user)



def number_secret():
    #number1 = int(random.random() * 100)
    #number2 = random.randrange(0, 101)
    number3 = random.randint(0, 100)
    return number3

if __name__ == "__main__":
    #gameLoop
    secret_number = number_secret()
    times = level_jogo()

    pontos = 1000
    print(f'Ponto: {pontos}')
    rodada = 1

    while rodada <= times:

        resultado = result(secret_number)
        
        if resultado == -1:
            break
        else:
            pontos -= resultado
        rodada +=1

    print(f'Ponto: {pontos}')
    print(f'Número secreto: {secret_number}')