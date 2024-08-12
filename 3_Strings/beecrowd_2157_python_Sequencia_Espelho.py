tests_number = int(input())
for i in range(tests_number):
    values = input().split()
    number1 = int(values[0])
    number2 =  int(values[1])
    for number in range(number1, number2+1):
        print(number, end='')
    for number in range(number2, number1-1, -1):
        print(str(number)[::-1], end='')
    print()
     