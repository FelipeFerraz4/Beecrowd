from collections import Counter

number_test = int(input())

input()

for i in range(number_test):
    species_count = Counter()
    total_trees = 0
    
    if i > 0:
        print()
    
    while True:
        try:
            species = input().strip()
            if species == "":
                break
            species_count[species] += 1
            total_trees += 1
        except EOFError:
            break
    
    sorted_species = sorted(species_count.items())
    
    for species, count in sorted_species:
        percentage = (count / total_trees) * 100
        print(f"{species} {percentage:.4f}")
