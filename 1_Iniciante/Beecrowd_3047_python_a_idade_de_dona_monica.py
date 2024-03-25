monica = int(input())
filho1 = int(input())
filho2 = int(input())
maior = 0
if filho1 > filho2:
    maior = filho1
else:
    maior = filho2

filho3 = monica - (filho1+filho2)

if maior > filho3:
    print(maior)
else:
    print(filho3)
