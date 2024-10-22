roupas = int(input())
lavadeira = list(map(int, input().split()))
secadeira = list(map(int, input().split()))

test = False
if lavadeira[0] <= roupas <= lavadeira[1]:
    if secadeira[0] <= roupas <= secadeira[1]:
        test = True

if test:
    print('possivel')
else:
    print('impossivel')
