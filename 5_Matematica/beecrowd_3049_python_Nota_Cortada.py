base1 = int(input())
base2 = int(input())

area_total = 70 * 160
area = ((base1+base2) * 70) / 2

if area > area_total / 2:
    print(1)
elif area == area_total / 2:
    print(0)
else:
    print(2)