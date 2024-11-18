while True:
    try:
        number = int(input())
        result = number // 100
        if 0 < number < 100 or number % 100 >= 1:
            result += 1
        print(result)
    except EOFError:
        break