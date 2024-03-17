array = []
for i in range(0, 20):
    value = int(input())
    array.append(value)

for i in range(0, 20):
    print(f'N[{i}] = {array[19 - i]}')
