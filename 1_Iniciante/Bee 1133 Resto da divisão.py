number1 = int(input())
number2 = int(input())

if number2 > number1:
    for i in range(number1+1, number2):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
else:
    for i in range(number2+1, number1):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
