from sys import stdin
number_test = int(stdin.readline())
for _ in range(number_test):
    buy_list = set(map(str, stdin.readline().split()))
    print(' '.join(sorted(buy_list)))