values = list(map(int, input().split()))
runes = {}
for i in range(values[0]):
    rune = input().split()
    runes[rune[0]] = int(rune[1])
number = int(input())
rune_friend = input().split()
sum_friend = 0
for item in rune_friend:
    sum_friend += runes[item]
print(sum_friend)
if sum_friend < values[1]:
    print('My precioooous')
else:
    print('You shall pass!')