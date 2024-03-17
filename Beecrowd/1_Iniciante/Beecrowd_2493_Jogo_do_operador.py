while True:
    try:
        quantidade = int(input())
        expressoes = []
        respostas = []
        reprovados = []
        for i in range(quantidade):
            form = input().split()
            termo = form[1].split('=')
            termo1 = int(form[0])
            termo2 = int(termo[0])
            termo3 = int(termo[1])
            expresao = [termo1, termo2, termo3]
            expressoes.append(expresao)
        
        for i in range(quantidade):
            resposta = input().split()
            respostas.append(resposta)
        
        for i in range(quantidade):
            formula = expressoes[int(respostas[i][1]) - 1]
            operacao = respostas[i][2]
            
            if operacao == '+':
                if formula[0] + formula[1] != formula[2]:
                    reprovados.append(respostas[i][0])
            elif operacao == '-':
                if formula[0] - formula[1] != formula[2]:
                    reprovados.append(respostas[i][0])
            elif operacao == '*':
                if formula[0] * formula[1] != formula[2]:
                    reprovados.append(respostas[i][0])
            else:
                if formula[0] + formula[1] == formula[2] or formula[0] - formula[1] == formula[2] or formula[0] * formula[1] == formula[2]:
                    reprovados.append(respostas[i][0])
        
        if len(reprovados) == 0:
            print('You Shall All Pass!')
        elif len(reprovados) == quantidade:
            print('None Shall Pass!')        
        else:
            reprovados.sort()
            print(' '.join(reprovados))
    except EOFError:
        break
