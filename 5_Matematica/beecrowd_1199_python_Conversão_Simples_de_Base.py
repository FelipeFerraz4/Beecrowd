run = True
while run:
    number = input()
    if number == '-1':
        run = False
        break
    
    if 'x' in number:
        print(int(number[2:], base=16))
    else:
        print("0x" + hex(int(number))[2:].upper())