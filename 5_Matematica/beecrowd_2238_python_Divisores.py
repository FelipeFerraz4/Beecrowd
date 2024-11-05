import math

A, B, C, D = map(int, input().split())

divisores_de_C = []
for i in range(1, int(math.sqrt(C) + 1)):
    if C % i == 0:
        divisores_de_C.append(i)
        if i != C // i:
            divisores_de_C.append(C // i)
            
divisores_de_C = sorted(divisores_de_C)
result = -1
for number in divisores_de_C:
    if number % A == 0 and number % B != 0 and D % number != 0:
        result = number
        break

print(result)