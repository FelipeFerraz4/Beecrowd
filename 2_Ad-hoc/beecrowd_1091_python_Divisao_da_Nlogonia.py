while True:
    number_tests = int(input())
    
    if number_tests == 0:
        break
    
    pointD = list(map(int, input().split()))
    for item in range(number_tests):
        pointR = list(map(int, input().split()))
        
        if pointD[0] == pointR[0] or pointD[1] == pointR[1]:
            print('divisa')
        elif pointR[0] > pointD[0] and pointR[1] > pointD[1]:
            print('NE')
        elif pointR[0] < pointD[0] and pointR[1] < pointD[1]:
            print('SO')
        elif pointR[0] < pointD[0] and pointR[1] > pointD[1]:
            print('NO')
        else:
            print('SE')