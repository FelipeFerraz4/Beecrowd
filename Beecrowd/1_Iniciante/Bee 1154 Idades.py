status = 0
mean = 0
counter = 0

while status != 1:
    number = int(input())
    if number < 0:
        status = 1
        break
    else:
        counter += 1
        mean += number

mean /= counter
print(f'{mean:.2f}')
