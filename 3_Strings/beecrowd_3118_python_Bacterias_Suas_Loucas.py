# Código que não conseguiu passar no teste -> Time limit exceeded

params = list(map(int, input().split()))
rules = {}

for i in range(params[1]):
    values = input().split()
    rules[values[0]] = values[1]

bacteria = list('A')

for _ in range(params[0]):
    new_bacteria = []
    start = 0

    while start < len(bacteria):
        end = start + 1
        while end < len(bacteria) and bacteria[end] == bacteria[start]:
            end += 1
        group_length = end - start
        group = bacteria[start]
        new_bacteria.extend(rules.get(group, group) * group_length)
        start = end

    bacteria = new_bacteria

print(f"{bacteria.count('A')} {bacteria.count('B')}")