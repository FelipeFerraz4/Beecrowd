biggest = 0
position = 0
for i in range(1, 101):
    value = int(input())
    if i == 1:
        position = i
        biggest = value
    else:
        if value > biggest:
            position = i
            biggest = value

print(biggest)
print(position)