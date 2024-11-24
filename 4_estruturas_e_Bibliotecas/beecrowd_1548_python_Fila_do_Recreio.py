from sys import stdin
number_test = int(stdin.readline())
for _ in range(number_test):
    number_student = int(stdin.readline())
    scores = list(map(int, stdin.readline().split()))
    indexed_scores = [(i, scores[i]) for i in range(number_student)]
    indexed_scores.sort(key=lambda x: x[1], reverse=True)
    count = 0
    for i in range(number_student):
        if indexed_scores[i][0] == i:
            count += 1
    print(count)