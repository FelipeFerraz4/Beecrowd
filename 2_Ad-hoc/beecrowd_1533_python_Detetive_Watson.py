import sys

while True:
    number_suspects = int(sys.stdin.readline())
    
    if number_suspects == 0:
        break
    
    suspects = list(map(int, sys.stdin.readline().split()))
    new_suspects = suspects.copy()
    new_suspects.sort(reverse=True)
    crimanal = new_suspects[1]
    print(suspects.index(crimanal) + 1)