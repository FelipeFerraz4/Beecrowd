run = True
count = 1
while run:
    number = int(input())
    
    if number == 0:
        run = False
        break
    
    numbers = list(map(int, input().split()))
    print(f'Teste {count}')
    
    for i in range(number):
        if numbers[i] == i + 1:
            print(numbers[i])
            break
    print()
    count += 1