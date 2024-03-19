salary = float(input())

percent = [0.15, 0.12, 0.1, 0.07, 0.04]

if 0 <= salary <= 400:
  count = 0
elif  400 < salary <= 800:
  count = 1
elif  800 < salary <= 1200:
  count = 2
elif  1200 < salary <= 2000:
  count = 3
else:
  count = 4

add_salary = (salary * percent[count])
new_salary = salary + add_salary

print(f'Novo salario: {new_salary:.2f}')
print(f'Reajuste ganho: {add_salary:.2f}')
print(f'Em percentual: {percent[count]*100:.0f} %')
