while True:
    try:
        sizeMaterial = int(input())
        sum1 = 0
        sum2 = 0
        for x in range(sizeMaterial):
            valores = input().split()
            score = int(valores[0])
            workload = int(valores[1])
            sum1 += score * workload
            sum2 += workload
        ira = sum1 / (sum2 * 100)
        print(f'{ira:.4f}')
    except EOFError:
        break