even = 2
sum = 1

for i in range(3, 41, 2):
    sum += i/even
    even *= 2

print(f'{sum:.2f}')
