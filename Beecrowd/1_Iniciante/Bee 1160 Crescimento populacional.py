times = int(input())

for i in range(0, times):
    value = input().split()
    populationA = int(value[0])
    populationB = int(value[1])
    growthA = float(value[2])
    growthB = float(value[3])

    status = 0
    year = 0
    while status != 1:
        year += 1
        populationA += int(populationA * (growthA/100))
        populationB += int(populationB * (growthB/100)) 
        
        if year > 100:
            print('Mais de 1 seculo.')
            break

        if populationA > populationB:
            status = 1
            print(f'{year} anos.')
            break
