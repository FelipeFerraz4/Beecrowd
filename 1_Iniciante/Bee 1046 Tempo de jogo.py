value = input().split()
hour1, hour2 = int(value[0]), int(value[1])

if hour2 <= hour1:
    time = (24 - hour1) + hour2
    print(f'O JOGO DUROU {time} HORA(S)')
else:
    print(f'O JOGO DUROU {hour2-hour1} HORA(S)')
