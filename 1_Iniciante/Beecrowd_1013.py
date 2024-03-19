value = input().split()
a, b, c = int(value[0]), int(value[1]), int(value[2])

maiorAB = (a + b + abs(a-b))/2

maiorABC = int((maiorAB + c + abs(maiorAB-c))/2)

print(f'{maiorABC} eh o maior')
