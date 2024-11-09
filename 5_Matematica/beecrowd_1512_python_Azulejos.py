import math

while True:
    values = list(map(int, input().split()))
    
    if sum(values) == 0:
        break
    
    multipleA = values[0] // values[1]
    multipleB = values[0] // values[2]
    intersectionAB = values[0] // math.lcm(values[1], values[2])
    
    
    tiles = multipleA + multipleB - intersectionAB
    
    print(tiles)