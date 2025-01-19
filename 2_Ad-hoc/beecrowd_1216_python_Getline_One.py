import sys
sum_distance = 0
count = 0
while True:
    try:
        name = sys.stdin.readline().strip()
        if not name:
            break
        sum_distance += float(sys.stdin.readline())
        count += 1
    except EOFError:
        break
    
mean = sum_distance / count
print(f'{mean:.1f}')