odd = []
even = []

for i in range(0, 15):
    value = int(input())
    
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
    
    if len(odd) == 5:
        for i in range(0, 5):
            print(f'impar[{i}] = {odd[i]}')
        for i in range(0, 5):
            odd.pop()

    if len(even) == 5:
        for i in range(0, 5):
            print(f'par[{i}] = {even[i]}')
        for i in range(0, 5):
            even.pop()

for i in range(0, len(odd)):
    print(f'impar[{i}] = {odd[i]}')

for i in range(0, len(even)):
    print(f'par[{i}] = {even[i]}')
