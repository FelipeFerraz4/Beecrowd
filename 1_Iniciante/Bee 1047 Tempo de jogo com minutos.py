value = input().split()
hour1, minute1, hour2, minute2 = int(value[0]), int(value[1]), int(value[2]), int(value[3])

if hour2 < hour1:
    time_hour = (24 - hour1) + hour2
    if minute2 <= minute1:
        time_hour -= 1
        time_minute = (60 - minute1) + minute2
    else:
        time_minute = minute2 - minute1
    print(f'O JOGO DUROU {time_hour} HORA(S) E {time_minute} MINUTO(S)')
elif hour2 == hour1:
    if minute2 < minute1:
        time_hour = 23
        time_minute = (60 - minute1) + minute2
    elif minute2 == minute1:
        time_hour = 24
        time_minute = 0
    else:
        time_hour = 0
        time_minute = minute2 - minute1
    
    print(f'O JOGO DUROU {time_hour} HORA(S) E {time_minute} MINUTO(S)')
else:
    time_hour = hour2 - hour1
    if minute2 <= minute1:
        time_hour -= 1
        time_minute = (60 - minute1) + minute2
    else:
        time_minute = minute2 - minute1
    print(f'O JOGO DUROU {time_hour} HORA(S) E {time_minute} MINUTO(S)')
