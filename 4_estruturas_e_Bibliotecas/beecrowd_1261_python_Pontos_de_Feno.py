import sys

numbers = list(map(int, sys.stdin.readline().split()))
hay_points = {}

for _ in range(numbers[0]):
    line = sys.stdin.readline().strip()
    word, value = line.split()
    hay_points[word] = int(value)
    
for _ in range(numbers[1]):
    total = 0
    while True:
        line = sys.stdin.readline().strip()
        for word in line.split():
            total += hay_points.get(word, 0)
        if line.count('.') == 1:
            break
    print(total)
