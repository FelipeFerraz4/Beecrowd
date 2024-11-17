number_test = int(input())
money_V = 0
money_G = 0
for i in range(number_test):
    values = input().split()
    if values[0] == 'G':
        money_G += int(values[1])
    else:
        money_V += int(values[1])

if money_V >= money_G:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
