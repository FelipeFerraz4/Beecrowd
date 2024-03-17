import math

number = int(input())
numberMin = number / math.log(number)
numberMax = numberMin * 1.25506
print(f'{numberMin:.1f} {numberMax:.1f}')
