stop = False
jipes = 0
people = 0
while stop == False:
    info = input().split()
    message = str(info[0])
    
    if message == 'SALIDA':
        jipes += 1
        people += int(info[1])
    elif message == 'VUELTA':
        jipes -= 1
        people -= int(info[1])
    else:
        stop = True
    
print(people)
print(jipes)
