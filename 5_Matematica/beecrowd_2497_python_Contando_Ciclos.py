count = 1
while True:
    number = int(input())
    
    if number == -1:
        break
    
    print(f'Experiment {count}: {number // 2} full cycle(s)')
    count += 1