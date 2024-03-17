numberTests = int(input())
for i in range(numberTests):
    textLine = str(input())
    possiblePassword = 1
    for letter in textLine:
        if letter in 'aAeEiIoOsS':
            possiblePassword *= 3
        else:
            possiblePassword *= 2
    print(possiblePassword)