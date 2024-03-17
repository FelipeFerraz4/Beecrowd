name = input()
salary = float(input())
sales = float(input())

salary_plus_bonus = salary + (sales * 0.15)
print(f'TOTAL = R$ {salary_plus_bonus:.2f}')
