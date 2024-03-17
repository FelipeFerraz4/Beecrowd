while True:
    try:
        times = int(input())
        x = 0
        y = times - 1
        for i in range(times):
            for j in range(times):
                valor = 3
                if j == y:
                    valor = 2
                elif j == x:
                    valor = 1
                print(valor, end='')
            x += 1
            y -= 1
            print()
    except EOFError:
      break