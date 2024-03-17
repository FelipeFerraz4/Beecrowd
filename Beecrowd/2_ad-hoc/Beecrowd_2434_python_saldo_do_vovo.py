valores = input().split()
dias = int(valores[0])
saldo = int(valores[1])

menorSaldo = saldo

for i in range(dias):
    valor = int(input())
    saldo += valor
    
    if saldo < menorSaldo:
        menorSaldo = saldo
 
print(menorSaldo)