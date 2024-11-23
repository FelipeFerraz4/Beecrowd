from sys import stdin
while True:
    number = int(input())
    
    if number == 0:
        break

    present = list(map(int, stdin.readline().split()))
    custe_present = []
    for i in range(number):
        custe_present.append(present[i] + present[number * 2 - i - 1])
    print(f'{max(custe_present)} {min(custe_present)}')