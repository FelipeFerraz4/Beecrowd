times = int(input())

inside = 0
outside = 0

for i in range(0, times):
    value = int(input())
    if 10 <= value <= 20:
        inside += 1
    else:
        outside += 1

print(f'{inside} in')
print(f'{outside} out')
