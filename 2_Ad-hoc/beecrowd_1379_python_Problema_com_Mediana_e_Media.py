while True:
    numbers = list(map(int, input().split()))
    if sum(numbers) == 0:
        break
    small = min(numbers)
    big = max(numbers)
    result = small - (big - small)
    print(result)