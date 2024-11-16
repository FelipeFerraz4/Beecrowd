number = int(input())
fibonacci = [1, 1]

for i in range(2, number):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
fibonacci = fibonacci[::-1]
for i in range(number):
    if i + 1 == number:
        print(fibonacci[i])
    else:
        print(fibonacci[i], end=' ')
