values = input().split()
if int(values[0]) > int(values[1]) > int(values[2]) or int(values[2]) > int(values[1]) > int(values[0]):
    print('zezinho')
elif int(values[1]) > int(values[0]) > int(values[2]) or int(values[2]) > int(values[0]) > int(values[1]):
    print('huguinho')
else:
    print('luisinho')