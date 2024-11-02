while True:
    try:
        number1 = input().strip()
        number2 = input().strip() 
        formatted_number1 = print(f'${int(number1):,}', end='')
        number2 = print(f'.{int(number2):02}')
    except EOFError:
        break
