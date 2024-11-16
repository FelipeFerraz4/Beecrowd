list_result = []
while True:
    try:
        values = list(map(int, input().split()))
        for i in range(values[2]):
            dimensions = list(map(int, input().split()))
            if (dimensions[0] <= values[0] and dimensions[1] <= values[1]) or (dimensions[1] <= values[0] and dimensions[0] <= values[1]):
                list_result.append('Sim')
            else:
                list_result.append('Nao')
    except EOFError:
        for response in list_result:
            print(response)
        break
