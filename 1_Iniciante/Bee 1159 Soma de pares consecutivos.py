status = 0
while status != 1:
    number = int(input())
    sum = 0

    if number == 0:
        status = 1
        break
    
    if number % 2 == 1:
        number += 1
    
    for i in range(0, 5):
        sum += number
        number += 2
    
    print(sum)
