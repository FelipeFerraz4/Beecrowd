from sys import stdin, stdout

number_test = int(stdin.readline())
results = []

for _ in range(number_test):
    number = int(stdin.readline())
    values = list(map(int, stdin.readline().split()))
    
    numbers_odd = [x for x in values if x % 2 == 1]
    numbers_odd.sort()
          
    ordered_list = []
    for i in range((len(numbers_odd) + 1) // 2):
        ordered_list.append(numbers_odd[-(i + 1)])
        if i < len(numbers_odd) // 2:
            ordered_list.append(numbers_odd[i])
    
    results.append(" ".join(map(str, ordered_list)))

stdout.write("\n".join(results) + "\n")
