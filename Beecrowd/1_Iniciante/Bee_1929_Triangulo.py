def trinaguloExiste(a, b, c):
    if abs(b - c) < a < (b + c):
      if abs(a - c) < b < (a + c):
        if abs(a - b) < c < (a + b):
            return True
    return False


valores = input().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
d = int(valores[3])

if trinaguloExiste(a, b, c) or trinaguloExiste(a, b, d) or trinaguloExiste(a, c, d) or trinaguloExiste(c, b, d):
  print('S')
else:
  print('N')
                    