from sys import stdin
number_test = int(stdin.readline())
for i in range(number_test):
    if i != 0:
        print()
    values = list(map(int, stdin.readline().split()))
    values_test = list(map(int, stdin.readline().split()))
    hashTable = [[] for _ in range(values[0])]
    for item in values_test:
        position = item % values[0]
        hashTable[position].append(item)
    for i, item in enumerate(hashTable):
        print(f'{i} -> ', end='')
        for item2 in item:
            print(f'{item2} -> ', end='')
        print('\\')
    
    