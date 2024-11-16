number_test = int(input())
car = 0
doll = 0
for i in range(number_test):
    text = input().split()
    if text[1] == 'F':
        doll += 1
    else:
        car += 1
print(f'{car} carrinhos')
print(f'{doll} bonecas')