age = int(input())

times = [365, 30, 1]
frase = ['ano(s)', 'mes(es)', 'dia(s)']
count = 0

for i in times:
    quantity = age // i
    age = age % i
    print(f'{quantity} {frase[count]}')
    count += 1
