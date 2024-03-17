times = int(input())

rabbit = 0
frog = 0
mouse = 0

for i in range(0, times):
    data = input().split()
    number = int(data[0])
    animal = data[1]

    if animal == 'C':
        rabbit += number
    elif animal == 'R':
        mouse += number
    else:
        frog += number

total = rabbit+mouse+frog
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {rabbit}')
print(f'Total de ratos: {mouse}')
print(f'Total de sapos: {frog}')
print(f'Percentual de coelhos: {100*rabbit/total:.2f} %')
print(f'Percentual de ratos: {100*mouse/total:.2f} %')
print(f'Percentual de sapos: {100*frog/total:.2f} %')
