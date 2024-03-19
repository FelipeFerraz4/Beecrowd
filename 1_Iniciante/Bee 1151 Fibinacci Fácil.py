term1 = 1
term2 = 0

number = int(input())

if number == 0:
    print(term2)
elif number == 1:
    print(term1)
else:
    print(term2, end=' ')
    print(term1, end=' ')
    for i in range(2, number):
        temp = term1 + term2
        term2 = term1
        term1 = temp
        if i == number - 1:
            print(term1)
        else:
            print(term1, end=' ')
