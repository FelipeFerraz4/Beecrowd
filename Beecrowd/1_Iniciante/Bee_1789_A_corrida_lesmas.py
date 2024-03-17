while True:
  try:
    times = int(input())
    velocidades = input().split()
    maiorNivel = 1
    for x in range(times):
        velocidade = int(velocidades[x])
        if velocidade >= 20:
            maiorNivel = 3
        elif maiorNivel < 2 and velocidade >= 10:
            maiorNivel = 2
    print(maiorNivel)
  except EOFError:
    break