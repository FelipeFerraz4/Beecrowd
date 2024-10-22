run = True
while run:
    values = list(map(int, input().split()))
    if values[0] == values[1] == 0:
        run = False
        break
    
    print(values[0] + values[1])
        