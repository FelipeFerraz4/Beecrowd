value = int(input())
count = 0
number = 0

while count < 1000:
    print(f'N[{count}] = {number}')
    if number == value-1:
        number = 0
    else:
        number += 1
    count += 1
