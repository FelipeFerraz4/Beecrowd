number_test = int(input())
plays = []
for _ in range(number_test):
    plays.append(int(input()))
if plays[0] < max(plays[1:]):
    print('N')
else:
    print('S')