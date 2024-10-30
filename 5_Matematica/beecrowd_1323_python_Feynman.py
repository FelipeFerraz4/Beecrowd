run = True
while run:
    number = int(input())
    
    if number == 0:
        run = False
        break
    
    result = (number * (number + 1) * (2*number + 1))//6
    print(result)