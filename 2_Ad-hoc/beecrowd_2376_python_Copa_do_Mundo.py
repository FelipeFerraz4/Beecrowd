teams_8 = 'ABCDEFGHIJKLMNOP'
matches_8 = []
matches_4 = []
matches_2 = []
matches_1 = []
for i in range(15):
    match = list(map(int, input().split()))
    if i < 8:
        matches_8.append(match)
    elif i < 12:
        matches_4.append(match)
    elif i < 14:
        matches_2.append(match)
    else:
        matches_1.append(match)
teams_4 = ''
for i in range(8):
    if matches_8[i][0] > matches_8[i][1]:
        teams_4 += teams_8[i * 2]
    else:
        teams_4 += teams_8[i * 2 + 1]
teams_2 = ''
for i in range(4):
    if matches_4[i][0] > matches_4[i][1]:
        teams_2 += teams_4[i * 2]
    else:
        teams_2 += teams_4[i * 2 + 1]
teams_1 = ''
for i in range(2):
    if matches_2[i][0] > matches_2[i][1]:
        teams_1 += teams_2[i * 2]
    else:
        teams_1 += teams_2[i * 2 + 1]
if matches_1[0][0] > matches_1[0][1]:
    print(teams_1[0])
else:
    print(teams_1[1])