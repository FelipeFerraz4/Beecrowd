number = int(input())
fibonacci_1 = 1
fibonacci_2 = 2
current = 1
count = 0
while count < number:
    if current == fibonacci_1:
        aux = fibonacci_1 + fibonacci_2
        fibonacci_1 = fibonacci_2
        fibonacci_2 = aux
    else:
        count += 1
        if count == number:
            break
    current += 1

print(current)
    