numbers_ball = sum(list(map(int, input().split()))) - 1
if numbers_ball % 9 == 0:
    print('Dasher')
elif numbers_ball % 9 == 1:
    print('Dancer')
elif numbers_ball % 9 == 2:
    print('Prancer')
elif numbers_ball % 9 == 3:
    print('Vixen')
elif numbers_ball % 9 == 4:
    print('Comet')
elif numbers_ball % 9 == 5:
    print('Cupid')
elif numbers_ball % 9 == 6:
    print('Donner')
elif numbers_ball % 9 == 7:
    print('Blitzen')
else:
    print('Rudolph')
