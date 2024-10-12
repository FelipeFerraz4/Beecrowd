diameter = int(input())
dimensions = list(map(int, input().split()))

if all(d >= diameter for d in dimensions):
    print('S')
else:
    print('N')