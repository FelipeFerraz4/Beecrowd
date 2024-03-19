times = int(input())
maiorNota = -1
matricula = 0

for x in range(times):
    valores = input().split()
    if float(valores[1]) > maiorNota:
        maiorNota = float(valores[1])
        matricula = valores[0]

if maiorNota < 8:
    print('Minimum note not reached')
else:
    print(matricula)
