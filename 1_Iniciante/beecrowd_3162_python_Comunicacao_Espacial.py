import math
from sys import stdin
number_test = int(input())
naves = []
for i in range(number_test):
    naves.append(list(map(int, stdin.readline().split())))
for i in range(number_test):
    distance = []
    for j in range(number_test):
        if i != j:
            aux = sum((naves[i][k] - naves[j][k])**2 for k in range(3))
            distance.append(math.sqrt(aux))
    min_distance = min(distance)
    if min_distance <= 20:
        print('A')
    elif min_distance <= 50:
        print('M')
    else:
        print('B')
