import sys

for line in sys.stdin:
    try:
        n = int(line.strip())
        phones = []

        for _ in range(n):
            phones.append(next(sys.stdin).strip())

        phones.sort()

        savings = 0
        for j in range(1, n):
            prefix_length = 0
            for k in range(len(phones[j])):
                if phones[j][k] == phones[j - 1][k]:
                    prefix_length += 1
                else:
                    break
            savings += prefix_length

        print(savings)

    except StopIteration:
        break
