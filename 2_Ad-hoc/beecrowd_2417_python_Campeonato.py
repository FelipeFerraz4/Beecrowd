values = list(map(int, input().split()))

pointC = values[0] * 3 + values[1]
pointF = values[3] * 3 + values[4]

if pointC > pointF:
    print('C')
elif pointF > pointC:
    print('F')
else:
    if values[2] > values[5]:
        print('C')
    elif values[5] > values[2]:
        print('F')
    else:
        print('=')