times = int(input())
times *= 2
state = 0
i = 1

for j in range(1, times+1):
    if state == 0:
        print(f'{i} {i*i} {i*i*i}')
        state = 1
    else:
        print(f'{i} {(i*i)+1} {(i*i*i)+1}')
        state = 0
        i += 1
