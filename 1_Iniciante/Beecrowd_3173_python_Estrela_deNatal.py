from math import floor
from datetime import datetime
from datetime import timedelta
revolucao = int(input())

anoBissestoJupiter = round((11.9 * revolucao) /4)
diasJupiter = floor((revolucao * 365 * 11.9) + anoBissestoJupiter)

anoBissestoSaturno = floor((29.6 * revolucao) /4)
diasSaturno = floor((revolucao * 365 * 29.6) + anoBissestoSaturno)

dataInicial = "2020-12-21"
dataInicial = datetime.strptime(dataInicial, "%Y-%m-%d")
dataJupiter = dataInicial + timedelta(days=diasJupiter)
dataSaturno = dataInicial + timedelta(days=diasSaturno)
print(f'Dias terrestres para Jupiter = {diasJupiter}')
print(f'Data terrestre para Jupiter: {dataJupiter.year}-{dataJupiter.month:02d}-{dataJupiter.day:02d}')
print(f'Dias terrestres para Saturno = {diasSaturno}')
print(f'Data terrestre para Saturno: {dataSaturno.year}-{dataSaturno.month:02d}-{dataSaturno.day:02d}')