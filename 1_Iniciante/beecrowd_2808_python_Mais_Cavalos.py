position = input().split()
position_number = [ord(position[0][0]), int(position[0][1]), ord(position[1][0]), int(position[1][1])]
valid = False
if position_number[0] - 1 == position_number[2]:
    if position_number[1] + 2 == position_number[3]:
        valid = True
    elif position_number[1] - 2 == position_number[3]:
        valid = True
elif position_number[0] - 2 == position_number[2]:
    if position_number[1] + 1 == position_number[3]:
        valid = True
    elif position_number[1] - 1 == position_number[3]:
        valid = True
elif position_number[0] + 1 == position_number[2]:
    if position_number[1] + 2 == position_number[3]:
        valid = True
    elif position_number[1] - 2 == position_number[3]:
        valid = True
elif position_number[0] + 2 == position_number[2]:
    if position_number[1] + 1 == position_number[3]:
        valid = True
    elif position_number[1] - 1 == position_number[3]:
        valid = True

if valid:
    print('VALIDO')
else:
    print('INVALIDO')
