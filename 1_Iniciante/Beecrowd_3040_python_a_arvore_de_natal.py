tests = int(input())

for i in range(tests):
    values = input().split()
    if 200 <= int(values[0]) <= 300:
        if int(values[1]) >= 50:
            if int(values[2]) >= 150:
                print('Sim')
                continue
    print('Nao')
