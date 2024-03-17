while True:
    try:
      tempo = input().replace(':', ' ').split()
      hora = int(tempo[0])
      minutos = int(tempo[1])
      resposata = 0
      if hora == 7:
          resposata += minutos
      elif hora == 8:
          resposata += 60 + minutos
      elif hora == 9:
          resposata +=  120 + minutos  
      print(f'Atraso maximo: {resposata}')
    except EOFError:
      break
