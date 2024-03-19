ddd = int(input())

ddds = [[61, 'Brasilia'], [71, 'Salvador'],
        [11, 'Sao Paulo'], 
        [21, 'Rio de Janeiro'],
        [32, 'Juiz de Fora'], 
        [19, 'Campinas'], 
        [27, 'Vitoria'],
        [31, 'Belo Horizonte']]

count = 0

for i in range(0, 8):
    if ddd != ddds[i][0]:
        count += 1
    else:
        break

if count != 8:
    print(ddds[count][1])
else:
    print('DDD nao cadastrado')
