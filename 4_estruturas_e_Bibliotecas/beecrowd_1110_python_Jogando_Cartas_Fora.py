from sys import stdin

number_test = int(stdin.readline())

odd = []
even = []

for _ in range(number_test):
    number = int(stdin.readline())
    
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

even.sort()
odd.sort(reverse=True)

print("\n".join(map(str, even + odd)))
