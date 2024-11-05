run = True
count = 0
while run:
    number = int(input())
    
    if number == -1:
        run = False
        break
    
    values = list(map(int, input().split()))
    sum = 0
    for number in values:
        sum += number
        if sum % 100 == 0:
            count += 1
            sum = 0
    
    print(count)
    count = 0