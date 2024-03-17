value = input().split()
a, b= int(value[0]), int(value[1])

if a % b == 0 or b % a == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
