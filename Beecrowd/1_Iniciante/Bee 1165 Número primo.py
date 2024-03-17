times = int(input())

for i in range(0, times):
    number = int(input())
    sum = 0
    for i in range(1, number+1):
        if number % i == 0:
            sum += i
    if sum == number+1:
        print(f'{number} eh primo')
    else:
        print(f'{number} nao eh primo')
