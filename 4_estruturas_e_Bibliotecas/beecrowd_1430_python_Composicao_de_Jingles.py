from sys import stdin
while True:
    compassos = list(map(str, stdin.readline().split('/')))
    if '*' in compassos[0]:
        break
    notas = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}
    count = 0
    for compasso in compassos[:len(compassos) - 1]:
        sum_nota = 0
        for nota in compasso:
            sum_nota += notas[nota]
        if sum_nota == 1:
            count += 1
    print(count)