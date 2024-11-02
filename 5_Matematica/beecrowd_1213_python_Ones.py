while True:
    try:
        number = int(input())

        number_test = 1
        number_of_one = 1

        while number_test % number != 0:
            number_test = ((number_test * 10) + 1) % number
            number_of_one += 1
        print(number_of_one)
    except EOFError:
        break