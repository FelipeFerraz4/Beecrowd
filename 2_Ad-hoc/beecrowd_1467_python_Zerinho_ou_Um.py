from sys import stdin
def getPeople(number, result):
    if result[0] == number:
        print('A')
    elif result[1] == number:
        print('B')
    else:
        print('C')
        
while True:
    try:
        result = stdin.readline().strip().split()
        
        if not result:
            break
        
        if result.count('0') == 1:
            getPeople('0', result)
        elif result.count('1') == 1:
            getPeople('1', result)
        else:
            print('*')
    except EOFError:
        break
