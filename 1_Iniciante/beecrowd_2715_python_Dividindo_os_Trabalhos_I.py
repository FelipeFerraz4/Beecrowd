while True:
    try:
        number = int(input())
        values = list(map(int, input().split()))
        
        total_sum = sum(values)
        sum_left = 0
        min_diff = float('inf')
        
        for i in range(number):
            sum_left += values[i]
            sum_right = total_sum - sum_left
            diff = abs(sum_left - sum_right)
            
            if diff < min_diff:
                min_diff = diff
        
        print(min_diff)
        
    except EOFError:
        break
