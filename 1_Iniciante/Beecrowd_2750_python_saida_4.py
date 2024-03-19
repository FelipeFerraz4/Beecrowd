def showData(decimal, octal, hexadecimal):
    dicimalSpace = 6
    octalSpace = 4 
    if decimal > 9:
        dicimalSpace -= 1
    if octal > 7:
        octalSpace -= 1
    print('|' + ' ' * dicimalSpace + f'{decimal}' + ' ' * 4 + '|' +  ' ' * octalSpace + f'{octal}' + ' ' * 4 + '|' +  ' ' * 7 + f'{hexadecimal}' + ' ' * 7 + '|')


print('-' * 39)
print('|' + ' ' * 2 + 'decimal' + ' ' * 2 + '|' +  ' ' * 2 + 'octal' + ' ' * 2 + '|' +  ' ' * 2 + 'Hexadecimal' + ' ' * 2 + '|')
print('-' * 39)
for i in range(10):
    if i > 7:
        showData(i, i + 2, i)
    else:
        showData(i, i, i)
showData(10, 12, 'A')
showData(11, 13, 'B')
showData(12, 14, 'C')
showData(13, 15, 'D')
showData(14, 16, 'E')
showData(15, 17, 'F')
print('-' * 39)
