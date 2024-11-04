run = True
while run:
    number = int(input())
    
    if number == 0:
        run = False
        break
    
    result = []
    i = 1
    while i * i <= number:
        result.append(str(i * i))
        i += 1
    
    print(" ".join(result))
