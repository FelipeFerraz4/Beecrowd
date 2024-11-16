number = int(input())
position = input()
glass = [0, 0, 0]

if position == 'A':
    glass[0] = 1
elif position == 'B':
    glass[1] = 1
else:
    glass[2] = 1

for i in range(number):
    operation = int(input())
    
    if operation == 1:
        aux = glass[0]
        glass[0] = glass[1]
        glass[1] = aux
    elif operation == 2:
        aux = glass[1]
        glass[1] = glass[2]
        glass[2] = aux
    else:
        aux = glass[0]
        glass[0] = glass[2]
        glass[2] = aux

if glass[0] == 1:
    print('A')
elif glass[1] == 1:
    print('B')
else:
    print('C')