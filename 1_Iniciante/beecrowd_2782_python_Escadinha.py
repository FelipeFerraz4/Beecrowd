number_test = int(input())
numbers = list(map(int, input().split()))

if number_test == 1:
    print(1)
else:
    count = 1
    prev_diff = numbers[1] - numbers[0]
    
    for i in range(2, number_test):
        current_diff = numbers[i] - numbers[i - 1]
        if current_diff != prev_diff:
            count += 1
            prev_diff = current_diff
    
    print(count)