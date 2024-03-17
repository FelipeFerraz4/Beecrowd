number1 = int(input())
number2 = int(input())

if number2 < number1:
    start = number2+1
    end = number1
else:
    start = number1+1
    end = number2

sum = 0

for i in range(start, end):
    if i % 2 == 1:
        sum += i

print(f'{sum}')
