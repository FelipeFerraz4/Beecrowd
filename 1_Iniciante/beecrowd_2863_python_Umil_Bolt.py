while True:
    try:
        number = int(input())
        runnes = []
        for i in range(number):
            runnes.append(float(input()))
        print(min(runnes))
    except EOFError:
        break