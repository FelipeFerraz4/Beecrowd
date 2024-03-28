values = input().split()
sizeFrut = int(values[0])
sizeText = int(values[1])
fruts = []
frutsIndex = []
reverseFruts = []
for i in range(sizeFrut):
    frut = str(input()).lower()
    fruts.append(frut)
    frutsIndex.append(0)
    reverseFruts.append(frut[::-1])

for i in range(sizeText):
    text = str(input()).lower()
    for j in range(sizeFrut):
        if fruts[j] in text:
            frutsIndex[j] = 1
    for j in range(sizeFrut):
        if reverseFruts[j] in text:
            frutsIndex[j] = 1

for i in range(sizeFrut):
    if frutsIndex[i] == 1:
        print(f'Sheldon come a fruta {fruts[i]}')
    else:
        print(f'Sheldon detesta a fruta {fruts[i]}')