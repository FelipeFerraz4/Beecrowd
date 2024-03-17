product1 = input().split()
id1, quantity1, product_value1 = int(product1[0]), int(product1[1]), float(product1[2])

product2 = input().split()
id2, quantity2, product_value2 = int(product2[0]), int(product2[1]), float(product2[2])

value = (quantity1 * product_value1) + (quantity2 * product_value2)

print(f'VALOR A PAGAR: R$ {value:.2f}')
