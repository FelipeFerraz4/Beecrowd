times = int(input())

for x in range(times):
    dadosDaPessoa = input().split()
    if dadosDaPessoa[0] == 'Thor':
        print('Y')
    else:
        print('N')
