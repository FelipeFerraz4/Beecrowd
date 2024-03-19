def printNivel(treeSize, folha):
    treeNivel = (' ' * ((treeSize - folha)//2)) + '*' * folha
    print(treeNivel)

while True:
    try:
        treeSize = int(input())
        folhas = 1
        while(folhas <= treeSize):
            printNivel(treeSize, folhas)
            folhas += 2
        printNivel(treeSize, 1)
        printNivel(treeSize, 3)
        print()
        
    except EOFError:
        break