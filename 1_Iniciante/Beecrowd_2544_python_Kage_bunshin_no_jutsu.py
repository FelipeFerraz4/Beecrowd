while True:
    try:
        clones = int(input())
        contador = 0
        clone = 1
        while(clone < clones):
            contador += 1
            clone *= 2
        print(contador)
    except EOFError:
        break