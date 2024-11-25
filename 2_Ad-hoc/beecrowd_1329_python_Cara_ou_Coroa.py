from sys import stdin
while True:
    number_test = int(stdin.readline())
    if number_test == 0:
        break
    win_jonh = sum(list(map(int, stdin.readline().split())))
    print(f'Mary won {number_test - win_jonh} times and John won {win_jonh} times')