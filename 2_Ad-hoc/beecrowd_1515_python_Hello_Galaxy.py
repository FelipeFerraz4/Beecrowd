run = True
while run:
    number = int(input())
    
    if number == 0:
        run = False
        break
    
    planet = ''
    year = 0
    
    for i in range(number):
        values = input().split()
        
        if i == 0:
            planet = values[0]
            year = int(values[1]) - int(values[2])
        
        if int(values[1]) - int(values[2]) < year:
            year = int(values[1]) - int(values[2])
            planet = values[0]
    
    print(planet)    
