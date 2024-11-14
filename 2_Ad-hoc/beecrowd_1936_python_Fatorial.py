number = int(input())

factorials = []
fat = 1
i = 1

while fat <= number:
    factorials.append(fat)
    i += 1
    fat *= i

count = 0
index = len(factorials) - 1

while number > 0:
    while factorials[index] > number:
        index -= 1
    number -= factorials[index]
    count += 1

print(count)