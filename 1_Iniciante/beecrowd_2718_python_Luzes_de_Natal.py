number_test = int(input())
for i in range(number_test):
    values = str(bin(int(input())))[2:]
    big_sequence = 0
    current = 0
    for i, number in enumerate(values):
        if number == '1':
            current += 1
        if number == '0' or i == len(values) - 1:
            if current > big_sequence:
                big_sequence = current
            current = 0
    print(big_sequence)