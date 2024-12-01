from sys import stdin
while True:
    hour1, minute1, hour2, minute2 = map(int, stdin.readline().split())
    if hour1 == minute1 == hour2 == minute2 == 0:
        break
    sleep = 0
    if hour1 < hour2:
        sleep = (hour2 - hour1) * 60 + minute2 - minute1
    elif hour1 > hour2:
        sleep = (24 - hour1 + hour2) * 60 + minute2 - minute1
    else:
        if minute1 < minute2:
            sleep = minute2 - minute1
        elif minute1 > minute2:
            sleep = 24 * 60 + minute2 - minute1
        else:
            sleep = 24 * 60
    print(sleep)