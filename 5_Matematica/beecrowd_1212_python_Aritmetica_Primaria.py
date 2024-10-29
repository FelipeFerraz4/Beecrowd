run = True
while run:
    numbers = input().split()
    number1 = numbers[0][::-1]
    number2 = numbers[1][::-1]
    number_carry = 0
    carry = 0
    
    if number1 == number2 == '0':
        run = False
        break
    
    for i in range(0, max(len(number1), len(number2))):
        if i < len(number1):
            value1 = int(number1[i])
        else:
            value1 = 0
        
        if i < len(number2):
            value2 = int(number2[i])
        else:
            value2 = 0
        
        result = value1 + value2 + carry
        if result > 9:
            carry = 1
            number_carry += 1
        else:
            carry = 0

    if number_carry == 0:
        print('No carry operation.')
    elif number_carry == 1:
        print('1 carry operation.')
    else:
        print(f'{number_carry} carry operations.')            