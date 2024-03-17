ranks = [1, 3, 5, 10, 25, 50, 100]

colocacao = int(input())

for i in range(len(ranks)):
    if colocacao <= ranks[i]:
        print(f'Top {ranks[i]}')
        break
        