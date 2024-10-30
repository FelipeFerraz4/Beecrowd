import math

while True:
    try:
        values = list(map(int, input().split()))
        distanciaG = math.sqrt((values[0]**2) + (12**2))
        tempoL = 12/values[1]
        tempoG = distanciaG/values[2]
        if tempoL < tempoG:
            print('N')
        else:
            print('S')
    except EOFError:
        break