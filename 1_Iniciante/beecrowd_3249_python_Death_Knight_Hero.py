from sys import stdin
number_test = int(stdin.readline())
count = number_test
for i in range(number_test):
    battle = stdin.readline()
    if 'CD' in battle:
        count -= 1
print(count)