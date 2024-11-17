# Erro nos espaço do código
text = input().split()

number = text[0]
number_float = ''
rest = ''
new_text = ' '.join(text[1:])
for i, item in enumerate(new_text):
    if item.isdecimal() or item == '.':
        number_float += item
    else:
        rest = new_text[i:]
        break
rest = rest.strip()
caracter = rest[0]
phase = rest[1:].strip()

print(' '.join(text))

print(f'{number}\t{number_float}\t{caracter}\t{phase}')

print(f'{number:10}{number_float:10}{caracter:10}{phase:10}')
