elfos = int(input())
horas = [0, 0, 0, 0]
for i in range(elfos):
    info = input().split()
    if info[1] == 'bonecos':
        horas[0] += int(info[2])
    elif info[1] == 'arquitetos':
        horas[1] += int(info[2])
    elif info[1] == 'musicos':
        horas[2] += int(info[2])
    else:
        horas[3] += int(info[2]) 
print((horas[0]//8) + (horas[1]//4) + (horas[2]//6) + (horas[3]//12))