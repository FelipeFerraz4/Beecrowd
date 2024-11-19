import re

count = 1
while True:
    if count != 1:
        print()
    
    number = int(input())
    
    if number == 0:
        break
    
    operation = input()
    
    # Remove zeros à esquerda dos números usando regex
    sanitized_operation = re.sub(r'\b0+(\d)', r'\1', operation)
    
    print(f'Teste {count}')
    print(eval(sanitized_operation))
    
    count += 1
