import math

while True:
    try:
        values = list(map(float, input().split()))
        
        angle_radians = math.radians(values[0])
        tree = ((values[1] * math.tan(angle_radians)) + values[2]) * 5
        
        print(f'{tree:.2f}')
    except EOFError:
        break