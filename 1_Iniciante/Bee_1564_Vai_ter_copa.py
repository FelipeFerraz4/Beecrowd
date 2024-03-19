while True:
  try:
    prosteto = int(input())
    if prosteto == 0:
      print('vai ter copa!')
    else:
      print('vai ter duas!')
  except EOFError:
    break