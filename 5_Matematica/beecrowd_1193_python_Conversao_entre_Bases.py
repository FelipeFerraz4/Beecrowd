number_tests = int(input())
for i in range(number_tests):
    number_base = input().split()
    
    print(f'Case {i+1}:')
    if number_base[1] == 'bin':
        print(f'{int(number_base[0], 2)} dec')
        print(f'{hex(int(number_base[0], 2))[2:]} hex')
    elif number_base[1] == 'dec':
        print(f'{hex(int(number_base[0]))[2:]} hex')
        print(f'{bin(int(number_base[0]))[2:]} bin')
    else:
        print(f'{int(number_base[0], 16)} dec')
        print(f'{bin(int(number_base[0], 16))[2:]} bin')
    print()