from sys import stdin

count = 1
while True:    
    farm = list(map(int, stdin.readline().split()))
    
    if sum(farm) == 0:
        break
    
    number_test = int(stdin.readline())
    meteorites_in_farm = 0
    
    big_x = max(farm[0], farm[2])
    small_x = min(farm[0], farm[2])
    big_y = max(farm[1], farm[3])
    small_y = min(farm[1], farm[3])
    
    for i in range(number_test):
        values = list(map(int, stdin.readline().split()))
        if small_x <= values[0] <= big_x and small_y <= values[1] <= big_y:
            meteorites_in_farm += 1
    
    print(f'Teste {count}')
    print(meteorites_in_farm)
    
    count += 1
