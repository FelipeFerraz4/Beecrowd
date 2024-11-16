while True:
    try:
        values = list(map(int, input().split()))
        hours = (12 * values[0]) // 360
        minute = (60 * values[1]) // 360
        print(f'{hours:0>2}:{minute:0>2}')
    except EOFError:
        break