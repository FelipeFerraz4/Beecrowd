values = list(map(int, input().split()))

if values[0] == 1:
    if values[1] == 1:
        print('A')
    else:
        print('B')
else:
    print('C')