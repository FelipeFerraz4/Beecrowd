import sys

while True:
    line = sys.stdin.readline().strip()
    if line == '*':
        break
    letter = line[0].lower()
    tautagrams = True
    for word in line.split():
        if word[0].lower() != letter:
            tautagrams = False
            break
    print('Y' if tautagrams else 'N')