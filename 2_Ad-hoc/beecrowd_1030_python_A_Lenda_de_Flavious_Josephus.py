from sys import stdin

number_test = int(stdin.readline())
for i in range(number_test):
    n, k = map(int, stdin.readline().split())
    result = 0
    for j in range(1, n + 1):
        result = (result + k) % j
    print(f'Case {i + 1}: {result + 1}')
    