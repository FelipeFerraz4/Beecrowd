
def fat(number):
    sum = 1
    for i in range(1, number+1):
        sum *= i
    return sum

while True:
    try:
        valores = input().split()
        sum = fat(int(valores[0])) + fat(int(valores[1]))
        print(sum)
    except EOFError:
        break