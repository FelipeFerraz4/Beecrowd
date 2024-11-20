while True:
    try:
        number = float(input())
        
        angle = number % 360
        if 0 <= angle < 90:
            print(f'Bom Dia!!')
        elif 90 <= angle < 180:
            print(f'Boa Tarde!!')
        elif 180 <= angle < 270:
            print(f'Boa Noite!!')
        else:
            print(f'De Madrugada!!')
        
        hour = (int((number * 240 / 3600)) + 6) % 24
        minute = int((number * 240 / 60)) % 60
        second = int((number * 240)) % 60    
        
        print(f'{hour:>02}:{minute:>02}:{second:>02}')
    except EOFError:
        break