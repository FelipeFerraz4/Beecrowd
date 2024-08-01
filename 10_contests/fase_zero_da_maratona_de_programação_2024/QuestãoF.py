from itertools import permutations
valor = int(input())

grupoDeParentes = input()
grupo = '()' * (valor//2)

print(permutations(grupo))