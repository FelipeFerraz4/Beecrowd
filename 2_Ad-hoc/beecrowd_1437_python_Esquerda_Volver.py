import sys
while True:
    number = int(sys.stdin.readline())
    
    if number == 0:
        break
    
    commands = sys.stdin.readline().strip()
    orientation = 90
    for command in commands:
        if command == 'D':
            orientation = (orientation - 90) % 360
        else:
            orientation = (orientation + 90) % 360
    if orientation == 0:
        print('L')
    elif orientation == 90:
        print('N')
    elif orientation == 180:
        print('O')
    else:
        print('S')
