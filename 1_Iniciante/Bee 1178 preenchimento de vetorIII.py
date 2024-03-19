value = float(input())
count = 0

while count < 100:
    print(f'N[{count}] = {value:.4f}')
    value /= 2
    count += 1
