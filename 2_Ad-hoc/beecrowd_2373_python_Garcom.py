number_tests = int(input())
glasses = 0
for item in range(number_tests):
    values = list(map(int, input().split()))
    if values[0] > values[1]:
        glasses += values[1]
print(glasses)