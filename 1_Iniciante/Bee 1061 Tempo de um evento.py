dia = input().split()
dia_start = int(dia[1]) 
hours = input().split()
hour_start = int(hours[0])
minute_start = int(hours[2])
second_start = int(hours[4])

dia = input().split()
dia_end = int(dia[1]) 
hours = input().split()
hour_end = int(hours[0])
minute_end = int(hours[2])
second_end = int(hours[4])

dia = dia_end - dia_start
hour = hour_end - hour_start
minute = minute_end - minute_start
second = second_end - second_start

if second < 0:
    second += 60
    minute -= 1

if minute < 0:
    minute += 60
    hour -= 1

if hour < 0:
    hour += 24
    dia -= 1

print(f'{dia} dia(s)')
print(f'{hour} hora(s)')
print(f'{minute} minuto(s)')
print(f'{second} segundo(s)')
