while True:
    try:
        number_tests = int(input())
        list_meat = {}
        for i in range(number_tests):
            meat, quantity = input().split()
            list_meat[meat] = int(quantity)
        list_meat = dict(sorted(list_meat.items(), key=lambda x: x[1]))
        print(" ".join(list_meat.keys()))
    except EOFError:
        break