while True:
    try:
        valores = input().split()
        numeroPessoas = int(valores[0])
        numeroDatas = int(valores[1])
        
        datas = []
        encontrado = -1
            
        for i in range(numeroDatas):
            dados = input().split()
            data = str(dados[0])
            datas.append(data)
            dia = 0
            for j in range(numeroPessoas):
                dia += int(dados[j+1])
            if dia == numeroPessoas and encontrado == -1:
                encontrado = i

        if encontrado != -1:
            print(datas[encontrado])
        else:
            print('Pizza antes de FdI')
        
    except EOFError:
        break