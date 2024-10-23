while True:
    try:
        values = list(map(int, input().split()))
        print(values[0] * (2 * values[1]))
    except EOFError:
        break