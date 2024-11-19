number_test = int(input())
rain = [0, 0]
used = [0, 0]
for i in range(number_test):
    days = input().split()
    if days[0] == 'chuva':
        if used[1] == 0:
            rain[0] += 1
            used[0] += 1
        else:
            used[1] -= 1
            used[0] += 1
    
    if days[1] == 'chuva':
        if used[0] == 0:
            rain[1] += 1
            used[1] += 1
        else:
            used[0] -= 1
            used[1] += 1
print(f'{rain[0]} {rain[1]}')