seconds = int(input())

times = [3600, 60, 1]
quantity_time = []

for i in times:
    aux = seconds // i
    quantity_time.append(aux)
    seconds = seconds % i

print(f'{quantity_time[0]}:{quantity_time[1]}:{quantity_time[2]}')
