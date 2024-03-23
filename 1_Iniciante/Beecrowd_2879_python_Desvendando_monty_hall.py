simulation = int(input())
count = 0

for i in range(simulation):
    door = int(input())
    if door != 1:
        count += 1
print(count)