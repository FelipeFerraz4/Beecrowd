number = int(input())
for _ in range(number):
    values = input()
    index = values.index('!')
    numero1 = values[:index]
    numero2 = len(values) - len(numero1)
    count = 1
    numero1 = int(numero1)
    result = numero1
    while numero1 - (count * numero2) >= 1:
        result *= numero1 - (count * numero2)
        count += 1
    print(result)