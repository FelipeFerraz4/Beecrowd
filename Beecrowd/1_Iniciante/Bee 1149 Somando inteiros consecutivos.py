numbers = input().split()

number1 = int(numbers[0])
number2 = int(numbers[len(numbers)-1])

sum = 0

for i in range(0, number2):
    sum += number1 + i

print(sum)
