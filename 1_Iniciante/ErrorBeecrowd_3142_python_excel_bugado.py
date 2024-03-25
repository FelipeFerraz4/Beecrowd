while True:
    try:
        column = str(input())
    except EOFError:
        break
    sizeColumn = (len(column)-1)
    if sizeColumn <= 2:
        numberColumn = (sizeColumn * 26) + (ord(column[(len(column)-1)]) - 64) 
        if numberColumn > 56:
            print('Essa coluna nao existe Tobias!') 
        else:
            print(numberColumn)
    else:
        print('Essa coluna nao existe Tobias!') 