while True:
    try:
        number = int(input())
        number = number % 360
        if 0 <= number < 90:
            print('Bom Dia!!')
        elif 90 <= number < 180:
            print('Boa Tarde!!')
        elif 180 <= number < 270:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')
    except EOFError:
        break