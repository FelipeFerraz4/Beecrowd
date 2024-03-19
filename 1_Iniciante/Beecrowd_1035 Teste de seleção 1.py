value = input().split()
a, b, c, d = int(value[0]), int(value[1]), int(value[2]), int(value[3])

if b > c and d > a and (c+d) > (a+b) and c >= 0 and d >= 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
