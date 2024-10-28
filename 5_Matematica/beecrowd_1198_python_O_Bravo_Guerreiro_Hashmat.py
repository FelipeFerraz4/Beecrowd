while True:
    try:
        solders = list(map(int, input().split()))
        print(abs(solders[1] - solders[0]))
    except EOFError:
        break