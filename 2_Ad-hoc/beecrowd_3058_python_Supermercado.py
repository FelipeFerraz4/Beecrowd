test_number = int(input())
prices = []
for _ in range(test_number):
    price = list(map(float, input().split()))
    prices.append((price[0] * 1000)/price[1])
print(f'{min(prices):.2f}')