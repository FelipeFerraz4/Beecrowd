import math

values = list(map(int, input().split()))
plates = values[0] * values[1]
for i in range(10, 90 + 1, 10):
    if i == 90:
        print(math.ceil(i * plates / 100))
    else:
        print(math.ceil(i * plates / 100), end=' ')
