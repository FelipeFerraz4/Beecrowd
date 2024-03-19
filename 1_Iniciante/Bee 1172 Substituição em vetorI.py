array = []
for i in range(0, 10):
    value = int(input())
    if value <= 0:
        value = 1
    array.append(value)
    print(f'X[{i}] = {array[i]}')
