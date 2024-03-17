quantidadePessoas = int(input())
pessoas = input().split()
menor = int(pessoas[0])

for x in range(quantidadePessoas):
    pessoa = int(pessoas[x])
    if pessoa <= menor:
        menor = pessoa

position = pessoas.index(str(menor))

print(position+1)
