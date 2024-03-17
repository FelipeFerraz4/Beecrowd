stop = int(input())
while stop != 0:
    text = []
    bigSizeLine = -1
    for i in range(stop):
        linhaTexto = input().strip().split()
        linhaTexto = ' '.join(linhaTexto)
        if i == 0 or len(linhaTexto) > bigSizeLine:
            bigSizeLine = len(linhaTexto)
        text.append(linhaTexto)

    for i in range(stop):
        print(f'{str(text[i]).rjust(bigSizeLine)}')
    stop = int(input())
    if stop != 0:
        print()
