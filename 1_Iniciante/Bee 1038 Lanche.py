value = input().split()
item, quantity = int(value[0]), int(value[1])

price = [4.0, 4.5, 5.0, 2.0, 1.5]
total = price[item-1] * quantity
print(f'Total: R$ {total:.2f}')
