number_tests = int(input())
for i in range(number_tests):
    values = input().split()
    number1 = int(values[0])
    number2 = int(values[1])
    
    if number1 >= number2:
        big = number1
        small = number2
    else:
        big = number2
        small = number1
    
    resto = big % small
    while resto != 0:
        big = small
        small = resto
        resto = big % small
        
    print(small)