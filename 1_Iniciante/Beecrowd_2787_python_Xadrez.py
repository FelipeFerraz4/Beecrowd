linhas = int(input())
colunas = int(input())

cor = 0

if linhas % 2 == 1:
    cor = 1

if colunas % 2 == 0:
    if cor == 1:
        cor = 0
    else:
        cor = 1 

print(cor)