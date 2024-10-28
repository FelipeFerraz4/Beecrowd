number_tests = int(input())
for item in range(number_tests):
    values = list(map(int, input().split()))
    average = (sum(values) - values[0])/values[0]
    student = 0
    for item in range(1, values[0] + 1):
        if values[item] > average:
            student += 1
    print(f'{student/values[0] * 100:.3f}%')