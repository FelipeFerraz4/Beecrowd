while True:
    try:
        numbers = input().split()
        population = int(numbers[0])
        numberQuery = int(numbers[1])
        scores = []
        for x in range(population):
            score = int(input())
            scores.append(score)
        scores = sorted(scores)
        scores.reverse()
        for x in range(numberQuery):
            position = int(input())
            print(scores[position-1])
    except EOFError:
        break