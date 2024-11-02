def fibonacci(number):
    data_fibonacci = [1, 2]
    for i in range(2, number):
        data_fibonacci.append(data_fibonacci[i-1] + data_fibonacci[i - 2])
    return data_fibonacci[number-1]

run = True
while run:
    number = int(input())
    
    if number == 0:
        run = False
        break
    
    print(fibonacci(number))