times = int(input())

for i in range(0, times):
    numbers = input().split()
    a, b, c = float(numbers[0]), float(numbers[1]), float(numbers[2]) 
    mean = ((a*2) + (b*3) + (c*5))/10.0
    print(f'{mean:.1f}')
