import math

run = True
count = 1
while run:
    values = list(map(int, input().split()))
    
    if sum(values) == 0:
        run = False
        break
    
    if values[1] >= values[0]:
        print(f'Case {count}: 0')
    else:
        result = math.ceil((values[0] - values[1]) / values[1])
        if result > 26:
            print(f'Case {count}: impossible')
        else:
          print(f'Case {count}: {result}')
        
    count += 1
        