number_test = int(input())
for i in range(number_test):
    values = list(map(int, input().split()))
    print(sum(values[1:]) - values[0] + 1)