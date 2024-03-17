value = input().split()
a, b, c = float(value[0]), float(value[1]), float(value[2])

sort = []

if a >= b and a >= c:
  sort.append(a)
  if b >= c:
    sort.append(b)
    sort.append(c)
  else:
    sort.append(c)
    sort.append(b)
elif b >= a and b >= c:
  sort.append(b)
  if a >= c:
    sort.append(a)
    sort.append(c)
  else:
    sort.append(c)
    sort.append(a) 
else:
  sort.append(c)
  if a >= b:
    sort.append(a)
    sort.append(b)
  else:
    sort.append(b)
    sort.append(a)  

if sort[0] >= sort[1]+sort[2]:
  print('NAO FORMA TRIANGULO')
else:
  if sort[0]**2 == sort[1]**2 + sort[2]**2:
    print('TRIANGULO RETANGULO')

  if sort[0]**2 > sort[1]**2 + sort[2]**2:
    print('TRIANGULO OBTUSANGULO')

  if sort[0]**2 < sort[1]**2 + sort[2]**2:
    print('TRIANGULO ACUTANGULO')

  if sort[0] == sort[1] == sort[2]:
    print('TRIANGULO EQUILATERO')
  elif sort[0] == sort[1] or sort[0] == sort[2] or \
                          sort[1] == sort[2]:
    print('TRIANGULO ISOSCELES')
