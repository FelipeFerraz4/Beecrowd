number = int(input())

if number <= 10:
    value = 7
elif number <= 30:
    value = 7 + ((number - 10) * 1)
elif number <= 100:
    value = 7 + 20 + ((number - 30) * 2)
else:
    value = 7 + 20 + 140 + ((number - 100) * 5)

print(value)