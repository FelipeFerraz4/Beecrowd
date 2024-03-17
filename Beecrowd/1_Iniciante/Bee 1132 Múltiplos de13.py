number1 = int(input())
number2 = int(input())
sum = 0

if number2 > number1:
    for i in range(number1, number2+1):
        if i % 13 != 0:
            sum += i
else:
    for i in range(number2, number1+1):
        if i % 13 != 0:
            sum += i

print(sum)