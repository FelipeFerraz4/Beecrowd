valores = input().split()
dia1 = int(valores[0])
dia2 = int(valores[1])
dia3 = int(valores[2])

respostas = [':)', ':(']
resposta = 0

if (dia1 < dia2) and (dia2 >= dia3):
    resposta = 1
elif (dia1 < dia2 < dia3) and (dia3 - dia2 < dia2 - dia1):
    resposta = 1
elif (dia1 > dia2 > dia3) and (dia2 - dia3 >= dia1 - dia2):
    resposta = 1
elif (dia1 == dia2) and (dia2 >= dia3):
    resposta = 1
    
print(respostas[resposta])
