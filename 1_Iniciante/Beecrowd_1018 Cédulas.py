value = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
print(f'{value}')

for i in notas:
    quantity_notas = value // i
    value = value % i
    print(f'{quantity_notas} nota(s) de R$ {i},00')
