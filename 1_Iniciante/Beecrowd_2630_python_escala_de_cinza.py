time = int(input())
for x in range(time):
    operational_type = str(input())
    
    values = input().split()
    red = int(values[0])
    green = int(values[1])
    blue = int(values[2])
    
    grey_scale = 0
    
    if(operational_type == 'eye'):
        grey_scale = (red*0.3) + (green*0.59) + (blue*0.11)
    elif (operational_type == 'mean'):
        grey_scale = (red + green + blue) // 3
    elif (operational_type == 'max'):
        grey_scale = max(red, green, blue)
    else:
        grey_scale = min(red, green, blue)
        
    print(f'Caso #{x+1}: {int(grey_scale)}')