from sys import stdin 
number_test = int(stdin.readline())
for i in range(number_test):
    diamonds = stdin.readline()
    
    count = 0
    left = 0
    
    for char in diamonds:
        if char == '<':
            left += 1
        elif char == '>' and left > 0:
            count += 1
            left -= 1
    
    print(count) 