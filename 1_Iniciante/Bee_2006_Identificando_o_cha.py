cha = input()
chutes = input().split()
contador = 0

for x in chutes:
    if x == cha:
        contador += 1

print(contador)
