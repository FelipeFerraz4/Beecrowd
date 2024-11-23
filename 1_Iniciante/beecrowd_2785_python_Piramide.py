n = int(input())
minimos = list(map(int, input().split()))
for i in range(2, n + 1):
    linha = list(map(int, input().split()))
    soma = sum(linha[:i])
    for j in range(n - i + 1):
        a = min(minimos[j], minimos[j + 1])
        minimos[j] = soma + a
        if j < n - i:
            soma += linha[j + i] - linha[j]

print(minimos[0])
