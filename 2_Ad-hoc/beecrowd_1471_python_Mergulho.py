import sys

while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
        n, r = map(int, line.split())

        returned = set(map(int, sys.stdin.readline().strip().split()))

        if n == r:
            print('*')
        else:
            missing = sorted(set(range(1, n + 1)) - returned)
            print(' '.join(map(str, missing)) + ' ')
    except EOFError:
        break
