def merge_sort(array, swaps):
    if len(array) <= 1:
        return array, swaps
    mid = len(array) // 2
    left_haft, swaps = merge_sort(array[:mid], swaps)
    right_haft, swaps = merge_sort(array[mid:], swaps)
    new_array, swaps = merge(left_haft, right_haft, swaps)
    return new_array, swaps

def merge(left, right, swaps):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            swaps += len(left) - i
    
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array, swaps
    
from sys import stdin
number_test = int(stdin.readline())
for _ in range(number_test):
    test = int(stdin.readline())
    train_car = list(map(int, stdin.readline().split()))
    train_car, count = merge_sort(train_car, 0)
    print(f'Optimal train swapping takes {count} swaps.')