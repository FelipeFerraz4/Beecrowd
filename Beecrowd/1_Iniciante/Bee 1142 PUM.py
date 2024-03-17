times = int(input())

count = 1
for i in range(0, times):
    for j in range(0, 4):
        if j == 3:
            print('PUM')
        else:
            print(f'{count+j}', end=' ')
    count += 4
