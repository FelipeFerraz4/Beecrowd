from sys import stdin

while True:
    try:
        x1, y1, x2, y2 = map(int, stdin.readline().split())

        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break

        if x1 == x2 and y1 == y2:
            print(0)
        elif x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
            print(1)
        else:
            print(2)

    except EOFError:
        break
