import sys

while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
        number = int(line)
        boots = {}
        for _ in range(number):
            line = sys.stdin.readline().strip()
            if not line:
                continue
            num, side = line.split()
            if num in boots:
                if side == 'D':
                    boots[num][0] += 1
                else:
                    boots[num][1] += 1
            else:
                if side == 'D':
                    boots[num] = [1, 0]
                else:
                    boots[num] = [0, 1]
        pairs = 0
        for boot in boots.values():
            pairs += min(boot)
        print(pairs)
    except ValueError:
        break
