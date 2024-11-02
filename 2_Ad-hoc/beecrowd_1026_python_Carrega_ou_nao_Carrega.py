while True:
    try:
        numbers = list(map(int, input().split()))
        result = numbers[0] ^ numbers[1]
        print(result)
    except EOFError:
        break