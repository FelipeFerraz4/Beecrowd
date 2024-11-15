number_tests = int(input())
vacancies = int(input())
plays = []
for _ in range(number_tests):
    plays.append(int(input()))
plays.sort(reverse=True)
index = vacancies
last_play = plays[vacancies-1]
while index != len(plays) and plays[index] == last_play:
    index += 1
print(index)