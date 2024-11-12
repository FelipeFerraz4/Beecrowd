number_tests = int(input())
for _ in range(number_tests):
    values = list(map(int, input().split()))
    price_ingredients = list(map(int, input().split()))
    cakes = []
    for _ in range(values[2]):
        cake = list(map(int, input().split()))
        cake_cost = 0
        for i in range(1, (cake[0] * 2) + 1, 2):
            cake_cost += price_ingredients[cake[i]] * cake[i+1]
        cakes.append(cake_cost)
    min_cake_cost = min(cakes)
    print(values[0]//min_cake_cost)
    