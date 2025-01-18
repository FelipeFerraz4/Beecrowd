from sys import stdin

number = int(stdin.readline())
while number != 0:
    wagonsA = list(map(str, stdin.readline().split()))
    wagonsB = list(map(str, stdin.readline().split()))
    stack = []
    i = 0
    j = 0
    result = []
    while True:
        if stack and stack[-1] == wagonsB[j]:
            stack.pop()
            print('R', end='')
            j += 1
        elif len(wagonsA) > i and wagonsA[i] == wagonsB[j]:
            print('I', end='')
            print('R', end='')
            i += 1
            j += 1
        else:
            if len(wagonsA) == i:
                break
            stack.append(wagonsA[i])
            print('I', end='')
            i += 1
    if len(wagonsA) == i and stack:
        print(' Impossible')
    else:
        print()
        
    number = int(stdin.readline())  