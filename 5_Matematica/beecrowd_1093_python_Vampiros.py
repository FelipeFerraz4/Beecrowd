def calculate_probability(turns_v1, turns_v2, attack_chance):
    if attack_chance == 3:
        return turns_v1 / (turns_v1 + turns_v2)
    else:
        prob_v1_hit = 1 - (6 - attack_chance) / 6
        failure_ratio = (1 - prob_v1_hit) / prob_v1_hit
        return (1 - failure_ratio**turns_v1) / (1 - failure_ratio**(turns_v1 + turns_v2))

while True:
    values = list(map(int, input().split()))

    if sum(values) == 0:
        break

    ev1, ev2, at, d = values

    turns_v1 = (ev1 + d - 1) // d
    turns_v2 = (ev2 + d - 1) // d

    result = calculate_probability(turns_v1, turns_v2, at)
    
    print(f'{result * 100:.1f}')

