# Não é aprovado no Beecrowd -> Time limit exceeded
while True:
    try:
        n = int(input())
        if n == 0:
            break
        
        pacotes = list(map(int, input().split()))
        tempos = list(map(int, input().split()))
        
        tempo_total = 0
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if pacotes[j] > pacotes[j + 1]:
                    pacotes[j], pacotes[j + 1] = pacotes[j + 1], pacotes[j]
                    tempos[j], tempos[j + 1] = tempos[j + 1], tempos[j]
                    tempo_total += tempos[j]
        
        print(tempo_total)
    except EOFError:
        break