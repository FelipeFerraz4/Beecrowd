from sys import stdin

number_test = int(stdin.readline())
for _ in range(number_test):
    length = int(stdin.readline())
    sequence = list(map(int, stdin.readline().split()))
    phase = str(stdin.readline().strip())
    result = 0
    for i in range(length):
        if (sequence[i] == 1 or sequence[i] == 2) and phase[i] == 'S':
            result += 1
        elif sequence[i] > 2 and phase[i] == 'J':
            result += 1
    print(result)