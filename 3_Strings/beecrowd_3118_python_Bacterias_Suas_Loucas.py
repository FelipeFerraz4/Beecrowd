def main():
    n, m = map(int, input().split())

    rules = {}
    for _ in range(m):
        key, value = input().split()
        rules[key] = value

    bacteria = "A"

    for _ in range(n):
        new_bacteria = ""

        start = 0
        while start < len(bacteria):
            end = start + 1
            while end < len(bacteria) and bacteria[end] == bacteria[start]:
                end += 1
            group_length = end - start
            group = bacteria[start:start + group_length]
            transformed = rules.get(group, group)
            new_bacteria += transformed
            start = end

        if new_bacteria == bacteria:
            break
        bacteria = new_bacteria

    countA = bacteria.count('A')
    countB = bacteria.count('B')

    print(countA, countB)

if __name__ == "__main__":
    main()