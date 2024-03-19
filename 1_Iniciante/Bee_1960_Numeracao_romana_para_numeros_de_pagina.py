valor = input()
unidadeRomanas = ['', 'I','II','III','IV','V','VI','VII','VIII','IX']
dezenaRomanas = ['', 'X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
centenaRomanas = ['', 'C','CC','CCC','CD','D','DC','DCC','DCCC','CM']

if  len(valor) == 3:
    centena = centenaRomanas[int(valor[0])]
    dezena = dezenaRomanas[int(valor[1])]
    unidade = unidadeRomanas[int(valor[2])]
    print(f'{centena}{dezena}{unidade}')
elif len(valor) == 2:
    dezena = dezenaRomanas[int(valor[0])]
    unidade = unidadeRomanas[int(valor[1])]
    print(f'{dezena}{unidade}')
elif len(valor) == 1:
    unidade = unidadeRomanas[int(valor[0])]
    print(unidade)
