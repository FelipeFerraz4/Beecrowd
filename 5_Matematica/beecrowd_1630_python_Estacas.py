from math import gcd

while True:
    try:
        values = list(map(int, input().split()))
        number_gcd = gcd(values[0], values[1])
        total = 2 * (values[0] + values[1])
        estacas = total // number_gcd
        print(estacas)
    except EOFError:
        break