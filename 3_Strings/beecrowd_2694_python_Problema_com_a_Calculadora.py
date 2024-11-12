number_tests = int(input())
for _ in range(number_tests):
    numbers = []
    values = input()
    aux = ''
    for i in range(len(values)):
        if values[i].isdecimal():
            aux += values[i]
            if i + 1 == len(values) or values[i+1].isalpha():
                numbers.append(int(aux))
                aux = ''
                
    print(sum(numbers))