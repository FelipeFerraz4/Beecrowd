while True:
    try:
        number = int(input())
        for i in range(number):
            codes = input().split()
            aux = (len(codes) - 1) * 3 + 1
            if len(codes[0]) == 2:
                aux += 1
            elif len(codes[0]) == 3:
                aux += 2
            
            aux += 96
            print(chr(aux))
                 
    except EOFError:
        break