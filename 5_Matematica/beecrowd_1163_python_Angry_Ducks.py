import math

PI = 3.14159
G = 9.80665

def distance_max(height, angle, velocity):
    angle_rad = angle * (PI / 180.0)
    
    velocity_x = velocity * math.cos(angle_rad)
    velocity_y = velocity * math.sin(angle_rad)
    
    delta = velocity_y**2 + 2 * height * G
    time = (velocity_y + math.sqrt(delta)) / G
    distance_end = velocity_x * time
    return distance_end
    
while True:
    try:
        height = float(input())
        p1, p2 = map(int, input().split())
        number_tests = int(input())
        
        for i in range(number_tests):
            angle, velocity = map(float, input().split())
            
            distance = distance_max(height, angle, velocity)
            
            if p1 <= distance <= p2:
                print(f'{distance:.5f} -> DUCK')
            else:
                print(f'{distance:.5f} -> NUCK')
    except EOFError:
        break
