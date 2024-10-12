numbers = list(map(int, input().split()))
prices = list(map(int, input().split()))

toll = 0

if numbers[0] >= numbers[1]:
    toll = (numbers[0] // numbers[1]) * prices[1]

price_total = (numbers[0] * prices[0]) + toll

print(price_total)