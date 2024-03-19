times = int(input())

tentativa = [0, 0, 0]
acerto = [0, 0, 0]

for x in range(times):
    nome = input()
    tentativas = input().split()
    acertos = input().split()
    for i in range(len(tentativas)):
        tentativa[i] += int(tentativas[i])
    for i in range(len(acertos)):
        acerto[i] += int(acertos[i])

print(f'Pontos de Saque: {acerto[0]/tentativa[0] * 100:.2f} %.')
print(f'Pontos de Bloqueio: {acerto[1]/tentativa[1] * 100:.2f} %.')
print(f'Pontos de Ataque: {acerto[2]/tentativa[2] * 100:.2f} %.')
