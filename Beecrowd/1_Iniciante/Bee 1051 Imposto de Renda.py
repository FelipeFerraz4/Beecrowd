salary = float(input())

tax = 0

if salary > 4500:
    tax += (1000 * 0.08)
    tax += (1500 * 0.18)
    tax += ((salary-4500) * 0.28)
elif salary > 3000:
    tax += (1000 * 0.08)
    tax += ((salary-3000) * 0.18)
elif salary > 2000:
    tax += ((salary-2000) * 0.08)

if tax != 0:
    print(f'R$ {tax:.2f}')
else:
    print('Isento')