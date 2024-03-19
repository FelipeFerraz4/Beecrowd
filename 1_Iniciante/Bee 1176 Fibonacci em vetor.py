times = int(input())
for i in range(0, times):
    value = int(input())
    if value == 0:
        print(f'Fib({value}) = {0}')
    elif value == 1:
        print(f'Fib({value}) = {1}')
    else:
        fib2 = 0
        fib1 = 1
        for i in range(1, value):
            aux = fib1 + fib2
            fib2 = fib1 
            fib1 = aux
        print(f'Fib({value}) = {fib1}')
