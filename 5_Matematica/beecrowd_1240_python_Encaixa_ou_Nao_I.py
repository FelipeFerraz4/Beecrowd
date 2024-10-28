number_tests = int(input())
for item in range(number_tests):
    values = input().split()
    if values[1] in values[0][-len(values[1]):]:
        print('encaixa')
    else:
        print('nao encaixa')