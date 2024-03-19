contador = 0
somador = 0 
while contador < 3:
  falaCorvo = input()
  if falaCorvo[0] == 'c':
      contador += 1
      print(somador)
      somador = 0
  else:
      if falaCorvo[0] == '*':
          somador += 4
      if falaCorvo[1] == '*':
          somador += 2
      if falaCorvo[2] == '*':
          somador += 1