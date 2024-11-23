from sys import stdin
while True:
    number = int(stdin.readline())
    
    if number == 0:
        break
    
    santa_claus = 1
    touch = 0
    for i in range(number):
        position = list(map(int, input().split()))
        if sum(position) != 0:
            if santa_claus == 1 and position[1] != 0:
                touch += 1
                if position[0] == 0:
                    santa_claus = 0
                else:
                    santa_claus = 2
            elif santa_claus == 0 and position[0] != 0:
                if position[1] == 0:
                    touch += 1
                    santa_claus = 1
                else:
                    touch += 2
                    santa_claus = 2
            elif santa_claus == 2 and position[2] != 0:
                if position[1] == 0:
                    touch += 1
                    santa_claus = 1
                else:
                    touch += 2
                    santa_claus = 0
    print(touch)