bolinhaAtual = int(input())
galhos = int(input())
bolinhas = (galhos//2) - bolinhaAtual
if bolinhas > 0:
    print(f'Faltam {bolinhas} bolinha(s)')
else:
    print('Amelia tem todas bolinhas!')
