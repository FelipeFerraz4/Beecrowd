number_tests = int(input())
line = ''
for i in range(number_tests):
    if i % 2 == 0:
        line += input().replace('.', '')
    else:
        line += input().replace('.', '')[::-1]
foods = line.split('A')
food_max = max(foods, key=len)
print(len(food_max))