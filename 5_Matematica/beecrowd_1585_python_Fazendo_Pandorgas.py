number_tests = int(input())
for _ in range(number_tests):
    values = list(map(int, input().split()))
    result = (values[0] * values[1])//2
    print(f'{result:} cm2')
