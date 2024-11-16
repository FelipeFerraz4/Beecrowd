number = int(input())
for _ in range(number):
    scoreJ = 0
    scoreM = 0
    for _ in range(3):
        data = list(map(int, input().split()))
        scoreJ += data[0] * data[1]
    for _ in range(3):
        data = list(map(int, input().split()))
        scoreM += data[0] * data[1]
    if scoreM > scoreJ:
        print('MARIA')
    else:
        print('JOAO')