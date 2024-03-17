count = 0
mean = 0

for i in range(0, 6):
    value = float(input())
    if value > 0:
        count += 1
        mean += value

mean /= count
print(f'{count} valores positivos')
print(f'{mean:.1f}')
