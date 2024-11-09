import math
while True:
    try:
        side = int(input())
        result = (8/5) * (side**2 * math.sqrt(3))/4
        print(f'{result:.2f}')
    except EOFError:
        break