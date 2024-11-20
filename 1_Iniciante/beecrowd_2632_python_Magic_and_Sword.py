import math
from sys import stdin

magic = {'fire': [200, 20, 30, 50], 'water': [300, 10, 25, 40], 'earth': [400, 25, 55, 70], 'air': [100, 18, 38, 60]}

def calculate_damage(enemy, magic_data):
    nearest_x = max(enemy[2], min(int(magic_data[2]), enemy[2] + enemy[0]))
    nearest_y = max(enemy[3], min(int(magic_data[3]), enemy[3] + enemy[1]))
    
    dist = math.sqrt((int(magic_data[2]) - nearest_x) ** 2 + (int(magic_data[3]) - nearest_y) ** 2)
    
    if dist <= magic[magic_data[0]][int(magic_data[1])]:
        return magic[magic_data[0]][0]
    return 0

number_test = int(input())
for i in range(number_test):
    enemy = list(map(int, stdin.readline().split()))
    magic_data = stdin.readline().split()
    print(calculate_damage(enemy, magic_data))    
