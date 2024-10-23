number_tests = int(input())
values = input().split()
invite = 0
for i in range(number_tests):
    if values[i] == '1':
        invite += 1
    
print(invite)