music = [ 'PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']
times = int(input())
for x in range(times):
    values = input().split()
    print(music[ int(values[0]) + int(values[1]) ])