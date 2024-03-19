times = 1
while times != 0:
    times = int(input())
    for x in range(times):
        number = int(input())
        pedidos  = 0
        if number % 2 == 0 and number != 0:
            pedidos += 2 + ((number-2) * 2)
        elif number % 2 == 1:
            pedidos += 1 + ((number-1) * 2)
        
        print(pedidos)
